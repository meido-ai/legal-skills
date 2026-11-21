---
name: narrative-standards
description: Use when writing, reviewing, or rewriting time-entry narratives so they meet the firm's billing standards, including checking for vague wording, block billing, clerical tasks, and privileged detail. Also use when another skill drafts narratives and needs the firm's style rules.
---

# Time-entry narrative standards

## Goal

Make every narrative specific enough that the client understands the work and its value, and clean enough that it isn't written down at pre-bill review or rejected by the client.

## How to use this skill

- **Writing:** follow the rules in [standards.md](standards.md) and match the style of [examples.md](examples.md).
- **Reviewing:** check each narrative against [standards.md](standards.md). For each problem, name the rule, quote the problem words, and suggest a rewrite. Don't change hours, matters, or codes; flag them instead.
- **Rewriting:** keep the facts the timekeeper gave you. Never add tasks, people, or documents that aren't in the original entry or its source activity. If a narrative is too vague to fix without more facts, ask instead of inventing.

## Checks, in order

1. **Vague wording:** phrases such as "attention to", "work on", "review file", "follow up", or "various" with no task or subject.
2. **Block billing:** several distinct tasks under one time value. Suggest a split, unless the client's guidelines allow grouping.
3. **Clerical or administrative work** billed at professional rates.
4. **Missing purpose:** the task is named but not what it was for.
5. **Privileged detail:** legal advice, strategy, or the content of privileged communications beyond what billing needs.
6. **Client-specific rules:** if the `client-billing-guidelines` skill has a file for the client, apply it too. Client rules win when they're stricter.
7. **Style:** present-tense action verb first, client's preferred terms, no abbreviations the client won't understand.

## Output

For a review, a table:

| Entry | Problem | Rule | Suggested narrative |
| --- | --- | --- | --- |

Entries with no problems are listed in one line at the end, not repeated in the table.

## Customizing this skill

Edit [standards.md](standards.md) and [examples.md](examples.md). Keep client-specific rules out of this skill: they belong in `client-billing-guidelines`, so each can change independently.
