import json
import time
from datetime import datetime

import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

from chat_completions_scrape import clean_training_data, rephrase_question, rephrase_solution


class ScrapeForum:

    def __init__(self, max_pages=1, data_file="data.jsonl",
                 url='https://community.meraki.com/t5/Wireless-LAN/bd-p/wireless-lan'):
        self.messages = dict()
        self.data = []
        self.max_pages = max_pages
        self.data_file = data_file
        self.forum_url = url
        self.next_page_url = self.forum_url

    @classmethod
    def create_training_entry(cls, question, solution, system="You are a tech support person for the Meraki product "
                                                              "line. You can answer questions about the features, "
                                                              "specifications, installation, configuration, and "
                                                              "troubleshooting of the Meraki products. You are polite,"
                                                              "professional, and helpful. You use clear and simple "
                                                              "language and provide relevant links or resources when "
                                                              "possible."):
        return {"messages": [{"role": "system", "content": system},
                             {"role": "user", "content": question}, {"role": "assistant", "content": solution}]}

    def get_netloc_url(self):
        return urlparse(self.forum_url).scheme + "://" + urlparse(self.forum_url).netloc

    def run(self):
        base = self.get_netloc_url()

        page_num = 1
        while self.next_page_url:
            start_time = datetime.now()
            response = requests.get(self.next_page_url)
            # Parse the HTML content of the page with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Get the first tbody element
            tbody = soup.select('#grid > table > tbody')[0]

            # Get all tr elements under the first tbody
            questions = tbody.find_all('tr')

            for question in questions:
                qs_data = {}
                # Get the link to the full question
                link = question.select('a.page-link.lia-link-navigation.lia-custom-event')[0]['href']
                # Send a GET request to the question URL
                question_response = requests.get(base + link)
                # Parse the HTML content of the question page with BeautifulSoup
                question_soup = BeautifulSoup(question_response.text, 'html.parser')
                # Get the content of the question
                div_content = question_soup.select('div.lia-message-body-content')[0]

                for a in div_content.find_all('a', href=True):
                    url = a['href']
                    text = a.get_text(strip=True)
                    if text.startswith('http'):
                        new_text = url
                    else:
                        new_text = f"{text} ({url})"
                    a.string.replace_with(new_text)

                qs_data['question'] = div_content.get_text()

                # Check if there is an accepted solution
                solution_link_element = question_soup.select('a.lia-link-navigation.accepted-solution-link')
                if solution_link_element:
                    solution_link = solution_link_element[0]['href']
                    solution_response = requests.get(base + solution_link)
                    solution_soup = BeautifulSoup(solution_response.text, 'html.parser')
                    div_solution_content = solution_soup.select(
                        'div.lia-message-body-content:has(div.lia-message-body-accepted-solution-checkmark)')[0]

                    for a in div_solution_content.find_all('a', href=True):
                        url = a['href']
                        text = a.get_text(strip=True)
                        if text.startswith('http'):
                            new_text = url
                        else:
                            new_text = f"{text} ({url})"
                        a.string.replace_with(new_text)

                    qs_data['solution'] = div_solution_content.get_text()

                    # I found that doing in two passes yield better results
                    question = clean_training_data(qs_data['question'])
                    solution = clean_training_data(qs_data['solution'])

                    question = rephrase_question(question)
                    solution = rephrase_solution(solution)

                    if question is None or solution is None:
                        continue
                    training_entry = self.create_training_entry(question, solution)
                    self.data.append(training_entry)

            next_button = soup.find('a',
                                    {'class': f'lia-link-navigation lia-js-data-pageNum-{page_num + 1} lia-custom-event',
                                     'rel': 'next'})
            self.next_page_url = next_button['href'] if next_button else None
            print(f"Scraped page {page_num} of the forum. Next page: {self.next_page_url}")
            end_time = datetime.now()
            print(f"Iteration took {(end_time - start_time).total_seconds():.2f} seconds")
            if page_num >= self.max_pages:
                break
            page_num += 1

        # Write data to a JSONL file
        with open(self.data_file, 'w') as f:
            for item in self.data:
                f.write(json.dumps(item) + '\n')
