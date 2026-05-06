# AC-003: Send Tuple to AI

**User Story:** As a software engineer on this project, I want to send the random tuple to an AI, so that I can get an interpretation of the combination.

---

## Scenario 1: Interpret function exists and is importable

- **Given** the file `interpreter.py` exists in the project root
- **When** I import `interpret_combination` from `interpreter`
- **Then** the import succeeds without error

## Scenario 2: Accepts a (action, theme) tuple

- **Given** `interpret_combination` is imported from `interpreter`
- **When** I call `interpret_combination(("Search", "Betrayal"))`
- **Then** the function does not raise a `TypeError`

## Scenario 3: Returns a non-empty string interpretation

- **Given** `interpret_combination` is imported from `interpreter`
- **When** I call `interpret_combination(("Search", "Betrayal"))`
- **Then** the return value is of type `str`
- **And** the return value has a length greater than 0

## Scenario 4: Prompt includes both the action and theme

- **Given** `interpret_combination` is imported from `interpreter`
- **When** the function builds a prompt from the tuple `("Search", "Betrayal")`
- **Then** the prompt sent to the AI contains the word "Search"
- **And** the prompt sent to the AI contains the word "Betrayal"

## Scenario 5: Function calls the Anthropic API

- **Given** `interpret_combination` is imported from `interpreter`
- **When** I call `interpret_combination(("Search", "Betrayal"))`
- **Then** the function makes a request to the Anthropic messages API
