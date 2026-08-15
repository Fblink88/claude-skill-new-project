#!/usr/bin/env python3
"""PreToolUse hook: blocks Edit/Write to this repo's SKILL.md if the resulting
frontmatter would violate the Agent Skills open standard (agentskills.io):
description <= 1024 chars, name lowercase/digits/hyphens <= 64 chars with no
reserved words."""
import json
import os
import re
import sys

# Repo root = two levels up from .claude/hooks/ — resuelto por ubicación del
# script, no hardcodeado, para no filtrar la ruta/usuario local en el repo público.
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TARGET = os.path.join(REPO_ROOT, "SKILL.md")
MAX_DESC = 1024
NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
RESERVED = ("anthropic", "claude")


def get_frontmatter(content):
    if not content.startswith("---"):
        return None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None
    return parts[1]


def extract_field(frontmatter, field):
    lines = frontmatter.splitlines()
    value_lines = []
    capturing = False
    for line in lines:
        m = re.match(rf"^{field}:\s?(.*)$", line)
        if m:
            capturing = True
            value_lines.append(m.group(1))
            continue
        if capturing:
            if re.match(r"^[A-Za-z_-]+:", line):
                break
            if line.startswith((" ", "\t")):
                value_lines.append(line.strip())
                continue
            break
    if not value_lines:
        return None
    return " ".join(value_lines).strip().strip('"').strip("'")


def main():
    try:
        data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    tool_name = data.get("tool_name")
    tool_input = data.get("tool_input", {})
    file_path = tool_input.get("file_path", "")

    if not file_path or os.path.abspath(file_path) != TARGET:
        sys.exit(0)

    if tool_name == "Write":
        content = tool_input.get("content", "")
    elif tool_name == "Edit":
        try:
            with open(TARGET, "r") as f:
                current = f.read()
        except FileNotFoundError:
            sys.exit(0)
        old = tool_input.get("old_string", "")
        new = tool_input.get("new_string", "")
        if tool_input.get("replace_all"):
            content = current.replace(old, new)
        else:
            content = current.replace(old, new, 1)
    else:
        sys.exit(0)

    fm = get_frontmatter(content)
    if fm is None:
        print(
            "validate-skill-md: no se pudo leer el frontmatter YAML (esperado entre '---').",
            file=sys.stderr,
        )
        sys.exit(2)

    name = extract_field(fm, "name")
    description = extract_field(fm, "description")

    errors = []
    if name is None:
        errors.append("falta el campo 'name' en el frontmatter.")
    elif not NAME_RE.match(name):
        errors.append(
            f"'name' inválido ('{name}') — debe ser minúsculas/números/guiones, máx 64 caracteres."
        )
    elif any(r in name.lower() for r in RESERVED):
        errors.append(
            f"'name' ('{name}') contiene una palabra reservada ({'/'.join(RESERVED)})."
        )

    if description is None:
        errors.append("falta el campo 'description' en el frontmatter.")
    elif len(description) > MAX_DESC:
        errors.append(
            f"'description' tiene {len(description)} caracteres, excede el máximo de {MAX_DESC} (spec Agent Skills)."
        )

    if errors:
        print("validate-skill-md: SKILL.md no cumple el spec de Agent Skills:", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
