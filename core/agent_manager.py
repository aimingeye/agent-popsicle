from agents.jira_agent import JiraAgent
# from agents.github_agent import GitHubAgent 

AGENT_REGISTRY = {
    "JiraAgent": JiraAgent,
    # "GitHubAgent": GitHubAgent,
}


def get_agent(agent_type: str, user_info: dict):
    """
    Returns an instance of the selected agent.
    """
    agent_cls = AGENT_REGISTRY.get(agent_type)
    if not agent_cls:
        raise ValueError(f"Unsupported agent type: {agent_type}")
    return agent_cls(user_info)
