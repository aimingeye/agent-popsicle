# 🍭 Popsicle — Your Multi-Agent Task Assistant

**Popsicle** is a friendly, pluggable multi-agent system with a sleek Streamlit UI. Just type what you want done in plain English, and Popsicle handles the rest. Currently, he knows how to work with Jira — but more capabilities are coming soon!

## ✨ Features

- 📝 Convert plain-text goals into **Jira Epics** and **Tasks**
- 🔐 Secure sidebar login with your name, email & API token
- 🤖 Powered by Popsicle — an extensible agent framework
- 📚 Modular design for adding new tools beyond Jira

## 📦 Tech Stack

- Python 🐍
- Streamlit 🎈
- Jira SDK
- Agent-oriented architecture (hello, future!)

## 🚀 How It Works

1. Fire up the app.
2. Enter your info in the sidebar.
3. Tell Popsicle what you need in plain English.
4. He parses your request and creates tasks in Jira — like magic!

## 📸 UI Preview

_(Add a screenshot here once you're ready)_

## 🔧 Setup

1. **Clone the repo**

```bash
git clone https://github.com/your-username/popsicle-agent.git
cd popsicle-agent
```

2. **Install requirements**

```bash
pip install -r requirements.txt
```

3. **Set Streamlit secrets**

Create `.streamlit/secrets.toml`:

```toml
jira_server = "https://your-domain.atlassian.net"
```

4. **Run the app**

```bash
streamlit run app.py
```

## 🧠 Coming Soon

- GitHub automation
- Notion task management
- Slack + Teams integration
- LLM-based custom task parsing

## 🙌 Contributions Welcome

Got an idea for a new agent? Popsicle loves learning new tricks! PRs, issues, and stars are always appreciated.
