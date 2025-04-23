import os

async def get_response(message: str, model: str = "openai"):
    agent = AIAgent(model)
    return await agent.send_message(message)
