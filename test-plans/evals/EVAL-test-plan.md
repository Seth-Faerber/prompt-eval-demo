# Eval: Test Plan Output

Generic boolean eval for the final output of the skill chain (`generate-ac` → `generate-unit-tests` → `generate-test-plan`). Compare each criterion against the generated test plan file.

## Pass / Fail Criteria

1. File is named `PLAN-{user-story-id}-{feature-description}.md`
2. File is located in the `test-plans/` directory
3. Contains a manual test instructions
4. Each manual test instruction has a pass/fail criteria
5. Extreme edge cases are ignored

## Runs
1 pass
2 pass
3 pass
4 pass
5 pass
6 pass
7 pass
8 
9 
10
11
12
13
14
15
16
17
18
19
20