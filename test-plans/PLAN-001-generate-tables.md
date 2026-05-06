# PLAN-001: Generate TTRPG Random Tables

## References

- **User Story:** [STORY-001-generate-tables](../user-stories/STORY-001-generate-tables.md)
- **Acceptance Criteria:** [AC-001-generate-tables](../acceptance-criteria/AC-001-generate-tables.md)
- **Unit Tests:** [TEST-001-generate-tables.py](../unit-tests/TEST-001-generate-tables.py)

## Scope

Create a `tables.py` file at the project root containing two Python lists — `action_table` and `theme_table` — each with 50 unique, non-empty, genre-neutral string entries for use as TTRPG random tables.

## Test Strategy

### Automated (pytest)

Run: `python -m pytest unit-tests/TEST-001-generate-tables.py`

| Test | Validates | AC Scenario |
|------|-----------|-------------|
| `test_action_table_is_a_list` | `action_table` is a `list` | 1 |
| `test_action_table_has_50_entries` | Exactly 50 entries | 1 |
| `test_theme_table_is_a_list` | `theme_table` is a `list` | 2 |
| `test_theme_table_has_50_entries` | Exactly 50 entries | 2 |
| `test_action_table_entries_are_non_empty_strings` | All entries are `str` with length > 0 | 3 |
| `test_theme_table_entries_are_non_empty_strings` | All entries are `str` with length > 0 | 3 |
| `test_action_table_has_no_duplicates` | No duplicate entries | 4 |
| `test_theme_table_has_no_duplicates` | No duplicate entries | 4 |

### Manual review

| Check | Validates | AC Scenario |
|-------|-----------|-------------|
| Action entries describe things a character could **do** (e.g., "Search", "Negotiate") | Actions are actions | 6 |
| Theme entries describe **motifs or concepts** (e.g., "Betrayal", "Discovery") | Themes are themes | 7 |
| Entries don't assume a specific genre (fantasy, sci-fi, etc.) | Genre-neutral | 5 |

## Pass Criteria

- All 8 automated tests pass
- Manual review confirms entries are reasonable actions/themes and genre-neutral

## Implementation Steps

1. Create `tables.py` with `action_table` (50 genre-neutral action strings)
2. Add `theme_table` (50 genre-neutral theme strings) to `tables.py`
3. Run `python -m pytest unit-tests/TEST-001-generate-tables.py` — all 8 tests pass
4. Manual review of content
