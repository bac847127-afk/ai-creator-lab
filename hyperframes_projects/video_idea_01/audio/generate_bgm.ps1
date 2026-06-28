param(
 [string]$OutputPath = (Join-Path $PSScriptRoot "bgm.mp3"),
 [string]$FfmpegPath = "C:\Users\xc\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.2-full_build\bin\ffmpeg.exe"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $FfmpegPath -PathType Leaf)) {
 throw "Missing ffmpeg at: $FfmpegPath"
}

$outputDir = Split-Path -Parent $OutputPath
if (-not (Test-Path -LiteralPath $outputDir -PathType Container)) {
 $null = New-Item -ItemType Directory -Path $outputDir -Force
}

$filter = "[0:a]volume=0.055[a0];[1:a]volume=0.035,tremolo=f=0.35:d=0.45[a1];[2:a]volume=0.020,lowpass=f=2200,highpass=f=180[a2];[a0][a1][a2]amix=inputs=3:duration=longest,afade=t=in:st=0:d=1.2,afade=t=out:st=58:d=2,alimiter=limit=0.45[a]"

$arguments = @(
 "-y",
 "-f", "lavfi", "-i", "sine=frequency=110:duration=60:sample_rate=48000",
 "-f", "lavfi", "-i", "sine=frequency=220:duration=60:sample_rate=48000",
 "-f", "lavfi", "-i", "anoisesrc=color=pink:duration=60:sample_rate=48000:amplitude=0.08",
 "-filter_complex", $filter,
 "-map", "[a]",
 "-t", "60",
 "-c:a", "libmp3lame",
 "-b:a", "160k",
 $OutputPath
)

$process = Start-Process -FilePath $FfmpegPath -ArgumentList $arguments -NoNewWindow -Wait -PassThru
if ($process.ExitCode -ne 0) {
 throw "ffmpeg BGM generation failed with exit code: $($process.ExitCode)"
}

if (-not (Test-Path -LiteralPath $OutputPath -PathType Leaf)) {
 throw "BGM generation finished, but output file was not found: $OutputPath"
}

Write-Host "BGM generated: $OutputPath"
