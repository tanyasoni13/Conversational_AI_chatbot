from fastapi import FastAPI, Request
from pydantic import BaseModel
from backend import get_response

app = FastAPI()


class ChatRequest(BaseModel):
    message: str
    model: str = "openai"  # Options: "openai", "gemini"
    history: list = []


@app.post("/chat")
async def chat_endpoint(chat_req: ChatRequest):
    response = get_response(chat_req.message, chat_req.model, chat_req.history)
    return {"response": response}
