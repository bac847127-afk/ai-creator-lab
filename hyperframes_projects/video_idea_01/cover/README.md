# Cover Export README

This folder contains the horizontal cover assets for video_idea_01. It does not modify the video project, index.html, or any rendered video file.

## Current Official Cover

- cover_v2.png: official fixed cover with safe Chinese text rendering.
- cover.html: source file for cover_v2.png. It uses UTF-8 meta and HTML numeric entities for visible Chinese text.
- cover_v1.png: deprecated because Chinese text rendered as mojibake, question marks, or replacement glyphs in some environments.

## Files

- cover.html: 1920x1080 cover source, built with local HTML, CSS, and SVG only.
- export_cover.ps1: exports the cover through local Edge or Chrome.
- cover_v2.png: official cover image.

## Open The Cover

Open this file in a browser:

hyperframes_projects/video_idea_01/cover/cover.html

Use a 1920x1080 viewport when checking or exporting.

## Export The Cover

Run from hyperframes_projects/video_idea_01:

powershell -ExecutionPolicy Bypass -File .\cover\export_cover.ps1

Default output:

cover/cover_v2.png

If the script cannot find Edge or Chrome, open cover.html manually, set the viewport to 1920x1080, and save the screenshot as cover/cover_v2.png.

## Recommended Platforms

- Bilibili horizontal video
- YouTube thumbnail
- WeChat Channels horizontal video
- Douyin horizontal knowledge video

## Replace Cover Copy

Edit these visible text areas in cover.html:

- Main title line 1: Chinese text for no editing needed
- Main title line 2: Chinese text for AI auto video generation
- Subtitle: trend to script to video project to MP4
- Right workflow nodes: Trend Input, Structure Agent, Script Package, HyperFrames, Final MP4
- Bottom tags: AI workflow, 60-second demo, Codex + HyperFrames

To avoid Chinese mojibake, keep UTF-8 encoding or continue using HTML numeric entities for Chinese text.
