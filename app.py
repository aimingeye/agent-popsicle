# app.py
import streamlit as st
from core.agent_manager import get_agent

# --- Sidebar: User Info ---
st.sidebar.title("User Info")
user_name = st.sidebar.text_input("Your Name")
user_email = st.sidebar.text_input("Email")
user_jira_token = st.sidebar.text_input("Jira Token", type="password")
agent_type = st.sidebar.selectbox("Select Agent", ["JiraAgent"])  # More agents can be added later

# --- Main Interface ---
st.title("🤖 Agent Popsicle")
st.markdown("Hi, I'm Popsicle! Enter a plain text description of what you'd like to do. I'll handle the rest.")

plain_text_input = st.text_area("Task Description")

if st.button("Run Agent"):
    if not all([user_name, user_email, plain_text_input]):
        st.error("Please fill in all fields.")
    else:
        user_info = {
            "name": user_name,
            "email": user_email,
            "jira_token": user_jira_token,
        }
        agent = get_agent(agent_type, user_info)
        response = agent.handle_input(plain_text_input)
        st.markdown(response)
