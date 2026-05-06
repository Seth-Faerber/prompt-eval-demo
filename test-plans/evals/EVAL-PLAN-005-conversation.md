An created test plan for the STORY-005-conversation should consider the following inputs:

- User Story
- Acceptance Criteria
- Unit Tests

Considering these three inputs, the test plan should specify the necessary steps to validate the implementation.

Scenarios to test:
1. The AI can recognize its own previous message
2. The AI can recognize the user's previous message
3. The AI doesn't choke when a user submits no input

Step by step instructions:
Scenario 1:
1. Send a message to the AI
2. Send another message to the AI asking it what its previous message was
3. Verify that it was identical

Scenario 2:
1. Send a message to the AI
2. Send another message to the AI asking it what the user's previous message was
3. Verify that it was identical

Scenario 3:
1. Send a message to the AI
2. Send an empty message to the AI
3. Verify that it doesn't choke

