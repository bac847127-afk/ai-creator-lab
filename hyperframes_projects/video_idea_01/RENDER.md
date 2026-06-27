# Render 使用说明

先完成 preview 检查，再渲染最终视频。

## 草稿渲染

```bash
cd hyperframes_projects/video_idea_01
npx hyperframes render --quality draft --output renders/video_idea_01_draft.mp4
```

## 最终渲染

```bash
cd hyperframes_projects/video_idea_01
npx hyperframes render --quality high --output renders/video_idea_01.mp4
```

渲染完成后检查 `renders/video_idea_01.mp4` 是否存在且文件大小正常。
