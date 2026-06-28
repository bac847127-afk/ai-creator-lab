param(
 [string]$InputPath = (Join-Path (Split-Path -Parent $PSScriptRoot) "renders\video_idea_01_16x9_final_with_audio.mp4"),
 [string]$OutputPath = (Join-Path (Split-Path -Parent $PSScriptRoot) "renders\video_idea_01_16x9_final_normalized.mp4"),
 [string]$FfmpegPath = "C:\Users\xc\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $InputPath -PathType Leaf)) {
 throw "Missing input MP4: $InputPath"
}

if (-not (Test-Path -LiteralPath $FfmpegPath -PathType Leaf)) {
 throw "Missing ffmpeg at: $FfmpegPath"
}

$outputDir = Split-Path -Parent $OutputPath
if (-not (Test-Path -LiteralPath $outputDir -PathType Container)) {
 $null = New-Item -ItemType Directory -Path $outputDir -Force
}

$filter = "loudnorm=I=-16:TP=-1:LRA=11:measured_I=-29.1:measured_TP=-6.0:measured_LRA=4.5:measured_thresh=-39.6:offset=2.2:linear=true:print_format=summary,alimiter=limit=0.794328,volume=-1.2dB"

$arguments = @(
 "-y",
 "-i", $InputPath,
 "-map", "0:v:0",
 "-map", "0:a:0",
 "-c:v", "copy",
 "-af", $filter,
 "-c:a", "aac",
 "-b:a", "192k",
 "-ar", "48000",
 "-t", "60",
 "-movflags", "+faststart",
 $OutputPath
)

$process = Start-Process -FilePath $FfmpegPath -ArgumentList $arguments -NoNewWindow -Wait -PassThru
if ($process.ExitCode -ne 0) {
 throw "ffmpeg audio normalization failed with exit code: $($process.ExitCode)"
}

if (-not (Test-Path -LiteralPath $OutputPath -PathType Leaf)) {
 throw "Normalization finished, but output file was not found: $OutputPath"
}

Write-Host "Normalized MP4 generated: $OutputPath"
