"""
Unit tests for STORY-005: Ongoing Conversation
Derived from AC-005-conversation.md

Scenario 6 (main loop integration) is tested via the eval plan.

Run with: python -m pytest unit-tests/TEST-005-conversation.py
"""

from conversation import Conversation


# --- Scenario 1: Conversation class exists and is importable ---

def test_conversation_is_instantiable():
    conv = Conversation()
    assert conv is not None


# --- Scenario 2: Conversation tracks user messages ---

def test_add_user_message():
    conv = Conversation()
    conv.add_user_message("Hello")
    messages = conv.get_messages()
    assert len(messages) == 1
    assert messages[0] == {"role": "user", "content": "Hello"}


# --- Scenario 3: Conversation tracks assistant messages ---

def test_add_assistant_message():
    conv = Conversation()
    conv.add_user_message("Hello")
    conv.add_assistant_message("Hi there")
    messages = conv.get_messages()
    assert len(messages) == 2
    assert messages[0] == {"role": "user", "content": "Hello"}
    assert messages[1] == {"role": "assistant", "content": "Hi there"}


# --- Scenario 4: Multi-turn history is preserved ---

def test_multi_turn_history_preserved():
    conv = Conversation()
    conv.add_user_message("First question")
    conv.add_assistant_message("First answer")
    conv.add_user_message("Second question")
    conv.add_assistant_message("Second answer")
    messages = conv.get_messages()
    assert len(messages) == 4
    assert messages[0]["role"] == "user"
    assert messages[1]["role"] == "assistant"
    assert messages[2]["role"] == "user"
    assert messages[3]["role"] == "assistant"
    assert messages[2]["content"] == "Second question"


def test_messages_maintain_order():
    conv = Conversation()
    conv.add_user_message("A")
    conv.add_assistant_message("B")
    conv.add_user_message("C")
    contents = [m["content"] for m in conv.get_messages()]
    assert contents == ["A", "B", "C"]


# --- Scenario 5: Conversation starts empty ---

def test_new_conversation_is_empty():
    conv = Conversation()
    assert conv.get_messages() == []
