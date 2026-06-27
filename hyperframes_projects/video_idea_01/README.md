# AI自动生成视频 HyperFrames Project

这是基于 `outputs/video_packages/video_idea_01/` 生成的第一条 HyperFrames 竖屏短视频工程。

## Composition

- 文件：`index.html`
- Composition ID：`video_idea_01`
- 分辨率：`1080x1920`
- 比例：`9:16`
- 时长：`60s`
- FPS：`30`
- 风格：AI知识博主、科技感、快节奏、大字动态字幕

## 内容结构

- `0-3秒`：开头钩子
- `3-10秒`：问题展示
- `10-25秒`：AI操作演示
- `25-45秒`：结果对比
- `45-60秒`：结尾引导

## Preview

```bash
cd hyperframes_projects/video_idea_01
npx hyperframes preview --port 3017
```

打开 Studio：

```text
http://localhost:3017/#project/video_idea_01
```

## Render

预览确认后再渲染：

```bash
cd hyperframes_projects/video_idea_01
npx hyperframes render --quality high --output renders/video_idea_01.mp4
```

快速草稿：

```bash
cd hyperframes_projects/video_idea_01
npx hyperframes render --quality draft --output renders/video_idea_01_draft.mp4
```

## Validate

```bash
cd hyperframes_projects/video_idea_01
npx hyperframes lint
npx hyperframes validate
npx hyperframes inspect
```
