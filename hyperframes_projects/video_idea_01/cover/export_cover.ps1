param(
 [string]$CoverPath = (Join-Path $PSScriptRoot "cover.html"),
 [string]$OutputPath = (Join-Path $PSScriptRoot "cover_v2.png")
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path -LiteralPath $CoverPath -PathType Leaf)) {
 throw "Missing cover HTML: $CoverPath"
}

$browserCandidates = New-Object System.Collections.Generic.List[string]
$programFiles = $env:ProgramFiles
$programFilesX86 = ${env:ProgramFiles(x86)}

if ($programFiles) {
 $browserCandidates.Add((Join-Path $programFiles "Microsoft\Edge\Application\msedge.exe"))
 $browserCandidates.Add((Join-Path $programFiles "Google\Chrome\Application\chrome.exe"))
}

if ($programFilesX86) {
 $browserCandidates.Add((Join-Path $programFilesX86 "Microsoft\Edge\Application\msedge.exe"))
 $browserCandidates.Add((Join-Path $programFilesX86 "Google\Chrome\Application\chrome.exe"))
}

$browserPath = $null
foreach ($candidate in $browserCandidates) {
 if (Test-Path -LiteralPath $candidate -PathType Leaf) {
 $browserPath = $candidate
 break
 }
}

if (-not $browserPath) {
 Write-Host "No local Edge or Chrome executable was found."
 Write-Host "Manual export: open cover/cover.html in a browser, set viewport to 1920x1080, then save a screenshot as cover/cover_v2.png."
 exit 1
}

$resolvedCover = Resolve-Path -LiteralPath $CoverPath
$coverUri = (New-Object System.Uri($resolvedCover.Path)).AbsoluteUri
$resolvedOutput = [System.IO.Path]::GetFullPath($OutputPath)

if (Test-Path -LiteralPath $resolvedOutput -PathType Leaf) {
 Remove-Item -LiteralPath $resolvedOutput -Force
}

$args = @(
 "--headless=new",
 "--disable-gpu",
 "--hide-scrollbars",
 "--window-size=1920,1080",
 "--screenshot=$resolvedOutput",
 $coverUri
)

$process = Start-Process -FilePath $browserPath -ArgumentList $args -Wait -PassThru -NoNewWindow

if ($process.ExitCode -ne 0) {
 Write-Host "Browser screenshot failed with exit code: $($process.ExitCode)"
 Write-Host "Manual export: open cover/cover.html in a browser, set viewport to 1920x1080, then save a screenshot as cover/cover_v2.png."
 exit $process.ExitCode
}

if (-not (Test-Path -LiteralPath $resolvedOutput -PathType Leaf)) {
 Write-Host "Browser finished, but cover PNG was not created."
 Write-Host "Manual export: open cover/cover.html in a browser, set viewport to 1920x1080, then save a screenshot as cover/cover_v2.png."
 exit 1
}

Write-Host "Cover exported: $resolvedOutput"
