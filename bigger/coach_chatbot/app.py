import gradio as gr
from model import chat

if __name__ == "__main__":
    app = gr.ChatInterface(fn=chat, title="Coach vs Selector")
    app.launch()
