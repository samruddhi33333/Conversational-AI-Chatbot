🤖 Conversational AI Chatbot
A simple chatbot app using FastAPI as the backend and Gradio as the frontend interface. You can interact with different LLMs like OpenAI, Anthropic, and Gemini.

🚀 Features
Interact with multiple LLMs

Built-in logic for simulated responses

Dropdown model selection

Clean chat interface using Gradio

🛠️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/your-repo.git
cd your-repo
2. Create a Virtual Environment and Activate It
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Run FastAPI Backend
bash
Copy
Edit
uvicorn index:app --reload
5. Run the Gradio Frontend
bash
Copy
Edit
python gradio_ui.py
🔄 Switching LLMs
Use the dropdown in the Gradio interface to switch between:

openai

anthropic

gemini

Each has custom logic to simulate real chatbot responses.