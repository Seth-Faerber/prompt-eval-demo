"""
Unit tests for STORY-003: Send Tuple to AI
Derived from AC-003-send-tuple.md

All tests mock the Anthropic API so no real API key is needed.

Run with: python -m pytest unit-tests/TEST-003-send-tuple.py
"""

from unittest.mock import patch, MagicMock

from interpreter import interpret_combination


def _mock_anthropic_response(text="A mocked interpretation."):
    """Return a MagicMock that mimics an Anthropic messages.create() response."""
    mock_block = MagicMock()
    mock_block.text = text
    mock_response = MagicMock()
    mock_response.content = [mock_block]
    return mock_response


# --- Scenario 1: Interpret function exists and is importable ---

def test_interpret_combination_is_callable():
    assert callable(interpret_combination)


# --- Scenario 2: Accepts a (action, theme) tuple ---

@patch("interpreter.Anthropic")
def test_accepts_tuple_without_error(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_client.messages.create.return_value = _mock_anthropic_response()
    mock_anthropic_cls.return_value = mock_client

    interpret_combination(("Search", "Betrayal"))


# --- Scenario 3: Returns a non-empty string interpretation ---

@patch("interpreter.Anthropic")
def test_returns_a_string(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_client.messages.create.return_value = _mock_anthropic_response("Some interpretation")
    mock_anthropic_cls.return_value = mock_client

    result = interpret_combination(("Search", "Betrayal"))
    assert isinstance(result, str)


@patch("interpreter.Anthropic")
def test_returns_non_empty_string(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_client.messages.create.return_value = _mock_anthropic_response("Some interpretation")
    mock_anthropic_cls.return_value = mock_client

    result = interpret_combination(("Search", "Betrayal"))
    assert len(result) > 0


# --- Scenario 4: Prompt includes both the action and theme ---

@patch("interpreter.Anthropic")
def test_prompt_contains_action_and_theme(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_client.messages.create.return_value = _mock_anthropic_response()
    mock_anthropic_cls.return_value = mock_client

    interpret_combination(("Search", "Betrayal"))

    call_kwargs = mock_client.messages.create.call_args
    prompt_text = str(call_kwargs)
    assert "Search" in prompt_text
    assert "Betrayal" in prompt_text


# --- Scenario 5: Function calls the Anthropic API ---

@patch("interpreter.Anthropic")
def test_calls_anthropic_api(mock_anthropic_cls):
    mock_client = MagicMock()
    mock_client.messages.create.return_value = _mock_anthropic_response()
    mock_anthropic_cls.return_value = mock_client

    interpret_combination(("Search", "Betrayal"))

    mock_client.messages.create.assert_called_once()
