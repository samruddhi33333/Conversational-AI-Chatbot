import requests

def chat_fn(message, history, llm_model):
    try:
        response = requests.post("http://127.0.0.1:8000/chat", json={
            "message": message,
            "model": llm_model
        })
        return response.json().get("response", "⚠️ No response from backend")
    except Exception as e:
        return f"❌ Error: {str(e)}"
