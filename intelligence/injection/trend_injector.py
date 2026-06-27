"""Convert human trend inputs into structured trend objects."""

from __future__ import annotations

import json
from typing import Any


def _category_for(raw_trend: str) -> str:
    if "视频" in raw_trend or "剪辑" in raw_trend:
        return "AI Video"
    if "Codex" in raw_trend or "代码" in raw_trend or "项目" in raw_trend:
        return "AI Coding"
    if "工作流" in raw_trend or "自动" in raw_trend:
        return "AI Workflow"
    return "AI Creator"


def _viral_score_for(raw_trend: str) -> int:
    score = 6
    high_signal_keywords = ["自动", "生成", "完整", "视频", "项目", "剪辑", "Codex"]
    for keyword in high_signal_keywords:
        if keyword in raw_trend:
            score += 1
    return min(score, 10)


def _why_it_works(raw_trend: str, category: str, viral_score: int) -> str:
    if category == "AI Video":
        return f"{raw_trend}把复杂制作变成可见结果，适合用前后对比制造传播点。"
    if category == "AI Coding":
        return f"{raw_trend}直接展示生产力跃迁，观众能快速理解它节省了多少时间。"
    if category == "AI Workflow":
        return f"{raw_trend}把多个步骤串成系统，容易引发创作者复制和收藏。"
    if viral_score >= 8:
        return f"{raw_trend}有明确的新鲜感和实用价值，适合做成短视频验证。"
    return f"{raw_trend}有AI话题热度，但需要更强案例来放大传播。"


def inject_trends(raw_trends: list[str]) -> list[dict[str, Any]]:
    """Normalize raw human trend inputs into structured trend objects."""
    trend_objects: list[dict[str, Any]] = []

    for raw_trend in raw_trends:
        title = raw_trend.strip()
        if not title:
            continue

        category = _category_for(title)
        viral_score = _viral_score_for(title)
        trend_objects.append(
            {
                "title": title,
                "category": category,
                "why_it_works": _why_it_works(title, category, viral_score),
                "viral_score": viral_score,
            }
        )

    return trend_objects


if __name__ == "__main__":
    sample_input = [
        "AI自动生成视频",
        "Codex写完整项目",
        "HyperFrames自动剪辑",
    ]
    print(json.dumps(inject_trends(sample_input), ensure_ascii=False, indent=2))
