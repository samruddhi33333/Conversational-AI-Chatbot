import gradio as gr
from agent.ai_agent import chat_fn

gr.ChatInterface(
    fn=chat_fn,
    additional_inputs=[
        gr.Dropdown(["openai", "anthropic", "gemini"], label="Choose LLM", value="openai")
    ],
    title="Conversational AI",
   
).launch()
