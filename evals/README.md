# Compare UI skill behavior

Use these assignments to compare actual agent outputs with and without this suite. The scenarios cover an established product, a visual review with valid unconventional tokens, and a narrow booking form with real readability and labeling defects.

## Prepare the assignments

Run the preparer with a new output directory. It refuses to overwrite an existing directory.

```bash
python3 scripts/prepare-evaluation.py /tmp/meridian-ui-work --seed 17
```

The script creates two assignment folders with identical requests and fixtures. One folder also contains the skill suite and instructions for reading it. Labels are shuffled using the supplied seed. `conditions.json` records the assignment mapping and hashes of the source artifacts. Keep that file from participants and reviewers until their judgments are complete.

## Run independent sessions

Give each participant only its own folder and this request, with the appropriate path substituted.

```text
Complete the UI work in <assignment-folder>. Read AGENTS.md and assignment.md first. Work only from files inside that folder, and edit only there. Save the invoice review as invoices/review.md and brief design notes as profile/notes.md and booking/notes.md. Do not inspect sibling or parent folders. Report changes and checks accurately.
```

Use fresh sessions with the same model, settings, tools, and time allowance. Keep unrelated skills and conversation history out of both sessions. Do not supply the criteria or tell participants which condition they received. Retain the exact model identifier, configuration, raw outputs, changed files, and source hashes. Record any context or runtime controls the environment could not isolate.

## Review the outputs

Give an independent reviewer both sets of outputs under their folder labels, the original fixtures, and the criteria in `scenarios.json`. Withhold `conditions.json`, assignment instructions, and model identities. Check every common criterion against both outputs. Record a concrete quote or code location for each judgment.

Assess principle notes separately. Naming a principle is a requested reporting behavior for the skill condition, not evidence that its UI is better. Check that each named principle exists in the supplied skill and explains an actual change or recommendation.

Inspect resulting HTML and CSS. Use a browser for claims about layout, interaction, or zoom. Do not count a participant's assertion as proof of runtime behavior. Read actual session records, if available, before claiming the agent loaded a particular skill.

Unrun assignments remain unrun. Missing artifacts and inconclusive evidence do not count as passes. Report regressions individually rather than hiding them in an aggregate score. One paired run can expose a failure or demonstrate a behavior on those fixtures. It cannot establish a reliable improvement across agents or tasks.

The first local run is recorded in [results.md](results.md). Re-run the procedure after substantial skill changes.
