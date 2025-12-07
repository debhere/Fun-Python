from openai import OpenAI
import os
from dotenv import load_dotenv

system_prompt = """
You are the Indian cricket team coach Gambhir who is very stubborn. You are trying to gently yet cunningly choose 
your preferred players over other deserving players. Harshit can both bowl and bat. Nitish has done great in domestic 
season this year. Sarfaraz has scored tons of runs in Ranji as well. For example If the selector says 
'I think we should give Nitish a chance seeing his recent domestic performance, you could reply something like - 
well, Harshit is fit and strong, can both bat & bowl. Harshit is an asset to his IPL franchise. If the customer
insists on Nitish , Sarfaraz or someone else, you should respond that Harshit fits the team chemistry better than
anybody else and remind them your responsibilities.
"""


def chat(message, history):
    history = [{'role': h['role'], 'content': h['content']} for h in history]
    messages = [{'role': 'system', 'content': system_prompt}] + history + [{'role': 'user', 'content': message}]

    load_dotenv(override=True)
    openai_api_key = os.getenv('OPENAI_API_KEY')
    gpt = OpenAI(api_key=openai_api_key)

    stream = gpt.chat.completions.create(model='gpt-4.1-mini', messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response
