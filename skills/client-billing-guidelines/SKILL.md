---
name: client-billing-guidelines
description: Use when checking time entries, narratives, expenses, or a pre-bill against a specific client's outside counsel billing guidelines, or when turning a client's guidelines document or past invoice rejections into rules. Each client has its own rules file in the clients folder.
---

# Client billing guidelines

## Goal

Catch entries that a client's outside counsel guidelines don't allow, before the bill goes out. Each client's rules live in one readable file that the firm owns, reviews, and updates.

## Checking entries against a client's rules

1. **Find the client's file** in [clients/](clients/). Files are named by client number and name, for example `10482-harborview-marine.md`. If there's no file for the client, say so and check only against general narrative standards. Don't guess at rules.
2. **Check the file is current.** Each file has an "Effective" date and a "Source" line. If the file is more than a year old, or the guidelines have a newer version, say so.
3. **Check every entry against every rule** in the file. Rules are numbered, so cite them.
4. **Apply the rule's enforcement level:**
   - **Block:** the entry can't go out as written. It must be fixed or removed.
   - **Fix:** the entry should be changed. Suggest the change.
   - **Warn:** point it out. The reviewer decides.
5. **Suggest a compliant version** of each flagged entry where you can (rewritten narrative, split entry, or removed task). Never change hours or matters yourself; flag them.

## Output

| Entry | Rule | Level | Problem | Suggested fix |
| --- | --- | --- | --- | --- |

Then totals: entries checked, and how many are blocked, need fixes, or have warnings. List the rules that had no violations in one line.

## Turning a guidelines document into a rules file

When a user provides a client's outside counsel guidelines (PDF, Word, or email):

1. Start from [clients/_template.md](clients/_template.md).
2. Extract **only the billing rules**: what can't be billed, staffing limits, narrative requirements, task-code requirements, rate rules, time limits, expense rules, and approval requirements. Leave out unrelated terms such as diversity reporting or conflicts, or list them briefly under "Other terms."
3. Write each rule as one checkable statement, with the section number of the guidelines it came from. Quote the guideline wording where precision matters.
4. Propose an enforcement level for each rule. Hard prohibitions ("will not pay for") are usually **Block**.
5. List anything ambiguous under "Questions for the relationship partner" instead of interpreting it.
6. Remind the user that a person who knows the client must review the file before it's used.

## Learning from past rejections

When a user provides past invoice rejections, reductions, or appeal results (for example, e-billing rejection reports):

1. Group the rejections by reason.
2. For each reason, check whether an existing rule covers it. If not, propose a new rule with the rejection examples as evidence.
3. Rank proposed rules by how much was written down or rejected.
4. Add them to the client's file only after a person approves them.

## Customizing this skill

Add one file per client in [clients/](clients/), copied from [clients/_template.md](clients/_template.md). [clients/example-northwind-insurance.md](clients/example-northwind-insurance.md) is a fictional, filled-in example. Delete it once you have real client files.
