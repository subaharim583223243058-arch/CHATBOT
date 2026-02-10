import streamlit as st
import google.generativeai as genai


# PAGE SETUP

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")

st.title("🤖 Simple Gemini Chatbot")

# API KEY INPUT

api_key = st.text_input(
    "Enter your Gemini API Key:",
    type="password"
)

if not api_key:
    st.warning("Please enter your API key to continue.")
    st.stop()

# CONFIGURE GEMINI

genai.configure(api_key=api_key)

model = genai.GenerativeModel("models/gemini-2.5-flash")


# CHAT HISTORY

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# USER INPUT

user_input = st.chat_input("Type your message...")

if user_input:

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Get reply
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = model.generate_content(user_input)
            reply = response.text

            st.markdown(reply)

    # Save reply
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

