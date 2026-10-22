#!/usr/bin/env python3
import os
import subprocess
import sys

ROOT = "/workspace"

REQUIRED = [
    "README.md",
    "AGENT.md",
    "TODO.md",
    "docs/00-MAP.md",
    "docs/STATE.md",
    "docs/01-ROADMAP.md",
    "docs/02-VISION.md",
    "docs/03-BRAND.md",
    "docs/04-PRODUCT.md",
    "docs/05-BUSINESS.md",
    "docs/06-GTM.md",
    "docs/07-LEARNING.md",
    "library/skills/doublecheck-copilot/SKILL.md",
    "library/templates/bp-outline.md",
    "library/templates/one-pager.md",
    "library/scripts/snapshot.sh",
    "library/scripts/check_html.py",
    "library/references/startup-reading-list.md",
    "library/plugins/README.md",
]

MARKERS = {
    "docs/00-MAP.md": ["决策记录", "血的教训"],
    "docs/02-VISION.md": ["L0", "L4", "交接协议"],
    "docs/03-BRAND.md": ["44.5", "25.5", "两只眼睛"],
    "docs/05-BUSINESS.md": ["129", "399"],
    "docs/06-GTM.md": ["奇绩", "2026-12-12"],
}


def main():
    problems = []
    for rel in REQUIRED:
        p = os.path.join(ROOT, rel)
        if not os.path.isfile(p):
            problems.append(f"missing: {rel}")
            continue
        if os.path.getsize(p) == 0:
            problems.append(f"empty: {rel}")

    for rel, keys in MARKERS.items():
        p = os.path.join(ROOT, rel)
        if not os.path.isfile(p):
            continue
        text = open(p, encoding="utf-8").read()
        for k in keys:
            if k not in text:
                problems.append(f"{rel} 缺少关键内容: {k}")

    docs_git = os.path.join(ROOT, "docs", ".git")
    if not os.path.isdir(docs_git):
        problems.append("docs/ 不是独立 git 仓库")

    snaps = [f for f in os.listdir(os.path.join(ROOT, ".local-backups"))
             if f.endswith(".tar.gz")] if os.path.isdir(os.path.join(ROOT, ".local-backups")) else []
    if len(snaps) == 0:
        problems.append("没有任何快照")

    print(f"files: {sum(1 for r in REQUIRED if os.path.isfile(os.path.join(ROOT, r)))}/{len(REQUIRED)}")
    print(f"snapshots: {len(snaps)}")
    if problems:
        print("PROBLEMS:")
        for p in problems:
            print("  -", p)
        return 1
    print("OK: 结构和关键内容完整")
    return 0


if __name__ == "__main__":
    sys.exit(main())
