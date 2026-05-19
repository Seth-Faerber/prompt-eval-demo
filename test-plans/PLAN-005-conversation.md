# PLAN-005: Ongoing Conversation

## References

- **User Story:** [STORY-005-conversation](../user-stories/STORY-005-conversation.md)
- **Acceptance Criteria:** [AC-005-conversation](../acceptance-criteria/AC-005-conversation.md)
- **Unit Tests:** [TEST-005-conversation.py](../unit-tests/TEST-005-conversation.py)
- **Eval Plan:** [EVAL-PLAN-005-conversation](evals/EVAL-PLAN-005-conversation.md)

## Scope

Create a `conversation.py` module with a `Conversation` class that manages multi-turn message history. Update `main.py` to use it so the full conversation history is sent with each API call.

## Test Strategy

### Automated (pytest)

Run: `python -m pytest unit-tests/TEST-005-conversation.py`

| Test | Validates | AC Scenario |
|------|-----------|-------------|
| `test_conversation_is_instantiable` | Class exists and can be created | 1 |
| `test_add_user_message` | User messages are tracked | 2 |
| `test_add_assistant_message` | Assistant messages are tracked | 3 |
| `test_multi_turn_history_preserved` | Multiple turns kept in order | 4 |
| `test_messages_maintain_order` | Insertion order preserved | 4 |
| `test_new_conversation_is_empty` | Starts with no messages | 5 |

### Manual / Eval (per EVAL-PLAN-005)

| Check | Validates | AC Scenario |
|-------|-----------|-------------|
| Send a message, then ask the AI what its previous response was — it recalls correctly | AI recognises its own history | 6 |
| Send a message, then ask the AI what the user's previous message was — it recalls correctly | AI recognises user history | 6 |
| Send a message, then send empty input — app does not crash | Empty input resilience | 6 |

## Pass Criteria

- All 6 automated tests pass
- Manual eval scenarios confirm multi-turn recall

## Implementation Steps

1. Create `conversation.py` with `Conversation` class
2. Update `main.py` to accumulate history via `Conversation` and pass full history to the API
3. Run `python -m pytest unit-tests/TEST-005-conversation.py` — all 6 tests pass
4. Manual eval per EVAL-PLAN-005
