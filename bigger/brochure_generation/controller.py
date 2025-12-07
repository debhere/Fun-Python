import os
from dotenv import load_dotenv
from dataclasses import dataclass


@dataclass
class ModelInfo:
    load_dotenv(override=True)

    openai_api_key: str = os.getenv('OPENAI_API_KEY')
    gemini_api_key: str = os.getenv('GEMINI_API_KEY')

    # gpt_prompt_model: str = 'gpt-4.1'
    gpt_translation_model: str = 'gpt-5-mini'
    gemini_brochure_model: str = 'gemini-2.5-flash'

    gemini_url: str = "https://generativelanguage.googleapis.com/v1beta/openai"

    system_prompt_generate: str = """
    You are a professional consultant who has worked for the best consulting firms across the globe. You
    analyze of a website and prepare short, crisp and professional brochure ensuring industry standards. Respond
    in markdown. Do not wrap the mark down in code block - respond just in markdown.
    """

    system_prompt_translate: str = """
    You are a professional translator who has worked with multinational companies across the globe. You
    understand the business context as well as the geography and use proper words as appropriate. You will
    get the content either in text or markdown and you need to translate and respond in markdown. Do not wrap the 
    markdown in code block - respond just in markdown.
    """
