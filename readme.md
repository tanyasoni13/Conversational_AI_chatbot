 # Conversational Chatbot with OpenAI and Google Gemini

This project implements a conversational chatbot using FastAPI as the backend, Gradio as the frontend, and Langchain for integrating OpenAI and Google Gemini models. It allows users to interact with different AI models through a web interface. 

**Note:** Currently, only Google Gemini is working because OpenAI does not provide a free tier for its API.

## Requirements

- Python 3.x
- Virtual environment (optional but recommended)

### Dependencies

The project uses the following dependencies:

- `fastapi`: Web framework for building the backend API.
- `uvicorn`: ASGI server for running the FastAPI application.
- `gradio`: Web interface library to interact with the chatbot.
- `requests`: Used for making HTTP requests to the backend API.
- `langchain`: For managing language models and their interactions.
- `langchain-community`: Provides support for community-driven models.
- `langchain-google-genai`: Interface for Google Gemini API.
- `openai`: OpenAI API client (although not used in this project).
- `anthropic`: Interface for Anthropic API (though not used in the provided code).
- `python-dotenv`: For loading environment variables from a `.env` file.

### Installation

1. Clone the repository:
   git clone <https://github.com/tanyasoni13/demo_repo.git>

2. Set up a virtual environment (optional but recommended):
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:
  pip install -r requirements.txt

4. Create a .env file in the project root directory with the following variables:
  # OpenAI
  OPENAI_API_KEY=<your-openai-api-key>  # Optional, but not currently used
  
  # Google Gemini (Generative AI)
  GEMINI_API_KEY=<your-gemini-api-key>

5. Run the FastAPI backend server:
   uvicorn app:app --reload

6. To run the frontend, run the following:
   python ui.py

## Project Structure
  app.py: Contains the FastAPI application and API route for handling chat requests.
  
  backend.py: Implements functions to interact with the OpenAI and Google Gemini models using Langchain.
  
  ui.py: Implements the Gradio interface for users to interact with the chatbot.
  
  .env: Stores sensitive keys such as OpenAI and Gemini API keys.
  
  requirements.txt: Lists all required Python dependencies.


## How it works
  Frontend (Gradio):
  The frontend interface is built using Gradio, where users can select between OpenAI and Google Gemini models, type their messages, and receive responses from the models.
  
  Backend (FastAPI):
  The backend exposes a FastAPI POST endpoint /chat that handles incoming requests with a message, selected model, and chat history. It uses the appropriate model (OpenAI or Gemini) to generate a response.
  
  Langchain:
  Langchain handles the interactions with the language models (OpenAI and Gemini), passing the user's input and maintaining the conversation history.
  
  Model Choice:
  Users can select between OpenAI's GPT model (gpt-3.5-turbo) and Google Gemini models (e.g., gemini-1.5-pro). However, due to OpenAI not offering a free tier, the project currently only supports Google Gemini.

## Usage
  Open the Gradio interface at http://127.0.0.1:7860.
  
  Choose the model (currently only "gemini" is functional) from the dropdown menu.
  
  Type a message and either press "Send" or hit Enter to submit the message.
  
  The chatbot will respond based on the selected model.

