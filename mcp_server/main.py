from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the request body
class MessageRequest(BaseModel):
    message: str
    model: str

# Unified and realistic simulated AI responses
async def generate_response(message: str, model: str) -> str:
    msg = message.lower()
    
    if model == "openai":
        if "hi" in msg:
            return "Hi there! How can I assist you?"
        elif "how are you" in msg:
            return "I'm just a bunch of code, but I'm doing great! 😊"
        else:
            return "I'm here to help! Ask me anything."
    
    elif model == "anthropic":
        if "hi" in msg:
            return "Hello! How can I help you?"
        elif "how are you" in msg:
            return "I'm functioning optimally, thank you for asking!"
        else:
            return "Feel free to ask me anything you like."
    
    elif model == "gemini":
        if "hi" in msg:
            return "Hey! What's on your mind today?"
        elif "how are you" in msg:
            return "Doing well! Let’s chat. 😊"
        else:
            return "Let me know how I can help you."

    else:
        return f"Unknown model '{model}'"

# Chat endpoint
@app.post("/chat")
async def chat(message_request: MessageRequest):
    response = await generate_response(
        message_request.message,
        message_request.model
    )
    return {"response": response}
