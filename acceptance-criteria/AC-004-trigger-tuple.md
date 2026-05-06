# AC-004: Trigger Tuple via Natural Language

**User Story:** As a user of this application, I want to be able to trigger the generation of a random tuple when I need it using natural language, so that I can get interpretations for my TTRPG game.

---

## Scenario 1: Trigger detection function exists and is importable

- **Given** the file `trigger.py` exists in the project root
- **When** I import `is_trigger` from `trigger`
- **Then** the import succeeds without error

## Scenario 2: Recognises common trigger phrases

- **Given** `is_trigger` is imported from `trigger`
- **When** I call `is_trigger` with inputs like "roll a random combo", "give me a scenario", "generate a combination", or "random table roll"
- **Then** the function returns `True` for each

## Scenario 3: Does not trigger on normal conversation

- **Given** `is_trigger` is imported from `trigger`
- **When** I call `is_trigger` with inputs like "What is Python?", "Tell me a joke", or "How do I sort a list?"
- **Then** the function returns `False` for each

## Scenario 4: Trigger detection is case-insensitive

- **Given** `is_trigger` is imported from `trigger`
- **When** I call `is_trigger` with "ROLL A COMBO" or "Roll Me A Scenario"
- **Then** the function returns `True` regardless of case

## Scenario 5: Main loop calls randomizer and interpreter when triggered

- **Given** the CLI application is running
- **When** the user types a trigger phrase
- **Then** the application generates a random (action, theme) tuple
- **And** sends it to the AI for interpretation
- **And** displays the interpretation to the user
