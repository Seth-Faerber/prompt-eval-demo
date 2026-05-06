---
name: generate-test-plan
description: Generate a test plan from a given user story, acceptance criteria, and unit tests.
---

## Inputs

Take a user story, acceptance criteria, and unit tests as input. If the user does not provide these, then ask them for it.

The user story, acceptance criteria, and unit tests can be found in the `user-stories`, `acceptance-criteria`, and `unit-tests` directories at the root of this project.

## Output

Return a test plan for the user story, acceptance criteria, and unit tests.

Write the test plan in a markdown file in the `test-plans` directory at the root of this project. It should be named `PLAN-{user-story-id}-{feature-description}.md`.

## Constraints

If you notice something in the user story, acceptance criteria, or unit tests that is unclear or ambiguous, ask the user for clarification.

Analyze the range of test scenarios from edge cases to normal cases. After identifying a variety of scenarios, only write tests for the most important and impactful ones.
