---
name: time-entry-drafting
description: Use when a timekeeper asks to draft, reconstruct, or catch up on time entries from their calendar, email, meetings, or document activity for a day, week, or other date range. Produces draft entries for review. Never submits time.
---

# Drafting time entries

## Goal

Produce **draft** time entries for the timekeeper to review. You never submit, release, or post time to a billing system. The timekeeper decides what is recorded.

## Before you start

Confirm three things, asking only if they aren't clear from the request:

1. **Whose time.** Default to the person you're talking to.
2. **The date range.** "Yesterday", "this week", and "October 3 to 7" are all fine. Catching up on older days is fine too. Say that entries reconstructed long after the fact are less reliable.
3. **What you can see.** Check which sources are connected (for example, Microsoft 365 or Google Workspace email, calendar, and files). Tell the timekeeper which sources you used and which you couldn't reach, such as phone calls or work outside these systems, so they know what to add themselves.

## Steps

1. **Gather activity** for the range: calendar events the timekeeper attended, email they sent or substantively replied to, and documents they created or edited. Ignore email they only received.
2. **Match each activity to a client and matter** (see "Matching").
3. **Group** related activity on the same matter and day into one entry, unless the narrative standards or the client's billing guidelines prohibit grouping (block billing).
4. **Estimate duration** (see "Durations"), in the firm's billing increment (default 0.1 hour, rounded up).
5. **Write the narrative** following [narrative-standards.md](narrative-standards.md). If the `narrative-standards` skill is installed, follow it instead, because it holds the firm's full standards.
6. **Apply task and activity codes** from [task-codes.md](task-codes.md) when the matter uses them.
7. **Check client rules.** If the `client-billing-guidelines` skill is installed and has a file for this client, check each entry against it and note any problem.
8. **List anything uncertain** under "Needs review" instead of guessing.

## Matching

- Prefer explicit identifiers: matter numbers in email subjects, meeting titles, folder paths, or file names.
- Otherwise use client names, email domains, and participants. If a billing-system connection is available (for example, the Juris MCP server's `find_matters` tool), use it to confirm the matter number and that the matter is open.
- If more than one matter is plausible, don't pick one. Put the activity under "Needs review" with the candidates.
- Leave out clearly non-billable activity (firm administration, marketing, recruiting, personal) unless the timekeeper asks to include it. List what you left out in one line so nothing disappears silently.

## Durations

- **Meetings and calls on the calendar:** the scheduled length, unless the event was declined or cancelled.
- **Email:** estimate from length and substance. Group several short emails on one matter into one entry. A one-line reply is rarely more than 0.1.
- **Documents:** estimate from editing activity where available. Mark low-confidence estimates.
- Never pad. When unsure, give the lower estimate and mark it.

## Privilege and confidentiality

- Narratives describe the work, not privileged advice. Don't quote legal strategy, advice, or the content of privileged communications beyond what billing requires.
- Don't copy email text into narratives.
- Use only the activity you were given. Never invent meetings, documents, or matters.

## Output

A table with one row per draft entry:

| Date | Client-matter | Hours | Task / activity code | Narrative | Confidence | Source |
| --- | --- | --- | --- | --- | --- | --- |

- **Confidence:** high, medium, or low, with a few words on why for medium and low.
- **Source:** the activity the entry came from (for example, "Meeting: Harborview lease call, 10:00–10:45").

Then:

- **Needs review:** each uncertain item and the reason (unclear matter, overlapping time, possible block billing, guideline problem).
- **Not included:** one line listing activity treated as non-billable.
- **Not visible to me:** sources you couldn't check.

End by asking the timekeeper to review, edit, and enter or release the time themselves.

## Customizing this skill

Firm-specific details live in the supporting files, not in this file:

- [narrative-standards.md](narrative-standards.md): short version of the firm's narrative rules.
- [task-codes.md](task-codes.md): task and activity codes the firm uses.
- [examples.md](examples.md): good and bad example entries. Five strong examples teach style better than a page of rules.
