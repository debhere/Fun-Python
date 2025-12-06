import gradio as gr
import requests
from scraper import get_content
from model import brochureGenerator


def generateBrochure(website: str):
    try:
        response = requests.get(website, timeout=5)
        print(response.status_code)
        texts, links = get_content(website)
        brochure = brochureGenerator(texts, links)
        yield from brochure
    except requests.exceptions.RequestException as e:
        return e


with gr.Blocks() as app:
    url = gr.Textbox(label="Enter the url of your website")
    markdown = gr.Markdown(label="Response: ")

    generateBtn = gr.Button("Generate Brochure")
    translateBtn = gr.Button("Translate Brochure", interactive=False)
    language = gr.Dropdown(['Bengali', 'Kannada', 'Hindi'], value='Bengali', interactive=False)

    generateBtn.click(fn=generateBrochure, inputs=url, outputs=markdown)


if __name__ == "__main__":
    app.launch()
