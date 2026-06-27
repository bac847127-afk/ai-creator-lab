"""Generate HyperFrames-ready video production packages."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


DEFAULT_OUTPUT_DIR = Path("outputs") / "video_packages"
PACKAGE_FILES = [
    "script.md",
    "storyboard.md",
    "visual_style.md",
    "subtitle_plan.md",
    "hyperframes_prompt.md",
]


def _safe_text(value: Any, fallback: str = "") -> str:
    text = str(value).strip()
    return text or fallback


def _shot_line(script: dict[str, Any], index: int, fallback: str) -> str:
    shots = script.get("shots", [])
    if index < len(shots):
        return _safe_text(shots[index].get("line"), fallback)
    return fallback


def _build_script_md(script: dict[str, Any]) -> str:
    title = _safe_text(script.get("title"), "短视频脚本")
    source_trend = _safe_text(script.get("source_trend"), title)
    lines = [
        f"# {title}",
        "",
        f"- 来源趋势：{source_trend}",
        f"- 建议时长：30-60秒",
        f"- Viral Score：{script.get('viral_score', 'N/A')}/10",
        "",
        "## 口播脚本",
        "",
    ]

    for shot in script.get("shots", []):
        lines.extend(
            [
                f"### {shot['time']}",
                f"- 画面：{shot['visual']}",
                f"- 口播：{shot['line']}",
                "",
            ]
        )

    lines.extend(["## 拍摄备注", "", _safe_text(script.get("shooting_notes"), "竖屏快节奏拍摄。")])
    return "\n".join(lines).rstrip() + "\n"


def _build_storyboard_md(script: dict[str, Any]) -> str:
    title = _safe_text(script.get("source_trend"), "短视频")
    hook = _shot_line(script, 0, f"展示{title}的最强结果。")
    problem = _shot_line(script, 1, f"说明为什么{title}值得关注。")
    operation = _shot_line(script, 1, f"录屏演示{title}的AI操作流程。")
    comparison = _shot_line(script, 2, f"展示{title}带来的结果对比。")
    close = _shot_line(script, 3, "总结方法，并引导观众收藏和复用。")

    return "\n".join(
        [
            f"# {title} Storyboard",
            "",
            "## 时间轴",
            "",
            f"### 0-3秒：开头钩子",
            f"- 画面：趋势标题大字入场，真人快速抛出结果。",
            f"- 口播：{hook}",
            "",
            f"### 3-10秒：问题展示",
            f"- 画面：展示传统制作流程慢、步骤多、成本高。",
            f"- 口播：{problem}",
            "",
            f"### 10-25秒：AI操作演示",
            f"- 画面：录屏展示输入需求、AI处理、生成结果。",
            f"- 口播：{operation}",
            "",
            f"### 25-45秒：结果对比",
            f"- 画面：左侧旧流程，右侧AI输出，突出效率差异。",
            f"- 口播：{comparison}",
            "",
            f"### 45-60秒：结尾引导",
            f"- 画面：回到真人口播，屏幕列出三步复用方法。",
            f"- 口播：{close}",
        ]
    ) + "\n"


def _build_visual_style_md(script: dict[str, Any]) -> str:
    return "\n".join(
        [
            f"# {_safe_text(script.get('source_trend'), '短视频')} Visual Style",
            "",
            "- 画幅：9:16竖屏",
            "- 背景：科技感背景，适合AI工具和工作流演示",
            "- 字幕：大字动态字幕，关键词进场时轻微放大",
            "- 转场：快节奏转场，录屏和真人口播交替出现",
            "- 色彩：高对比色，深色背景搭配亮色重点词",
            "- 平台：适合抖音/短视频平台",
            "- 画面节奏：每3-5秒有一次画面变化，避免长时间静态画面",
        ]
    ) + "\n"


def _build_subtitle_plan_md(script: dict[str, Any]) -> str:
    source_trend = _safe_text(script.get("source_trend"), "AI趋势")
    keywords = [word for word in re.split(r"[：:，,。\s]+", source_trend) if word]
    keyword_text = "、".join(keywords[:4]) or source_trend
    return "\n".join(
        [
            f"# {source_trend} Subtitle Plan",
            "",
            "## 动态字幕规则",
            "",
            "- 关键词放大",
            "- 重点词高亮",
            "- 每句不超过14个中文字",
            "- 字幕跟随口播节奏",
            "- 强调前3秒停留",
            "",
            "## 关键词",
            "",
            f"- {keyword_text}",
            "- 自动化",
            "- 结果对比",
            "- 可复制",
        ]
    ) + "\n"


def _build_hyperframes_prompt_md(script: dict[str, Any]) -> str:
    source_trend = _safe_text(script.get("source_trend"), "AI趋势")
    title = _safe_text(script.get("title"), source_trend)
    return "\n".join(
        [
            f"# {source_trend} HyperFrames Prompt",
            "",
            "请使用 Codex + HyperFrames 根据以下制作指令生成一条 9:16 竖屏短视频。",
            "",
            "## 制作目标",
            "",
            f"- 视频主题：{title}",
            "- 时长：30-60秒",
            "- 平台：抖音/短视频平台",
            "- 风格：科技感背景、大字动态字幕、快节奏转场、高对比色",
            "",
            "## 素材与结构",
            "",
            "- 使用 script.md 作为完整口播脚本",
            "- 使用 storyboard.md 作为时间轴和镜头规划",
            "- 使用 visual_style.md 控制整体视觉风格",
            "- 使用 subtitle_plan.md 生成动态字幕",
            "",
            "## 输出要求",
            "",
            "- 前3秒必须保留强钩子字幕",
            "- 每个镜头都要有明确画面变化",
            "- 重点词放大并高亮",
            "- 结尾给出可复制行动建议",
            "- 输出适合直接发布的短视频成片方案",
        ]
    ) + "\n"


def _write_package(package_dir: Path, script: dict[str, Any]) -> Path:
    package_dir.mkdir(parents=True, exist_ok=True)
    files = {
        "script.md": _build_script_md(script),
        "storyboard.md": _build_storyboard_md(script),
        "visual_style.md": _build_visual_style_md(script),
        "subtitle_plan.md": _build_subtitle_plan_md(script),
        "hyperframes_prompt.md": _build_hyperframes_prompt_md(script),
    }
    for filename, content in files.items():
        (package_dir / filename).write_text(content, encoding="utf-8")
    return package_dir


def generate_video_packages(
    video_scripts: list[dict[str, Any]],
    output_dir: Path = DEFAULT_OUTPUT_DIR,
    limit: int = 3,
) -> list[Path]:
    """Generate one HyperFrames-ready package for each selected video script."""
    output_dir.mkdir(parents=True, exist_ok=True)
    package_paths: list[Path] = []

    for index, script in enumerate(video_scripts[:limit], start=1):
        package_dir = output_dir / f"video_idea_{index:02d}"
        package_paths.append(_write_package(package_dir, script))

    return package_paths
if __name__ == "__main__":
    import sys

    sys.path.append(str(Path(__file__).resolve().parents[1]))
    from main import run_pipeline

    paths = generate_video_packages(run_pipeline()["video_scripts"])
    for path in paths:
        print(path)
