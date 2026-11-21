# Legal billing skills

Open-source skills that help law firms capture more billable time and get cleaner bills out faster, using the AI platform the firm already has. They're written in Anthropic's [Agent Skills](https://agentskills.io) format, which works in Claude Desktop, claude.ai, Claude Code, and the Claude API.

Each skill is a template. The structure and instructions are shared. Your firm's narrative standards, task codes, and client rules go in clearly marked files that you fill in and own.

Maintained by [Meido](https://meido.ai), an independent technology advisor for law firms.

## The skills

| Skill | What it does |
| --- | --- |
| [`time-entry-drafting`](skills/time-entry-drafting/SKILL.md) | Drafts time entries from a day's (or week's) calendar, email, and documents, citing where each entry came from. Lists anything uncertain for review. Never submits time. |
| [`narrative-standards`](skills/narrative-standards/SKILL.md) | Writes and reviews narratives against the firm's standards: vague wording, block billing, clerical work, privileged detail. |
| [`client-billing-guidelines`](skills/client-billing-guidelines/SKILL.md) | One rules file per client, checked against every entry at a set enforcement level (block, fix, or warn). Turns a client's guidelines document, or past invoice rejections, into rules. |
| [`pre-bill-review`](skills/pre-bill-review/SKILL.md) | Marks up a matter's unbilled time before it's billed: guideline problems, narratives, codes, duplicates, staffing, unusual time. Says who should act on each item. |

The skills work together. For example, `pre-bill-review` applies `client-billing-guidelines` and `narrative-standards` when they're installed.

## Works with the Juris MCP server

`pre-bill-review` can read unbilled time directly from Juris through the [Juris MCP server](https://github.com/meido-ai/juris-mcp), a read-only Claude Desktop extension. Without it, paste or attach a pre-bill export.

## Getting started

1. **Customize.** Fill in every file marked **Customize this file**:
   - `time-entry-drafting/narrative-standards.md`, `task-codes.md`, `examples.md`
   - `narrative-standards/standards.md`, `examples.md`
   - `client-billing-guidelines/clients/`: one file per client, copied from `_template.md`. Delete the fictional Northwind example.
   - `pre-bill-review/checks.md`: thresholds
2. **Package:** `bash scripts/package.sh` checks every skill and creates one zip per skill in `dist/`.
3. **Install:** see [docs/setup-claude.md](docs/setup-claude.md) for Claude Desktop, firm-wide provisioning, the Juris MCP server, and Claude Code.
4. **Pilot** with a few volunteers before rolling out. Compare drafts with what timekeepers actually recorded, and have someone who reviews pre-bills check the output.

## Design principles

- **People decide.** Skills draft, check, and suggest. They never submit, approve, or release time.
- **Flags over guesses.** Anything uncertain goes on a "Needs review" list.
- **Rules you can read.** Every client rule is a line in a file the firm can review, version, and audit.
- **No invented facts.** Skills use only the activity and entries they're given.
- **Confidentiality.** Narratives don't repeat privileged advice or strategy.

## Before using with real data

Using these skills means an AI model reads time entries, email, and documents that may be privileged. Confirm the firm's AI policy covers it and that your AI plan's data terms (retention, training) are acceptable. Example data in this repository is fictional.

## Contributing

Run `python3 scripts/validate.py` before opening a pull request. It checks each skill's header and links. CI runs the same check and packages the skills.

## License

[MIT](LICENSE). The skills are templates; your firm's customized standards and client rules are yours.
