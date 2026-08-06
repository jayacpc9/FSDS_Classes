import gradio as gr
from nltk.chat.util import Chat, reflections
import chat_pairs as chatpair


# Initialize NLTK Chat
chat = Chat(chatpair.pairs, reflections)

# Gradio predict function
def chatbot_response(message, history):
    # Get response from NLTK chat engine
    reply = chat.respond(message)
    if not reply:
        reply = "our customer service will reach you"
    return reply

# Create the Gradio interface
demo = gr.ChatInterface(
    fn=chatbot_response,
    title="NLTK Chatbot",
    description="Hi, I'm Jaya and I like to chat. Please type lowercase English language to start.",
    examples=["hi", "what is your name?", "who is your favorite cricketer?"],
    # 'type' argument removed — newer gradio versions don't accept it here
)

if __name__ == "__main__":
    demo.launch()