---
name: pre-bill-review
description: Use when reviewing a matter's or client's unbilled time before a bill goes out, for example "review the pre-bill for 10482-002" or "check October's unbilled time for Harborview". Flags problems, suggests fixes, and produces a markup for the billing attorney. Works with a billing-system connection such as the Juris MCP server, or with a pasted or exported pre-bill.
---

# Pre-bill review

## Goal

Give the billing attorney a marked-up pre-bill: every entry that needs attention, why, and a suggested fix, so the bill goes out sooner and with fewer write-downs. You review and suggest. You never change, approve, or release time in the billing system.

## Step 1: Get the unbilled time

Use the first option that's available:

1. **A billing-system connection.** With the Juris MCP server:
   - Find the matter with `find_matters` (or the client with `find_clients`) and confirm it with `get_matter`. Note the responsible and billing timekeepers.
   - Get the entries with `list_time_entries`, scope `unbilled`, for the matter (or client) and period. Ask for full narratives if they were cut short.
   - Use `list_billing_codes` to read task and activity codes, and `find_timekeepers` for names and roles.
   - **Pass on every caveat** in the tools' `notes`, such as placeholder status filters or incomplete results, at the top of your review.
2. **A pre-bill the user pasted or attached** (PDF, spreadsheet, or text export).
3. Otherwise, ask the user for one of these. Don't review from memory.

## Step 2: Check every entry

Apply these checks, in order, and keep track of which entries fail which check:

1. **Client guidelines.** If the `client-billing-guidelines` skill has a file for this client, check every rule in it, at its enforcement level (block, fix, or warn).
2. **Narratives.** If the `narrative-standards` skill is installed, apply it: vague wording, block billing, clerical work, missing purpose, privileged detail.
3. **Codes.** Missing or mismatched task and activity codes, where the matter requires them.
4. **Duplicates.** The same task on the same day by the same timekeeper, or two timekeepers billing the same meeting.
5. **Staffing.** More timekeepers than the client allows, or senior timekeepers on clearly junior tasks.
6. **Unusual time.** Entries much longer than similar work on the matter, days over 12 hours for one timekeeper, or time on dates the matter was closed.
7. **Late time.** Entries dated long before they were entered, if the client limits that.

Use [checks.md](checks.md) for the details of each check.

## Step 3: Write the markup

Follow [output-format.md](output-format.md). In short:

- A summary for the billing attorney: totals, how much time is affected, and the three most important issues.
- A table of flagged entries, most serious first, with a suggested fix for each.
- Who should act on each item: the timekeeper (fix a narrative), the billing attorney (write-down or staffing decision), or billing staff (codes, duplicates).

## Rules

- Never recommend a specific write-down amount as a decision. Show the time affected; the billing attorney decides.
- Never put privileged detail in your markup beyond what's in the entries.
- If the guidelines file is missing or out of date, say so at the top. Don't invent client rules.
- When unsure whether something is a problem, flag it as a question, not a violation.
