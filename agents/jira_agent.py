import streamlit as st
from jira import JIRA
from agents.base_agent import BaseAgent
from utils.llm_parser import parse_tasks_with_llm

token = st.secrets["jira"]["token"]

class JiraAgent(BaseAgent):
    def __init__(self, user_info):
        super().__init__(user_info)
        self.server = st.secrets["jira"]["server"]
        self.jira = JIRA(server=self.server, basic_auth=(user_info["email"], user_info["jira_token"]))

    def handle_input(self, plain_text):

        if plain_text.strip().lower() == "get epic fields":
            fields = self.jira.fields()
            return "\n".join(
                f"{field['name']} = {field['id']}" for field in fields if "epic" in field['name'].lower()
            )

        try:
            system_prompt = (
                "You're a Jira project manager, your name is Popsicle. Given a plain text goal, "
                "break it into a dictionary of Epics and related tasks in this JSON format and it should be a valid 'list of JSON objects' output:\n"
                "tasks = [{'summary': 'Epic: Sample Project Setup', 'type': 'Epic'}, "
                "{'summary': 'Set up GitHub repo', 'type': 'Task'}, "
                "{'summary': 'Add README', 'type': 'Task'}"
            )

            tasks = parse_tasks_with_llm(plain_text, system_prompt)

            project_key = "SCRUM"  # Replace with your Jira project key
            created = []
            print(f"Tasks to create: {tasks}")
            epic_key = None
            for field in self.jira.fields():
                if "epic" in field['name'].lower():
                    print(f"{field['name']} = {field['id']}")

            for task in tasks:
                issue_dict = {
                    'project': {'key': project_key},
                    'summary': task['summary'],
                    'issuetype': {'name': task['type']}
                }

                if task['type'] == "Epic":
                    new_issue = self.jira.create_issue(fields=issue_dict)
                    epic_key = new_issue.key
                    created.append(f"✅ {task['type']}: {new_issue.key} - {task['summary']}\n")
                else:
                    if epic_key:
                        issue_dict['parent'] = {'key': epic_key}  # Parent Epic field
                    new_issue = self.jira.create_issue(fields=issue_dict)
                    created.append(f"✅ {task['type']}: {new_issue.key} - {task['summary']} \n")

                yield "\n".join(created)

        except Exception as e:
            yield f"❌ Error: {str(e)}"