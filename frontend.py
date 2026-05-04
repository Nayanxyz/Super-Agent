import streamlit as st
import requests
import uuid

# === 1. UI CONFIGURATION ===
st.set_page_config(page_title="Enterprise Swarm", page_icon="🐝")
st.title("🐝 Enterprise AI Swarm")

# === 2. API CONNECTION (THE BRIDGE) ===
# [IMPORTANT]: Paste your actual Render URL here. Make sure it ends in /chat!
API_URL = "https://super-agent-0ycr.onrender.com/chat"

# === 3. SESSION MEMORY ===
# We need to give this specific browser window a unique ID so the API remembers who we are.
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())  # Generates a random string like '123e4567-e89b-12d3...'

# We need to store the chat history just for the visual screen
if "messages" not in st.session_state:
    st.session_state.messages = []

# === 4. DRAW THE CHAT HISTORY ===
# This loops through all past messages and draws them on the screen
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

