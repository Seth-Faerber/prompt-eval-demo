# AC-002: Randomizer

**User Story:** As a software engineer on this project, I want to randomly select an action and theme from the tables, so that I can have a unique combination when I need them.

---

## Scenario 1: Randomizer function exists and is importable

- **Given** the file `randomizer.py` exists in the project root
- **When** I import `get_random_combination` from `randomizer`
- **Then** the import succeeds without error

## Scenario 2: Returns a tuple of two strings

- **Given** `get_random_combination` is imported from `randomizer`
- **When** I call `get_random_combination()`
- **Then** it returns a tuple
- **And** the tuple contains exactly 2 elements
- **And** both elements are non-empty strings

## Scenario 3: Returned action is from the action table

- **Given** `get_random_combination` is imported from `randomizer`
- **And** `action_table` is imported from `tables`
- **When** I call `get_random_combination()`
- **Then** the first element of the returned tuple is a member of `action_table`

## Scenario 4: Returned theme is from the theme table

- **Given** `get_random_combination` is imported from `randomizer`
- **And** `theme_table` is imported from `tables`
- **When** I call `get_random_combination()`
- **Then** the second element of the returned tuple is a member of `theme_table`

## Scenario 5: Results vary across multiple calls

- **Given** `get_random_combination` is imported from `randomizer`
- **When** I call `get_random_combination()` many times
- **Then** not all results are identical (randomness is present)
