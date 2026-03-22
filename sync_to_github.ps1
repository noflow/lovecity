# LoveCity — Sync script for GitHub Desktop
# Run this from PowerShell INSIDE your repo folder:
#   C:\Users\bradj\OneDrive\Life As\LoveCity\lovecity
#
# Usage:
#   cd "C:\Users\bradj\OneDrive\Life As\LoveCity\lovecity"
#   .\sync_to_github.ps1

$repoRoot = "C:\Users\bradj\OneDrive\Life As\LoveCity\lovecity"
$zipPath  = "$env:USERPROFILE\Downloads\lovecity_renpy.zip"
$tempDir  = "$env:TEMP\lovecity_sync"

Write-Host ""
Write-Host "╔══════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║   LoveCity — GitHub Desktop Sync Tool   ║" -ForegroundColor Cyan
Write-Host "╚══════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check zip exists
if (-not (Test-Path $zipPath)) {
    Write-Host "ERROR: Could not find lovecity_renpy.zip in Downloads." -ForegroundColor Red
    Write-Host "       Download it from Claude first, then re-run this script." -ForegroundColor Red
    exit 1
}

# Check repo exists
if (-not (Test-Path "$repoRoot\.git")) {
    Write-Host "ERROR: No git repo found at:" -ForegroundColor Red
    Write-Host "       $repoRoot" -ForegroundColor Red
    Write-Host "       Make sure GitHub Desktop has cloned the repo first." -ForegroundColor Red
    exit 1
}

Write-Host "✓ Found zip:  $zipPath" -ForegroundColor Green
Write-Host "✓ Found repo: $repoRoot" -ForegroundColor Green
Write-Host ""

# Extract zip to temp
Write-Host "Extracting zip..." -ForegroundColor Yellow
if (Test-Path $tempDir) { Remove-Item $tempDir -Recurse -Force }
Expand-Archive -Path $zipPath -DestinationPath $tempDir
$extractedRoot = Get-ChildItem $tempDir | Select-Object -First 1 -ExpandProperty FullName
Write-Host "✓ Extracted to: $extractedRoot" -ForegroundColor Green

# Files to copy (relative to both roots)
$filesToSync = @(
    ".gitignore",
    "README.md",
    "game\options.rpy",
    "game\variables.rpy",
    "game\characters.rpy",
    "game\locations.rpy",
    "game\screens.rpy",
    "game\map_screen.rpy",
    "game\location_hub.rpy",
    "game\sandbox.rpy",
    "game\bg_colors.rpy",
    "game\gui.rpy",
    "game\backgrounds\bedroom.webp",
    "game\story\intro.rpy",
    "game\story\alex.rpy",
    "game\story\dr_rivera.rpy",
    "game\story\maya_kai.rpy",
    "game\story\luna.rpy"
)

Write-Host ""
Write-Host "Copying files to repo..." -ForegroundColor Yellow
$copied = 0
foreach ($file in $filesToSync) {
    $src  = Join-Path $extractedRoot $file
    $dest = Join-Path $repoRoot $file

    if (Test-Path $src) {
        $destDir = Split-Path $dest -Parent
        if (-not (Test-Path $destDir)) {
            New-Item -ItemType Directory -Path $destDir -Force | Out-Null
        }
        Copy-Item -Path $src -Destination $dest -Force
        Write-Host "  ✓ $file" -ForegroundColor Green
        $copied++
    } else {
        Write-Host "  - $file (not in zip, skipping)" -ForegroundColor DarkGray
    }
}

Write-Host ""
Write-Host "Copied $copied files." -ForegroundColor Cyan

# Git commit
Write-Host ""
Write-Host "Committing to git..." -ForegroundColor Yellow
Set-Location $repoRoot

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
$msg = "Sync from Claude session — $timestamp"

git add -A
git status --short
git commit -m $msg

Write-Host ""
Write-Host "╔══════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║   Done! Now push in GitHub Desktop:     ║" -ForegroundColor Green
Write-Host "║   Repository → Push origin  (Ctrl+P)   ║" -ForegroundColor Green  
Write-Host "╚══════════════════════════════════════════╝" -ForegroundColor Green
Write-Host ""

# Cleanup temp
Remove-Item $tempDir -Recurse -Force
