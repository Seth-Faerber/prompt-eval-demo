"""
Unit tests for STORY-004: Trigger Tuple via Natural Language
Derived from AC-004-trigger-tuple.md

Scenario 5 (main loop integration) is an integration concern tested manually.

Run with: python -m pytest unit-tests/TEST-004-trigger-tuple.py
"""

from trigger import is_trigger


# --- Scenario 1: Trigger detection function exists and is importable ---

def test_is_trigger_is_callable():
    assert callable(is_trigger)


# --- Scenario 2: Recognises common trigger phrases ---

POSITIVE_PHRASES = [
    "roll a random combo",
    "give me a scenario",
    "generate a combination",
    "random table roll",
    "roll the tables",
    "roll me a random scenario",
    "can you roll a combo for me",
    "I need a random combination",
]


def test_positive_trigger_phrases():
    for phrase in POSITIVE_PHRASES:
        assert is_trigger(phrase) is True, f"Expected True for: {phrase!r}"


# --- Scenario 3: Does not trigger on normal conversation ---

NEGATIVE_PHRASES = [
    "What is Python?",
    "Tell me a joke",
    "How do I sort a list?",
    "Explain recursion",
    "What's the weather today?",
]


def test_negative_phrases_do_not_trigger():
    for phrase in NEGATIVE_PHRASES:
        assert is_trigger(phrase) is False, f"Expected False for: {phrase!r}"


# --- Scenario 4: Trigger detection is case-insensitive ---

CASE_VARIANT_PHRASES = [
    "ROLL A COMBO",
    "Roll Me A Scenario",
    "GENERATE A RANDOM COMBINATION",
    "Give Me A Scenario",
]


def test_trigger_is_case_insensitive():
    for phrase in CASE_VARIANT_PHRASES:
        assert is_trigger(phrase) is True, f"Expected True for: {phrase!r}"
