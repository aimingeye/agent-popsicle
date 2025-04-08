from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import re
import streamlit as st
import json

def parse_tasks_with_llm(prompt: str, system_prompt: str) -> dict:

    llm = ChatOpenAI(
        model="gpt-4o-mini", 
        temperature=0.3, 
        openai_api_key=st.secrets["openai"]["api_key"]
    )

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)
    print(f"Response: {response.content}")

    response_text = response.content
    return clean_and_parse_json(response_text)

def clean_and_parse_json(response_content: str):
    # Remove triple backticks and optional "json"
    cleaned = re.sub(r"^```json|```$", "", response_content.strip(), flags=re.MULTILINE).strip()
    return json.loads(cleaned)