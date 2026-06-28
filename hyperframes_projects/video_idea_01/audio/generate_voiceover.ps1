param(
 [string]$ScriptPath = (Join-Path $PSScriptRoot "voiceover_script.txt"),
 [string]$OutputPath = (Join-Path $PSScriptRoot "voiceover.wav")
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $ScriptPath -PathType Leaf)) {
 throw "Missing voiceover script: $ScriptPath"
}

try {
 Add-Type -AssemblyName System.Speech
} catch {
 throw "System.Speech is unavailable. Run with Windows PowerShell 5.1: powershell.exe -ExecutionPolicy Bypass -File .\audio\generate_voiceover.ps1"
}

$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$voices = $synth.GetInstalledVoices()
$voiceName = $null

foreach ($installedVoice in $voices) {
 $info = $installedVoice.VoiceInfo
 $culture = $info.Culture.Name
 $name = $info.Name
 if ($culture.StartsWith("zh") -or $culture.StartsWith("cmn") -or $name.Contains("Chinese") -or $name.Contains("Huihui") -or $name.Contains("Kangkang") -or $name.Contains("Yaoyao") -or $name.Contains("Hanhan") -or $name.Contains("Xiaoxiao") -or $name.Contains("Yunxi") -or $name.Contains("Yunjian") -or $name.Contains("Xiaoyi")) {
 $voiceName = $name
 break
 }
}

if (-not $voiceName) {
 Write-Host "No Chinese speech voice was found. Installed voices:"
 foreach ($installedVoice in $voices) {
 $info = $installedVoice.VoiceInfo
 Write-Host ("- " + $info.Name + " | " + $info.Culture.Name + " | " + $info.Gender)
 }
 throw "Install a Chinese Windows speech voice, then rerun this script."
}

$rawLines = Get-Content -LiteralPath $ScriptPath -Encoding UTF8
$spokenLines = New-Object System.Collections.Generic.List[string]

foreach ($line in $rawLines) {
 $text = $line.Trim()
 if ($text.Length -eq 0) { continue }
 if ($text.StartsWith("AI Creator Lab")) { continue }
 if ($text.Contains("秒：")) { continue }
 $spokenLines.Add($text)
}

$spokenText = [string]::Join(" ", $spokenLines.ToArray())
if ($spokenText.Trim().Length -eq 0) {
 throw "Voiceover script has no speakable text."
}

$synth.SelectVoice($voiceName)
$synth.Rate = 3
$synth.Volume = 100
$synth.SetOutputToWaveFile($OutputPath)
$synth.Speak($spokenText)
$synth.Dispose()

if (-not (Test-Path -LiteralPath $OutputPath -PathType Leaf)) {
 throw "Voiceover generation finished, but output file was not found: $OutputPath"
}

Write-Host "Voiceover generated: $OutputPath"
