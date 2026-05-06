---
name: generate-unit-tests
description: Generate unit tests for acceptance criteria.
---

## Inputs

Take Gherkin-formatted acceptance criteria as input. If the user does not provide acceptance criteria, then ask them for it.

The acceptance criteria can be found in the `acceptance-criteria` directory at the root of this project.

## Output

Return unit tests for the acceptance criteria.

Write the unit tests to a file in the `unit-tests` directory at the root of this project. It should be named `TEST-{user-story-id}-{feature-description}.py`.

## Constraints

If you notice something in the acceptance criteria that is unclear or ambiguous, ask the user for clarification.

Analyze the range of unit tests scenarios from edge cases to normal cases. After identifying a variety of scenarios, only write tests for the most important and impactful ones.
