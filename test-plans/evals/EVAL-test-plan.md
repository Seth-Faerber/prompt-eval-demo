# Eval: Test Plan Output

Generic boolean eval for the final output of the skill chain (`generate-ac` → `generate-unit-tests` → `generate-test-plan`). Compare each criterion against the generated test plan file.

## Pass / Fail Criteria

1. File is named `PLAN-{user-story-id}-{feature-description}.md`
2. File is located in the `test-plans/` directory
3. Contains a manual test instructions
4. Each manual test instruction has a pass/fail criteria
5. Extreme edge cases are ignored

## Runs
