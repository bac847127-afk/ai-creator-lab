"""Content structure agent for injected trends."""

from __future__ import annotations

import json
from typing import Any


def _build_structure(trend: dict[str, Any]) -> dict[str, Any]:
    title = trend["title"]
    return {
        "trend": title,
        "category": trend["category"],
        "viral_score": trend["viral_score"],
        "why_it_works": trend["why_it_works"],
        "hook": f"我把「{title}」跑了一遍，结果比想象中更像一条内容生产线。",
        "content_flow": [
            "先用一句反差说明这个趋势解决了什么问题",
            "展示输入、AI处理、输出结果三个画面",
            "拆解它为什么能提升创作者效率",
            "给出一个普通人今天就能复制的小动作",
        ],
        "pacing": "0-5秒抛出结果，5-20秒展示过程，20-45秒拆解价值，45-60秒给出行动建议。",
        "visual_style": "屏幕录制、真人口播、结果对比三段切换；字幕用短句和关键词高亮。",
    }


def run(trends: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Convert injected trend objects into content structure breakdowns."""
    return [_build_structure(trend) for trend in trends]


if __name__ == "__main__":
    try:
        from intelligence.injection.trend_injector import inject_trends
    except ModuleNotFoundError:
        import sys
        from pathlib import Path

        sys.path.append(str(Path(__file__).resolve().parents[1]))
        from intelligence.injection.trend_injector import inject_trends

    sample_trends = inject_trends(["AI自动生成视频", "Codex写完整项目", "HyperFrames自动剪辑"])
    print(json.dumps(run(sample_trends), ensure_ascii=False, indent=2))
