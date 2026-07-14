from openai import OpenAI
from config import API_KEY, BASE_URL, MODEL

client = OpenAI(
    api_key=API_KEY,
    base_url=BASE_URL
)


def send_message(messages):
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        stream=True
        )
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            yield content



