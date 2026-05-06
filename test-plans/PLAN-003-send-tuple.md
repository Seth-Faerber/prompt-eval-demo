# PLAN-003: Send Tuple to AI

## References

- **User Story:** [STORY-003-send-tuple](../user-stories/STORY-003-send-tuple)
- **Acceptance Criteria:** [AC-003-send-tuple](../acceptance-criteria/AC-003-send-tuple.md)
- **Unit Tests:** [TEST-003-send-tuple.py](../unit-tests/TEST-003-send-tuple.py)

## Scope

Create an `interpreter.py` file at the project root containing an `interpret_combination(combination)` function that sends a random (action, theme) tuple to the Anthropic API and returns the AI's interpretation as a string.

## Test Strategy

### Automated (pytest)

Run: `python -m pytest unit-tests/TEST-003-send-tuple.py`

All tests mock the Anthropic API — no API key required to run.

| Test | Validates | AC Scenario |
|------|-----------|-------------|
| `test_interpret_combination_is_callable` | Function exists and is callable | 1 |
| `test_accepts_tuple_without_error` | Accepts `(action, theme)` tuple | 2 |
| `test_returns_a_string` | Return type is `str` | 3 |
| `test_returns_non_empty_string` | Return value is non-empty | 3 |
| `test_prompt_contains_action_and_theme` | Prompt sent to AI contains both values | 4 |
| `test_calls_anthropic_api` | `messages.create` is called exactly once | 5 |

## Pass Criteria

- All 6 automated tests pass

## Implementation Steps

1. Create `interpreter.py` with `interpret_combination()` that builds a prompt from the tuple and calls the Anthropic messages API
2. Run `python -m pytest unit-tests/TEST-003-send-tuple.py` — all 6 tests pass
