param(
 [string]$VoiceoverPath = (Join-Path $PSScriptRoot "voiceover.wav"),
 [string]$BgmPath = (Join-Path $PSScriptRoot "bgm.mp3"),
 [string]$VideoPath = (Join-Path (Split-Path -Parent $PSScriptRoot) "renders\video_idea_01_16x9_publish_v2.mp4"),
 [string]$OutputPath = (Join-Path (Split-Path -Parent $PSScriptRoot) "renders\video_idea_01_16x9_final_with_audio.mp4")
)

$ErrorActionPreference = "Stop"

function Assert-FileExists {
 param(
 [string]$Path,
 [string]$Message
 )

 if (-not (Test-Path -LiteralPath $Path -PathType Leaf)) {
 throw $Message
 }
}

Assert-FileExists -Path $VideoPath -Message "Missing input video: $VideoPath. Render publish_v2 MP4 first."
Assert-FileExists -Path $VoiceoverPath -Message "Missing voiceover file: $VoiceoverPath. Create or record audio/voiceover.wav first."
Assert-FileExists -Path $BgmPath -Message "Missing BGM file: $BgmPath. Prepare audio/bgm.mp3 first."

$ffmpeg = Get-Command ffmpeg -ErrorAction SilentlyContinue
if (-not $ffmpeg) {
 throw "Missing ffmpeg. Install ffmpeg first and make sure it is available in PATH."
}

$outputDir = Split-Path -Parent $OutputPath
if (-not (Test-Path -LiteralPath $outputDir -PathType Container)) {
 $null = New-Item -ItemType Directory -Path $outputDir -Force
}

$filter = "[1:a]volume=1.0,atrim=0:60,apad=pad_dur=60,atrim=0:60,asetpts=PTS-STARTPTS[voice];" +
 "[2:a]volume=0.16,atrim=0:60,apad=pad_dur=60,atrim=0:60,asetpts=PTS-STARTPTS[bgm];" +
 "[voice][bgm]amix=inputs=2:duration=longest:dropout_transition=0,atrim=0:60,alimiter=limit=0.95[a]"

ffmpeg -y -i $VideoPath -i $VoiceoverPath -stream_loop -1 -i $BgmPath -filter_complex $filter -map 0:v:0 -map "[a]" -t 60 -c:v copy -c:a aac -b:a 192k $OutputPath

if ($LASTEXITCODE -ne 0) {
 throw "ffmpeg merge failed with exit code: $LASTEXITCODE"
}

if (-not (Test-Path -LiteralPath $OutputPath -PathType Leaf)) {
 throw "Merge command finished, but output file was not found: $OutputPath"
}

Write-Host "Audio merge complete: $OutputPath"
