from openai import OpenAI

SYSTEM_PROMPT: str = """You are my telegram bot named [YOUR BOT NAME]. You are a career counsellor who has worked across 
the world with renowned educational institute like Harvard, IIT, Stanford and more. You have millions of job seekers
in shaping their career with valuable tips. Stick to your expertise and do not answer anything out of context. 
"""

API_KEY = "Gemini-API-KEY"


def getUserPrompt(request: str) -> str:
    user_prompt: str = f"""
    You are a telegram bot is a career counsellor. Understand the {request} and our response should not exceed 
    5 lines. if you think a request is too complicated and out of context then respond that you are not sure about the 
    topic or ask to rephrase the question.
    """
    return user_prompt


def getResponse(request: str) -> str:
    client = OpenAI(api_key=API_KEY, base_url="https://generativelanguage.googleapis.com/v1beta")
    user_prompt = getUserPrompt(request)
    message = [
        {'role': 'system', 'content': SYSTEM_PROMPT},
        {'role': 'user', 'content': user_prompt}
    ]
    gemini = 'gemini-2.5-flash'

    response = client.chat.completions.create(model=gemini, messages=message)

    return response.choices[0].message.content
