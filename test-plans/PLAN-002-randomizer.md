# PLAN-002: Randomizer

## References

- **User Story:** [STORY-002-randomizer](../user-stories/STORY-002-randomizer)
- **Acceptance Criteria:** [AC-002-randomizer](../acceptance-criteria/AC-002-randomizer.md)
- **Unit Tests:** [TEST-002-randomizer.py](../unit-tests/TEST-002-randomizer.py)

## Scope

Create a `randomizer.py` file at the project root containing a `get_random_combination()` function that randomly selects one action from `action_table` and one theme from `theme_table`, returning them as a tuple.

## Test Strategy

### Automated (pytest)

Run: `python -m pytest unit-tests/TEST-002-randomizer.py`

| Test | Validates | AC Scenario |
|------|-----------|-------------|
| `test_get_random_combination_is_callable` | Function exists and is callable | 1 |
| `test_returns_a_tuple` | Return type is `tuple` | 2 |
| `test_tuple_has_two_elements` | Tuple has exactly 2 elements | 2 |
| `test_both_elements_are_non_empty_strings` | Both elements are non-empty `str` | 2 |
| `test_action_is_from_action_table` | First element is in `action_table` | 3 |
| `test_theme_is_from_theme_table` | Second element is in `theme_table` | 4 |
| `test_results_vary_across_calls` | Multiple calls produce different results | 5 |

## Pass Criteria

- All 7 automated tests pass

## Implementation Steps

1. Create `randomizer.py` with `get_random_combination()` that uses `random.choice` on both tables
2. Run `python -m pytest unit-tests/TEST-002-randomizer.py` — all 7 tests pass
