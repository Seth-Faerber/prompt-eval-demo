"""
Manage multi-turn conversation history for the Anthropic messages API.
"""


class Conversation:
    """Accumulates user and assistant messages for multi-turn dialogue."""

    def __init__(self):
        self._messages = []

    def add_user_message(self, content):
        """Append a user message to the history."""
        self._messages.append({"role": "user", "content": content})

    def add_assistant_message(self, content):
        """Append an assistant message to the history."""
        self._messages.append({"role": "assistant", "content": content})

    def get_messages(self):
        """Return the full message history as a list of dicts."""
        return list(self._messages)
