import gradio as gr, requests

API_URL = "http://127.0.0.1:8000/chat"


def chat_with_mcp(message, model, chat_history):
    chat_history = chat_history or []
    payload = {
        "message": message,
        "model": model,
        "history": [{"sender": "user", "user": u, "bot": b} for u, b in chat_history],
    }

    try:
        bot_reply = requests.post(API_URL, json=payload).json()["response"]
    except Exception as e:
        bot_reply = f"{e}"

    chat_history.append((message, bot_reply))
    return "", chat_history  # clear textbox, update chat


with gr.Blocks() as demo:
    gr.Markdown("## Chat Demo")
    chatbot = gr.Chatbot()

    with gr.Row():
        txt = gr.Textbox(label="Your message", lines=2, placeholder="Type your message")
        send_btn = gr.Button("Send", variant="primary")
        model_dd = gr.Dropdown(
            ["openai", "gemini"], value="openai", label="Model", scale=0.5
        )

    # Enter key
    txt.submit(chat_with_mcp, [txt, model_dd, chatbot], [txt, chatbot])
    # Button click
    send_btn.click(chat_with_mcp, [txt, model_dd, chatbot], [txt, chatbot])

demo.launch(share=True)
