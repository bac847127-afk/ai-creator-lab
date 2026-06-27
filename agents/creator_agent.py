"""Creator agent for viral short video scripts."""

from __future__ import annotations

import json
from typing import Any


def _build_script(structure: dict[str, Any], index: int) -> dict[str, Any]:
    title = structure["trend"]
    return {
        "title": f"{index}. {title}：60秒可拍短视频脚本",
        "source_trend": title,
        "viral_score": structure["viral_score"],
        "duration_seconds": 60,
        "shots": [
            {
                "time": "0-5秒",
                "visual": "正对镜头，屏幕上放大趋势标题",
                "line": structure["hook"],
            },
            {
                "time": "5-20秒",
                "visual": "录屏展示输入内容和AI开始处理",
                "line": f"我先输入一个真实需求：{title}，看它能不能直接产出结果。",
            },
            {
                "time": "20-45秒",
                "visual": "切到结果页、项目页或视频成片前后对比",
                "line": structure["why_it_works"],
            },
            {
                "time": "45-60秒",
                "visual": "回到真人口播，旁边列出3个步骤",
                "line": "你可以照着做：先给趋势，再让AI拆结构，最后生成可拍脚本。",
            },
        ],
        "shooting_notes": "竖屏拍摄，真人口播占三分之一画面，录屏结果占三分之二画面。",
    }


def run(structures: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Create shootable scripts only for trends with viral_score >= 7."""
    selected = [structure for structure in structures if structure["viral_score"] >= 7][:3]
    return [_build_script(structure, index) for index, structure in enumerate(selected, start=1)]


if __name__ == "__main__":
    try:
        from agents.structure_agent import run as run_structures
        from intelligence.injection.trend_injector import inject_trends
    except ModuleNotFoundError:
        import sys
        from pathlib import Path

        sys.path.append(str(Path(__file__).resolve().parents[1]))
        from agents.structure_agent import run as run_structures
        from intelligence.injection.trend_injector import inject_trends

    sample_trends = inject_trends(["AI自动生成视频", "Codex写完整项目", "HyperFrames自动剪辑"])
    print(json.dumps(run(run_structures(sample_trends)), ensure_ascii=False, indent=2))
