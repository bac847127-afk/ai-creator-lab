"""Pipeline entrypoint for AI Creator Intelligence Lab."""

from __future__ import annotations

import json
from typing import Any

from agents.creator_agent import run as run_creator_agent
from agents.structure_agent import run as run_structure_agent
from intelligence.injection.trend_injector import inject_trends


INPUT_TRENDS = [
    "AI自动生成视频",
    "Codex写完整项目",
    "HyperFrames自动剪辑",
]


def run_pipeline(input_trends: list[str] | None = None) -> dict[str, Any]:
    """Run Trend Injection -> Structure -> Creator and return all stage outputs."""
    raw_trends = input_trends or INPUT_TRENDS
    trends = inject_trends(raw_trends)
    structures = run_structure_agent(trends)
    video_scripts = run_creator_agent(structures)

    return {
        "raw_trends": raw_trends,
        "trends": trends,
        "content_structures": structures,
        "video_scripts": video_scripts,
    }


if __name__ == "__main__":
    print(json.dumps(run_pipeline(), ensure_ascii=False, indent=2))
