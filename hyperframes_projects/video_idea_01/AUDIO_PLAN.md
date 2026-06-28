# Audio Plan - video_idea_01 Publish V1

## Voiceover Script

0-3s: 不用剪辑，一套流程自动生成视频。趋势进来，脚本、视频工程和 MP4 直接出来。

3-10s: 很多人做视频慢，不是慢在创意，而是慢在流程。选题、脚本、字幕、剪辑，每一步都要重新沟通。

10-20s: 第一步，把趋势输入系统。人负责判断方向，AI 负责把趋势结构化，并给出传播分数。

20-30s: 第二步，AI 拆结构。它先生成开头钩子、内容节奏、画面逻辑和字幕规则。

30-45s: 第三步，生成脚本和视频包。这里输出的不只是文案，而是可以交给 HyperFrames 的完整生产材料。

45-60s: 最后，预览确认，再渲染成 MP4。这条线跑通以后，就能持续生产 AI 教学视频。

## BGM Style

- Style: clean tech, light future bass, low-frequency pulse
- Tempo: 95-110 BPM
- Mood: professional, confident, fast but not noisy
- Volume target: -22 LUFS under voiceover

## Sound Effects

- 0.0s: soft impact for hook title
- 3.0s: short glitch transition into pain point
- 10.0s: digital swipe for trend injection
- 20.0s: data scan sound for structure generation
- 30.0s: success chime for script/package output
- 45.0s: render start beep
- 58.0s: clean outro hit

## Replacement Workflow

1. Record or synthesize the voiceover as `audio/voiceover.wav`.
2. Add BGM as `audio/bgm.wav` and normalize it under narration.
3. Add SFX as short WAV files under `audio/sfx/`.
4. Wire audio files as direct children of the HyperFrames root and let HyperFrames own playback.
5. Re-run `npx hyperframes validate` and render again.
