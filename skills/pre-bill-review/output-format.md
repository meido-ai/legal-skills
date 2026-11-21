# Pre-bill markup format

## 1. Header

- Client and matter, period reviewed, billing attorney.
- Source of the time (for example, "Juris, unbilled time, via MCP" or "pasted pre-bill").
- Caveats: anything the tools reported in their `notes`, and whether a client guidelines file was found and how current it is.

## 2. Summary

- Entries reviewed, total hours, and total fees (if available).
- Entries flagged, and the hours and fees they represent, split by level: **Block**, **Fix**, **Warn**, **Question**.
- The three issues that matter most, in plain sentences.

## 3. Flagged entries

Most serious first:

| Date | Timekeeper | Hours | Narrative (as entered) | Issue | Level | Suggested fix | Who acts |
| --- | --- | --- | --- | --- | --- | --- | --- |

- **Issue:** cite the rule, for example "Northwind rule 2: block billing" or "Narrative standards: vague wording".
- **Suggested fix:** a rewritten narrative, a split, a code, or a question.
- **Who acts:** timekeeper, billing attorney, or billing staff.

## 4. Clean entries

One line: "N entries had no issues."

## 5. Next steps

A short list grouped by who acts, so the markup can be sent to each person as it is.
