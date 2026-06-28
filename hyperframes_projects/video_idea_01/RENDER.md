# Render Guide

This project currently renders a clean silent MP4 from HyperFrames. Final publishing audio should be added in a post-processing pass after voiceover and BGM are ready.

## Silent publish render

```bash
cd hyperframes_projects/video_idea_01
npx hyperframes render --quality high --output renders/video_idea_01_16x9_publish_v2.mp4
```

## Audio merge plan

Expected files:

- `audio/voiceover.wav`: final 60s narration
- `audio/bgm.mp3`: low-volume tech BGM

Merge voiceover and BGM into the silent render:

```bash
ffmpeg -y \
  -i renders/video_idea_01_16x9_publish_v2.mp4 \
  -i audio/voiceover.wav \
  -i audio/bgm.mp3 \
  -filter_complex "[2:a]volume=0.18[bgm];[1:a][bgm]amix=inputs=2:duration=first:dropout_transition=0[a]" \
  -map 0:v -map "[a]" \
  -c:v copy -c:a aac -shortest \
  renders/final_with_audio.mp4
```

## Validate after audio merge

```bash
ffprobe -v error -show_entries format=duration,size -of default=noprint_wrappers=1 renders/final_with_audio.mp4
```
