import os
import openai
from prompt import system_msg

openai.api_key = os.getenv("OPENAI_API_KEY")


def gpt_process(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=0.2,
        max_tokens=1000,
        frequency_penalty=0.0
    )

    content = response.choices[0].message.content
    return content


def bild_prompt_for_gpt(text):
    user_msg = f"""'На входе:
    '''
    {text}
    '''
    На выходе:'
    """
    prompt = [{"role": "system", "content": system_msg}, {"role": "user", "content": user_msg}]

    return prompt
