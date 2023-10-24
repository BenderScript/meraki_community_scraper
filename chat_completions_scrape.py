import os
import openai
from dotenv import load_dotenv

load_dotenv(override=True, dotenv_path=".env")

openai.api_key = os.getenv("OPENAI_API_KEY")


def clean_training_data(user_message):
    messages = []
    messages.append({"role": "system", "content": "Given a text, rewrite it with proper grammar, punctuation, "
                                                  "spelling, and formatting. Make sure that emails and URLs are valid "
                                                  "and consistent. Remove any non-printable characters (except space) "
                                                  "and any unnecessary or redundant words. Do not change the meaning "
                                                  "or tone of the original text."})
    messages.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, temperature=0.5
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.ServiceUnavailableError as e:
        print(e)
        print("Try again in a few seconds")
        return None


def rephrase_question(user_message):
    messages = []
    messages.append({"role": "system", "content": "Given a text, rewrite it as a question that can be used to "
                                                  "fine-tune a GPT model. The rewritten question should be "
                                                  "grammatically correct and should not change the meaning or tone of "
                                                  "the original text. Your answer should contain only the new text and "
                                                  "nothing more"})
    messages.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, temperature=0.6
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.ServiceUnavailableError as e:
        print(e)
        print("Try again in a few seconds")
        return None
    except openai.error.APIError as e:
        print(e)
        print("Timeout")
        return None


def rephrase_solution(user_message):
    messages = []
    messages.append({"role": "system", "content": "Given a text, rewrite it as a answer that can be used to "
                                                  "fine-tune a GPT model. The rewritten question should be "
                                                  "grammatically correct and should not change the meaning or tone of "
                                                  "the original text. Your answer should contain only the new text and "
                                                  "nothing more."})
    messages.append({"role": "user", "content": user_message})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages, temperature=0.6
        )
        return response["choices"][0]["message"]["content"]
    except openai.error.ServiceUnavailableError as e:
        print(e)
        print("Try again in a few seconds")
        return None
    except openai.error.APIError as e:
        print(e)
        print("Timeout")
        return None
