# Template Reuse Guide

这个模板用于把 `video_idea_01` 从一次样片，扩展成可复用的 AI 教学视频生产模板。核心原则是：保留工程结构，替换内容输入，重新生成脚本、视频包、音频和最终发布文件。

## 1. 需要替换哪些文案

优先替换这些内容：

- 开头强钩子：当前是不用剪辑，一套流程自动生成视频。
- 顶部章节标题：例如输入趋势、AI拆结构、生成脚本、输出视频包、渲染MP4。
- 左侧主标题和步骤列表。
- 右侧代码或工作流面板里的示例内容。
- 底部口播字幕。
- `audio/voiceover_script.txt` 中的口播文案。
- `publish_package/` 下的平台标题、简介和封面提示词。

不要优先改动布局和动画，除非新主题确实需要不同结构。

## 2. 需要替换哪些趋势

趋势来源在 Intelligence Lab 的输入流中维护。新视频可以替换为：

- 新 AI 工具趋势
- 新内容平台趋势
- 新工作流自动化趋势
- 新 Codex 项目案例
- 新 HyperFrames 视频生成案例

建议每条视频只聚焦 1 个主趋势，最多带 2 个辅助趋势，避免 60 秒内容过散。

## 3. 如何生成新脚本

推荐流程：

1. 在主 pipeline 中输入新的 `input_trends`。
2. 通过 trend injector 生成结构化 trend object。
3. 让 structure agent 输出 hook、content flow、pacing、visual style。
4. 让 creator agent 只选择 `viral_score 的主题。
5. 生成 30-60 秒可直接拍的短视频脚本。

脚本必须保留明确时间线，例如：

- 0-3秒：强钩子
- 3-10秒：痛点或反差
- 10-20秒：输入趋势
- 20-30秒：AI拆结构
- 30-45秒：生成脚本和视频包
- 45-60秒：结果展示和关注引导

## 4. 如何生成新视频包

运行日报或视频包生成流程后，为新选题生成独立 package：

- `script.md`
- `storyboard.md`
- `visual_style.md`
- `subtitle_plan.md`
- `hyperframes_prompt.md`

建议输出到：

- `outputs/video_packages/video_idea_02/`
- `outputs/video_packages/video_idea_03/`
- `outputs/video_packages/video_idea_04/`

每个 package 应该独立，不要复用旧脚本文件名覆盖旧内容。

## 5. 如何重新渲染

复用当前 HyperFrames 模板时，推荐复制整个工程目录：

- 从 `hyperframes_projects/video_idea_01/` 复制到 `hyperframes_projects/video_idea_02/`。
- 替换新工程里的文案、字幕、代码面板内容。
- 保持分辨率 `1920x1080` 和时长 `60s`。
- 运行 lint 和 validate。
- 渲染新 MP4。

示例命令：

```powershell
npx hyperframes lint
npx hyperframes validate
npx hyperframes render --quality high --output renders/video_idea_02_16x9_publish_v1.mp4
```

## 6. 如何合成音频

每个新视频都应有独立音频目录：

- `audio/voiceover_script.txt`：新口播稿
- `audio/generate_voiceover.ps1`：生成语音
- `audio/generate_bgm.ps1`：生成临时 BGM
- `audio/audio_merge.ps1`：合成有声 MP4
- `audio/normalize_final_audio.ps1`：最终响度归一化

推荐输出链路：

1. 生成无声画面 MP4。
2. 生成 `audio/voiceover.wav`。
3. 生成 `audio/bgm.mp3`。
4. 合成 `renders/..._final_with_audio.mp4`。
5. 归一化输出 `renders/..._final_normalized.mp4`。

最终发布优先使用 normalized 版本。

## 7. 如何批量生成 video_idea_02、03、04

批量生产建议按以下方式组织：

- `video_idea_02`：换一个趋势主题，复用横屏教学结构。
- `video_idea_03`：换一个工具组合，例如 Codex + 数据分析。
- `video_idea_04`：换一个平台目标，例如 B站课程型拆解。

批量流程：

1. 一次输入 5-10 条趋势。
2. 让系统计算 viral score。
3. 只保留分数最高的 3 条。
4. 为每条生成独立 video package。
5. 复制模板工程并替换文案。
6. 分别渲染、合成音频、归一化。
7. 为每条创建独立 publish package。

建议命名：

- `hyperframes_projects/video_idea_02/`
- `hyperframes_projects/video_idea_03/`
- `hyperframes_projects/video_idea_04/`

每个工程都保留自己的 `renders/`、`audio/` 和 `publish_package/`，这样后续可以独立发布、回溯和复盘。
