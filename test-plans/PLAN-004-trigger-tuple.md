# PLAN-004: Trigger Tuple via Natural Language

## References

- **User Story:** [STORY-004-trigger-tuple](../user-stories/STORY-004-trigger-tuple.md)
- **Acceptance Criteria:** [AC-004-trigger-tuple](../acceptance-criteria/AC-004-trigger-tuple.md)
- **Unit Tests:** [TEST-004-trigger-tuple.py](../unit-tests/TEST-004-trigger-tuple.py)

## Scope

Create a `trigger.py` file with an `is_trigger(user_input)` function that detects whether the user is requesting a random TTRPG combo via natural language. Integrate it into `main.py` so the CLI intercepts trigger phrases, generates a random tuple, sends it to the AI, and displays the interpretation.

## Test Strategy

### Automated (pytest)

Run: `python -m pytest unit-tests/TEST-004-trigger-tuple.py`

| Test | Validates | AC Scenario |
|------|-----------|-------------|
| `test_is_trigger_is_callable` | Function exists and is callable | 1 |
| `test_positive_trigger_phrases` | Common trigger phrases return `True` | 2 |
| `test_negative_phrases_do_not_trigger` | Normal conversation returns `False` | 3 |
| `test_trigger_is_case_insensitive` | Case variations still trigger | 4 |

### Manual review

| Check | Validates | AC Scenario |
|-------|-----------|-------------|
| Type a trigger phrase in the CLI and confirm a random combo + interpretation is displayed | Main loop integration | 5 |

## Pass Criteria

- All 4 automated tests pass
- Manual test confirms end-to-end flow in the CLI

## Implementation Steps

1. Create `trigger.py` with `is_trigger()` using keyword matching
2. Update `main.py` to check `is_trigger()` before the normal API call, and route to randomizer + interpreter when triggered
3. Run `python -m pytest unit-tests/TEST-004-trigger-tuple.py` — all 4 tests pass
4. Manual CLI test
