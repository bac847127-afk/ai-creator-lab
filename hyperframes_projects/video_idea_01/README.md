# AI Workflow Teaching Video - Publish V1

This project is a 1920x1080 horizontal AI teaching sample for an AI creator workflow.

## Composition

- File: `index.html`
- Composition ID: `video_idea_01`
- Resolution: `1920x1080`
- Duration: `60s`
- Format: 16:9 horizontal
- Output target: `renders/video_idea_01_16x9_publish_v1.mp4`

## Story Timeline

- `0-3s`: Strong hook
- `3-10s`: Pain point, video production is too slow
- `10-20s`: Input trend
- `20-30s`: AI structures the content
- `30-45s`: Generate script and video package
- `45-60s`: Render MP4 and invite reuse

## Layout

- Top: chapter title only
- Left 40%: bright main title and three clear steps
- Right 60%: readable AI workflow code/data panel
- Bottom: fixed 120px voiceover subtitle bar

## Audio

This version does not synthesize final voiceover audio yet. See `AUDIO_PLAN.md` for voiceover script, BGM direction, SFX timing, and replacement workflow.

## Validate

```bash
npx hyperframes lint
npx hyperframes validate
```

## Render

```bash
npx hyperframes render --quality high --output renders/video_idea_01_16x9_publish_v1.mp4
```

## Publish Package

The publishing package for this video is located at:

- `publish_package/`

It includes platform titles, descriptions, cover prompts, publishing notes, and the template reuse guide.

Final publish-ready video:

- `renders/video_idea_01_16x9_final_normalized.mp4`
