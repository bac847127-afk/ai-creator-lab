"""Mock trend discovery agent."""

from __future__ import annotations

import json


def run() -> list[dict[str, str]]:
    """Return a fixed list of AI creator trends."""
    return [
        {
            "id": "trend_001",
            "title": "AI视频生成爆发",
            "summary": "AI video tools are moving from demos into repeatable creator workflows.",
        },
        {
            "id": "trend_002",
            "title": "Codex自动写代码",
            "summary": "Coding agents are becoming a visible part of product building and tutorial content.",
        },
        {
            "id": "trend_003",
            "title": "HyperFrames自动视频化",
            "summary": "Structured prompts and templates are turning written ideas into video drafts faster.",
        },
        {
            "id": "trend_004",
            "title": "AI工作流自动化",
            "summary": "Creators are connecting research, scripting, editing, and publishing into one pipeline.",
        },
        {
            "id": "trend_005",
            "title": "AI博主开始工业化",
            "summary": "Individual creators are adopting production systems that look like small media factories.",
        },
    ]


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
