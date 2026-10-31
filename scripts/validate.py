"""Validate package metadata and local links; no model calls or quality scoring."""

from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

import yaml

ROOT = Path(__file__).resolve().parents[1]


def check(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    skill = ROOT / "skills/interview-review"
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    check(front is not None, "Missing skill frontmatter")
    data = yaml.safe_load(front.group(1))
    check(isinstance(data, dict), "Frontmatter must be a mapping")
    check(data.get("name") == skill.name, "Skill name must match its directory")
    description = data.get("description")
    check(isinstance(description, str) and 0 < len(description) <= 1024,
          "Missing or overlong description")
    check(set(data) <= {"name", "description", "metadata", "license", "allowed-tools"},
          "Unexpected frontmatter fields")
    ui = yaml.safe_load((skill / "agents/openai.yaml").read_text(encoding="utf-8"))
    check("$interview-review" in ui["interface"]["default_prompt"],
          "UI prompt must identify the skill")
    check(25 <= len(ui["interface"]["short_description"]) <= 64,
          "UI description must be 25–64 characters")
    required = ["README.md", "LICENSE", "CONTRIBUTING.md", "docs/evaluation.md",
                "examples/walkthrough.md", "skills/interview-review/references/maintenance.md"]
    for name in required:
        check((ROOT / name).is_file(), f"Missing {name}")
    count = 0
    for path in ROOT.rglob("*.md"):
        if any(part in {".git", ".venv"} for part in path.relative_to(ROOT).parts):
            continue
        body = path.read_text(encoding="utf-8")
        check("[TODO:" not in body, f"Unfinished scaffold: {path.relative_to(ROOT)}")
        check("/Users/" not in body and "C:\\Users\\" not in body,
              f"Personal home path: {path.relative_to(ROOT)}")
        # This repository uses inline links with simple destinations, not reference links.
        for raw in re.findall(r"\]\(([^\s)]+)\)", body):
            target = urlsplit(raw)
            if target.scheme or target.netloc or not target.path:
                continue
            dest = (path.parent / unquote(target.path)).resolve()
            check(dest.is_relative_to(ROOT), f"Link leaves repository: {raw}")
            check(dest.exists(), f"Broken local link in {path.relative_to(ROOT)}: {raw}")
            count += 1
    print(f"PASS: skill metadata, required files, and {count} local links")
    print("Behavioral quality and remote URLs are not checked.")


if __name__ == "__main__":
    main()
