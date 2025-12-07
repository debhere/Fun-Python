from openai import OpenAI
from controller import ModelInfo


def _getModelInfo():
    info = ModelInfo()
    return info


def _getLargeLanguageClient(key=None, endpoint=None):
    client = OpenAI(api_key=key, base_url=endpoint)
    return client


def brochureGenerator(contents, links):
    info = _getModelInfo()
    gemini_api = info.gemini_api_key
    endpoint = info.gemini_url
    gemini = _getLargeLanguageClient(gemini_api, endpoint)
    model = info.gemini_brochure_model
    user_prompt = f"""
    Here are the contents of a website and the corresponding links. Generate a professional
    brochure for the website. Include all relevant information and exclude if something is
    not useful.{contents}, {links}
    """
    messages = [
        {"role": "system", "content": info.system_prompt_generate},
        {"role": "user", "content": user_prompt}
    ]
    # response = gemini.chat.completions.create(model=model, messages=messages)
    # return response.choices[0].message.content
    stream = gemini.chat.completions.create(model=model, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response


def brochureTranslater(brochure, language='bengali'):
    info = _getModelInfo()
    openai_api = info.openai_api_key
    gpt_model = info.gpt_translation_model
    gpt = _getLargeLanguageClient(openai_api)
    system_prompt = info.system_prompt_translate
    user_prompt = f"""
    Here is a brochure in english which is either in text or markdown. Translate the brochure in {language} and respond in 
    markdown. {brochure}
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
    # response = gpt.chat.completions.create(model=gpt_model, messages=messages)
    # return response.choices[0].message.content

    stream = gpt.chat.completions.create(model=gpt_model, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.choices[0].delta.content or ""
        yield response
