# Audio Merge Workflow

本目录只负责给现有无声视频增加音频，不修改 `index.html`，也不重新设计画面。

## 1. 生成 voiceover.wav

使用 `voiceover_script.txt` 作为 60 秒中文口播稿。

可选方式：

- 手动录音，导出为 WAV。
- 使用任意 TTS 工具生成中文口播。
- 如果后续使用 HyperFrames / HeyGen 音频能力，先登录或配置对应凭证，再把生成结果保存为本目录下的 `voiceover.wav`。

要求：

- 文件路径：`audio/voiceover.wav`
- 建议时长：接近 60 秒
- 建议采样率：44.1kHz 或 48kHz
- 人声要清晰，前 3 秒钩子要有力度

## 2. 准备 bgm.mp3

准备一段适合 AI 教学视频的科技感背景音乐。

要求：

- 文件路径：`audio/bgm.mp3`
- 风格：科技感、轻节奏、干净、不抢人声
- 时长可以少于 60 秒，脚本会循环 BGM 并截取到 60 秒

合成脚本会把 BGM 音量压低到约 16%，避免盖住口播。

## 3. 运行合成脚本

在 `hyperframes_projects/video_idea_01/` 目录运行：

```powershell
powershell -ExecutionPolicy Bypass -File .\audio\audio_merge.ps1
```

脚本默认读取：

- 视频：`renders/video_idea_01_16x9_publish_v2.mp4`
- 口播：`audio/voiceover.wav`
- BGM：`audio/bgm.mp3`

如果缺少 `voiceover.wav`、`bgm.mp3` 或输入视频，脚本会直接给出明确错误提示。

## 4. 最终输出

合成完成后输出：

```text
renders/video_idea_01_16x9_final_with_audio.mp4
```

该文件会保持 60 秒时长，视频轨沿用现有画面，音频轨包含清晰口播和低音量背景音乐。
