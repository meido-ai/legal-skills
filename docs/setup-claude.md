# Setting up the skills in Claude

These steps cover Claude Desktop and claude.ai, the Juris MCP server, and Claude Code. Claude's menus change from time to time. If a menu name below doesn't match what you see, look for **Skills** in Claude's settings.

## Before you start

- **Get approval.** Skills don't send data anywhere by themselves, but using them means Claude reads time entries, email, and documents that may be privileged. Confirm the firm's AI policy covers this use and that the data terms of your Claude plan (retention, training) are acceptable.
- **Use a work plan.** Claude Team or Enterprise gives administrators control over connectors and skills. Skills require code execution to be turned on.
- **Customize first.** Fill in the files marked **Customize this file** in each skill (narrative standards, task codes, examples, client rules) before rolling out. The defaults are starting points, not your firm's standards.

## 1. Package the skills

From the repository folder:

```bash
bash scripts/package.sh
```

This checks every skill and creates one zip per skill in `dist/`, for example `dist/time-entry-drafting.zip`. Each zip contains the skill's folder.

## 2a. Install for yourself (Claude Desktop or claude.ai)

1. Open Claude's settings and find **Skills** (under **Capabilities** in recent versions).
2. Make sure code execution is turned on.
3. Upload the zip for each skill you want.
4. Start a new conversation and ask for something the skill covers, for example *"Draft my time entries for yesterday."* Claude loads the skill when the request matches its description.

## 2b. Install for the whole firm (Team or Enterprise)

Organization owners can provision skills for everyone, or for specific groups on Enterprise, under **Organization settings → Plugins & skills**. Start with a pilot group rather than the whole firm.

## 3. Add the Juris MCP server (optional)

The `pre-bill-review` skill works best with a live connection to the firm's billing system. For Juris, install the [Juris MCP server](https://github.com/meido-ai/juris-mcp) as a Claude Desktop extension:

1. Download `juris-mcp.mcpb` from its latest release, or get it from IT.
2. Open the file. Claude Desktop shows an install dialog. (Or open **Settings → Extensions** and drag the file in.)
3. Enter your Juris user name and password. Leave the fields marked *IT only* alone.
4. Ask Claude *"Check the Juris connection."*

Then try *"Review the pre-bill for 10482-002 for October."* The skill uses the Juris tools to read unbilled time.

The Juris MCP server is read-only, so Claude can review time but can't change or release it. See its README for its current status and open questions before using it with real data.

Without a billing-system connection, the skills still work: paste or attach a pre-bill export.

## 4. Connect email, calendar, and documents (for time-entry drafting)

`time-entry-drafting` needs to see the timekeeper's activity. In Claude, that means a Microsoft 365 or Google Workspace connector, which an administrator must approve. See [How to Connect Claude to Microsoft 365 at a Law Firm](https://meido.ai/blog/connect-claude-microsoft-365-law-firm).

## Claude Code

Copy a skill folder into `~/.claude/skills/` (for yourself) or `.claude/skills/` inside a project (for everyone working on it):

```bash
cp -R skills/pre-bill-review ~/.claude/skills/
```

## Updating

When you change a skill, run `scripts/package.sh` again and upload the new zip in place of the old one. Keep your firm's customized copy in your own repository, so changes are reviewed and versioned like any other firm standard.
