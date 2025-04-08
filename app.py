import streamlit as st
from core.agent_manager import get_agent
from PIL import Image


#Sidebar:
st.sidebar.title("Your Info:")
user_name = st.sidebar.text_input("Your Name")
user_email = st.sidebar.text_input("Email")
user_jira_token = st.sidebar.text_input("Jira Token", type="password")
agent_type = st.sidebar.selectbox("Select Agent", ["JiraAgent"])  # More agents can be added later

# --- Main Interface ---
col1, col2 = st.columns([1, 9])
with col1:
    image = Image.open("pop.png")  # Replace with actual path if different
    st.image(image, width=100)
with col2:
    st.title("Agent Popsicle.")
st.markdown("Hi, I'm Popsicle! Enter a plain text description of what you'd like to do. I'll handle the rest.")

plain_text_input = st.text_area("Task Description")

if st.button("Popsicle it!"):
    if not all([user_name, user_email, plain_text_input]):
        st.error("Please fill in all fields.")
    else:
        user_info = {
            "name": user_name,
            "email": user_email,
            "jira_token": user_jira_token,
        }
        with st.chat_message("user"):
            st.markdown(plain_text_input)

        with st.chat_message("assistant"):
            st.markdown("👋 Hey! Popsicle is on it...")

        agent = get_agent(agent_type, user_info)
        # NEW: stream updates as tasks are created
        response_box = st.empty()
        for update in agent.handle_input(plain_text_input):
            response_box.markdown(update)
