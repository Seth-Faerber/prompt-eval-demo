# AC-005: Ongoing Conversation

**User Story:** As a user, I want to have an ongoing conversation with the AI, so that we can continue to build on multiple turns of dialogue.

---

## Scenario 1: Conversation class exists and is importable

- **Given** the file `conversation.py` exists in the project root
- **When** I import `Conversation` from `conversation`
- **Then** the import succeeds without error

## Scenario 2: Conversation tracks user messages

- **Given** a new `Conversation` instance
- **When** I call `add_user_message("Hello")`
- **Then** `get_messages()` contains a dict with `{"role": "user", "content": "Hello"}`

## Scenario 3: Conversation tracks assistant messages

- **Given** a new `Conversation` instance
- **When** I call `add_user_message("Hello")` then `add_assistant_message("Hi there")`
- **Then** `get_messages()` contains both messages in order

## Scenario 4: Multi-turn history is preserved

- **Given** a `Conversation` with several user and assistant messages added
- **When** I call `get_messages()`
- **Then** all messages are returned in the order they were added
- **And** the list alternates between user and assistant roles

## Scenario 5: Conversation starts empty

- **Given** a new `Conversation` instance
- **When** I call `get_messages()`
- **Then** the result is an empty list

## Scenario 6: Main loop sends full history to the API

- **Given** the CLI application is running
- **When** the user sends multiple messages
- **Then** each API call includes all previous user and assistant messages
- **And** the AI can reference earlier parts of the conversation
