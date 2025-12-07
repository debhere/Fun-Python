import gradio as gr
import requests
from scraper import get_content
from model import brochureGenerator, brochureTranslater


def generateBrochure(website: str):
    try:
        response = requests.get(website, timeout=5)
        print(response.status_code)
        texts, links = get_content(website)
        brochure = brochureGenerator(texts, links)
        yield from brochure
    except requests.exceptions.RequestException as e:
        return e


def EnableTranslation():
    return gr.Button(interactive=True)


def EnableLanguageSelection():
    return gr.Dropdown(interactive=True)


def clearMarkdown():
    return gr.Markdown(value='')


def translateBrochure(content, language):
    translated = brochureTranslater(content, language)
    yield from translated


with gr.Blocks() as app:
    url = gr.Textbox(label="Enter the url of your website")
    markdown = gr.Markdown(label="Response: ")

    generateBtn = gr.Button("Generate Brochure")
    translateBtn = gr.Button("Translate Brochure", interactive=False)
    languageSelect = gr.Dropdown(['Bengali', 'Spanish', 'French'], value='Bengali', interactive=False)

    generateBtn.click(fn=generateBrochure, inputs=url, outputs=markdown)

    gr.on([generateBtn.click], EnableTranslation, None, translateBtn)
    gr.on([generateBtn.click], EnableLanguageSelection, None, languageSelect)

    translateBtn.click(fn=translateBrochure, inputs=[markdown, languageSelect], outputs=markdown)

if __name__ == "__main__":
    app.launch()
