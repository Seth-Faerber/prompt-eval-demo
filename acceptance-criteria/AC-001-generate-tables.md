# AC-001: Generate TTRPG Random Tables

**User Story:** As a software engineer on this project, I want have two arrays of data which represent action and theme random tables for a TTRPG where each array has 50 entries, so that I can build features that use these tables.

---

## Scenario 1: Action table exists and is importable

- **Given** the file `tables.py` exists in the project root
- **When** I import `action_table` from `tables`
- **Then** `action_table` is a Python list
- **And** it contains exactly 50 entries

## Scenario 2: Theme table exists and is importable

- **Given** the file `tables.py` exists in the project root
- **When** I import `theme_table` from `tables`
- **Then** `theme_table` is a Python list
- **And** it contains exactly 50 entries

## Scenario 3: All entries are non-empty strings

- **Given** `action_table` and `theme_table` are imported from `tables`
- **When** I iterate over every entry in each table
- **Then** every entry is of type `str`
- **And** every entry has a length greater than 0 (no empty strings)

## Scenario 4: All entries are unique within their table

- **Given** `action_table` and `theme_table` are imported from `tables`
- **When** I check for duplicate values within each table
- **Then** `action_table` contains no duplicate entries
- **And** `theme_table` contains no duplicate entries

## Scenario 5: Entries are genre-neutral

- **Given** `action_table` and `theme_table` are imported from `tables`
- **When** I review the content of each entry
- **Then** the entries are generic enough to fit any TTRPG setting (fantasy, sci-fi, horror, etc.)

## Scenario 6: Action table entries represent actions

- **Given** `action_table` is imported from `tables`
- **When** I review the content of each entry
- **Then** each entry describes an action a character could take (e.g., "Search", "Negotiate", "Defend")

## Scenario 7: Theme table entries represent themes

- **Given** `theme_table` is imported from `tables`
- **When** I review the content of each entry
- **Then** each entry describes a theme or motif for a scenario (e.g., "Betrayal", "Discovery", "Survival")
