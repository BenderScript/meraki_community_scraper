
# How to Scrape a Forum for Awesome GPT Fine-Tuning Data

Welcome to this repository, where you will learn how to scrape a community forum for some amazing data that you can use to fine-tune your chatGPT model. This is a cool project that shows you how to build an AI solution from scratch, from data collection to model deployment.

## Scraping and Cleaning Data

Before we get to the fun part of GenAI, we need to get some data first. And not just any data, but high-quality data that is relevant and useful for our task.

Scraping a forum is not as easy as it sounds. There are many challenges and decisions that we need to face, such as:

- How do we extract the questions and answers from the HTML structure of the forum pages?
- How do we deal with the pagination of the forum pages? Do we scrape all the pages or just the first few?
- How do we select the best answers for each question? Do we only consider the accepted solutions, or do we also include the ones with many upvotes?
- How do we deal with grammar and spelling errors in the text? Do we correct them or leave them as they are?
- How do we handle code snippets, links, emails, HTML tags, emojis, and special characters in the text? Do we remove them or keep them? And if we keep them, how do we format them properly?

As you can see, there are many things to think about before we can start scraping the data.

## Rewriting the Questions and Answers 

Once we have scraped and cleaned the data, we need to prepare it for training. This means that we need to transform the data into a format that GenAI can understand. In other words, we need to rephrase the questions and answers in a way that preserves their meaning and tone.

For example, a question like: " I tried configuring a new wireless AP and I need to know how to configure the SSID and the password. Can someone help me? "
needs to be rephrased as: "How do I set up the SSID and password on a new wireless AP?"

The same goes for the answers. We need to rephrase them in a clear and concise way.

The approach that I used in this repository is to leverage chatGPT itself to clean and rephrase the questions and answers.

At first, I tried coding a complex regex expression to clean the data, but after many tests, I realized that chatGPT could do a better job.

I also found out that doing it in two steps was better. First, I asked chatGPT to clean the data, and then I asked it to rephrase it. Yes, this takes more time, but the results are worth it.

Okay, here is a possible rewritten version of that part:

## How to Run It

To make this repository work, you need **Python 3.9** or above on your computer. You also need to get the Python libraries in **requirements.txt** using pip:

You need a `.env` file with your OpenAI API key as in

```bash
OPENAI_API_KEY=<your api key>
```

To run it with the default settings, just type:

```bash
python3 main.py
```

## Feedback

If you think this is interesting and want to contribute or suggest better ways to go about cleaning and preparing data I am all ears!

