#!/usr/bin/env python3
"""Check every skill in skills/ before packaging or release.

For each skills/<folder>/SKILL.md it checks that:
- the file starts with a YAML header containing `name` and `description`
- `name` matches the folder, uses lowercase letters, digits and hyphens, and is at most 64 characters
- `description` is present and at most 1,024 characters
- every relative Markdown link in the skill's files points to a file that exists

No dependencies. Exits non-zero if anything fails.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)\s#]+)(?:#[^)]*)?\)")


def header(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip("\"'")
    return fields


def check_skill(folder: Path) -> list[str]:
    errors = []
    skill_md = folder / "SKILL.md"
    if not skill_md.exists():
        return [f"{folder.name}: missing SKILL.md"]
    fields = header(skill_md.read_text(encoding="utf-8"))
    if fields is None:
        return [f"{folder.name}: SKILL.md must start with a --- header block"]
    name = fields.get("name", "")
    description = fields.get("description", "")
    if not name:
        errors.append(f"{folder.name}: header has no name")
    elif name != folder.name:
        errors.append(f"{folder.name}: name '{name}' doesn't match the folder name")
    elif not NAME_RE.match(name) or len(name) > 64:
        errors.append(f"{folder.name}: name must be lowercase letters, digits and hyphens, at most 64 characters")
    if not description:
        errors.append(f"{folder.name}: header has no description")
    elif len(description) > 1024:
        errors.append(f"{folder.name}: description is {len(description)} characters (max 1,024)")
    for md in folder.rglob("*.md"):
        for target in LINK_RE.findall(md.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("mailto:"):
                continue
            if not (md.parent / target).exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link to {target}")
    return errors


def main() -> int:
    folders = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if not folders:
        print("No skills found in skills/")
        return 1
    errors = [e for f in folders for e in check_skill(f)]
    for e in errors:
        print(f"ERROR {e}")
    print(f"Checked {len(folders)} skills: {'OK' if not errors else f'{len(errors)} problem(s)'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
