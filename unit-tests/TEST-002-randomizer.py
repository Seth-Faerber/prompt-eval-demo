"""
Unit tests for STORY-002: Randomizer
Derived from AC-002-randomizer.md

Run with: python -m pytest unit-tests/TEST-002-randomizer.py
"""

from randomizer import get_random_combination
from tables import action_table, theme_table


# --- Scenario 1: Randomizer function exists and is importable ---

def test_get_random_combination_is_callable():
    assert callable(get_random_combination)


# --- Scenario 2: Returns a tuple of two strings ---

def test_returns_a_tuple():
    result = get_random_combination()
    assert isinstance(result, tuple)


def test_tuple_has_two_elements():
    result = get_random_combination()
    assert len(result) == 2


def test_both_elements_are_non_empty_strings():
    action, theme = get_random_combination()
    assert isinstance(action, str) and len(action) > 0
    assert isinstance(theme, str) and len(theme) > 0


# --- Scenario 3: Returned action is from the action table ---

def test_action_is_from_action_table():
    for _ in range(20):
        action, _ = get_random_combination()
        assert action in action_table


# --- Scenario 4: Returned theme is from the theme table ---

def test_theme_is_from_theme_table():
    for _ in range(20):
        _, theme = get_random_combination()
        assert theme in theme_table


# --- Scenario 5: Results vary across multiple calls ---

def test_results_vary_across_calls():
    results = {get_random_combination() for _ in range(100)}
    assert len(results) > 1
