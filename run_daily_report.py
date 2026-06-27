"""Generate the daily AI creator report from the trend injection pipeline."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from main import run_pipeline
from video.video_package_generator import generate_video_packages


OUTPUT_PATH = Path("outputs") / "daily_report.md"


def _format_list(items: list[str]) -> str:
    return "\n".join(f"  - {item}" for item in items)


def build_report(data: dict[str, Any]) -> str:
    """Render pipeline output as a Markdown daily report."""
    lines: list[str] = [
        "# AI Creator Daily Report",
        "",
        "## Trends",
        "",
    ]

    for index, trend in enumerate(data["trends"], start=1):
        lines.extend(
            [
                f"{index}. **{trend['title']}**",
                f"   - Category: {trend['category']}",
                f"   - Viral Score: {trend['viral_score']}/10",
            ]
        )

    lines.extend(["", "## Viral Breakdown", ""])
    for trend in data["trends"]:
        lines.extend(
            [
                f"### {trend['title']}",
                f"- 为什么会火：{trend['why_it_works']}",
                f"- 传播判断：viral_score {trend['viral_score']}/10",
                "",
            ]
        )

    lines.extend(["## Content Structures", ""])
    for structure in data["content_structures"]:
        lines.extend(
            [
                f"### {structure['trend']}",
                f"- Hook：{structure['hook']}",
                "- Content flow：",
                _format_list(structure["content_flow"]),
                f"- Pacing：{structure['pacing']}",
                f"- Visual style：{structure['visual_style']}",
                "",
            ]
        )

    lines.extend(["## Video Scripts", ""])
    for index, script in enumerate(data["video_scripts"], start=1):
        lines.extend(
            [
                f"{index}. **{script['title']}**",
                f"   - 来源趋势：{script['source_trend']}",
                f"   - 时长：≤{script['duration_seconds']}秒",
                f"   - Viral Score：{script['viral_score']}/10",
                "   - 分镜脚本：",
            ]
        )
        for shot in script["shots"]:
            lines.extend(
                [
                    f"     - {shot['time']}：{shot['visual']}",
                    f"       台词：{shot['line']}",
                ]
            )
        lines.append(f"   - 拍摄备注：{script['shooting_notes']}")

    return "\n".join(lines).rstrip() + "\n"


def generate_daily_report(path: Path = OUTPUT_PATH) -> Path:
    """Run the pipeline, write the report, and generate video packages."""
    data = run_pipeline()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(build_report(data), encoding="utf-8")
    generate_video_packages(data["video_scripts"])
    return path


if __name__ == "__main__":
    report_path = generate_daily_report()
    print(f"Daily report generated: {report_path}")
