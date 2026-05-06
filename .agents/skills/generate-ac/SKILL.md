---
name: generate-ac
description: Generate Gherkin-formatted acceptance criteria from a single user story.
---

## Inputs

Take a user story as input. If the user does not provide a user story id, then ask them for it.

The user story can be found in the `user-stories` directory at the root of this project.

The user story will be in format of "As a [type of user], I want to [action] so that [benefit]."

It should focus on the "what" and "why." 

Example: As a user, I want to reset my password so I can regain access if I forget it.

## Output

Return a Gherkin-formatted acceptance criteria document.

Format: Given/When/Then (Scenario, Context, Action, Outcome).

Focus: The "how" (specific, executable scenarios).

Example: 
- Given I'm on the login page
- When I click “Forgot password” and enter a registered email
- Then I receive a reset link within 5 minutes.

Write the output to a markdown file in the `acceptance-criteria` directory at the root of this project. It should be named `AC-{user-story-id}-{feature-description}.md`.

## Constraints

If you notice something in the user story that is unclear or ambiguous, ask the user for clarification.