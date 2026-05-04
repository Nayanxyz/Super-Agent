import streamlit as st
import requests
import uuid

# === 1. UI CONFIGURATION ===
st.set_page_config(page_title="Enterprise Swarm", page_icon="🐝")
st.title("🐝 Enterprise AI Swarm")

# === 2. API CONNECTION (THE BRIDGE) ===
# [IMPORTANT]: Paste your actual Render URL here. Make sure it ends in /chat!
API_URL = "https://super-agent-0ycr.onrender.com/chat"

