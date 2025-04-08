class BaseAgent:
    def __init__(self, user_info):
        self.user_info = user_info

    def handle_input(self, plain_text):
        """Parse and perform the task"""
        raise NotImplementedError("Each agent must implement `handle_input`.")
