import os
from langchain_community.chat_models import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import HumanMessage, AIMessage
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Get the API keys from the environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def get_model(model_name):
    if model_name == "openai":
        return ChatOpenAI(
            api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=0.5
        )
    elif model_name == "gemini":
        return ChatGoogleGenerativeAI(
            api_key=GEMINI_API_KEY, model="models/gemini-1.5-pro", temperature=0.5
        )
    else:
        raise ValueError("Unsupported model")


def get_response(message, model_name, history):
    chat = get_model(model_name)
    history_messages = [
        HumanMessage(content=msg["user"])
        if msg["sender"] == "user"
        else AIMessage(content=msg["user"])
        for msg in history
    ]
    history_messages.append(HumanMessage(content=message))
    reply = chat.invoke(history_messages)
    return reply.content
