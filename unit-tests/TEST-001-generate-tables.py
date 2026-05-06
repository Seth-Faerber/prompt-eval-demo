"""
Unit tests for STORY-001: Generate TTRPG Random Tables
Derived from AC-001-generate-tables.md

Scenarios 5-7 (genre-neutral content, action descriptions, theme descriptions)
are subjective content reviews and are not covered by automated unit tests.

Run with: python -m pytest unit-tests/TEST-001-generate-tables.py
"""

from tables import action_table, theme_table


# --- Scenario 1: Action table exists and is importable ---

def test_action_table_is_a_list():
    assert isinstance(action_table, list)


def test_action_table_has_50_entries():
    assert len(action_table) == 50


# --- Scenario 2: Theme table exists and is importable ---

def test_theme_table_is_a_list():
    assert isinstance(theme_table, list)


def test_theme_table_has_50_entries():
    assert len(theme_table) == 50


# --- Scenario 3: All entries are non-empty strings ---

def test_action_table_entries_are_non_empty_strings():
    for entry in action_table:
        assert isinstance(entry, str)
        assert len(entry) > 0


def test_theme_table_entries_are_non_empty_strings():
    for entry in theme_table:
        assert isinstance(entry, str)
        assert len(entry) > 0


# --- Scenario 4: All entries are unique within their table ---

def test_action_table_has_no_duplicates():
    assert len(action_table) == len(set(action_table))


def test_theme_table_has_no_duplicates():
    assert len(theme_table) == len(set(theme_table))
