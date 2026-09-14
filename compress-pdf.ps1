<#
.SYNOPSIS
    Compresses a PDF using Ghostscript by downsampling embedded images.

.DESCRIPTION
    Wraps gswin64c -sDEVICE=pdfwrite to shrink a PDF's file size. Checks that
    Ghostscript is installed first and gives download/install instructions if not.

.PARAMETER InputPath
    Path to the source PDF.

.PARAMETER OutputPath
    Path to write the compressed PDF to. Defaults to "<input>-compressed.pdf"
    next to the input file.

.PARAMETER Resolution
    DPI to downsample color/gray/mono images to. Default 300.

.PARAMETER CompatibilityLevel
    PDF compatibility level passed to Ghostscript. Default 1.5.

.EXAMPLE
    .\compress-pdf.ps1 -InputPath .\input.pdf

.EXAMPLE
    .\compress-pdf.ps1 -InputPath .\input.pdf -OutputPath .\output.pdf -Resolution 150
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$InputPath,

    [Parameter(Position = 1)]
    [string]$OutputPath,

    [int]$Resolution = 300,

    [string]$CompatibilityLevel = '1.5'
)

$ErrorActionPreference = 'Stop'

function Find-Ghostscript {
    # gswin64c = 64-bit console exe, gswin32c = 32-bit console exe.
    foreach ($name in @('gswin64c', 'gswin32c')) {
        $cmd = Get-Command $name -ErrorAction SilentlyContinue
        if ($cmd) {
            return $cmd.Source
        }
    }
    return $null
}

function Show-InstallInstructions {
    Write-Host ''
    Write-Host 'Ghostscript was not found on this system.' -ForegroundColor Yellow
    Write-Host ''
    Write-Host 'To install it, choose one of the following:' -ForegroundColor Yellow
    Write-Host ''
    Write-Host '  Option 1 - Chocolatey (recommended):' -ForegroundColor Cyan
    Write-Host '    choco install ghostscript -y'
    Write-Host ''
    Write-Host '  Option 2 - Manual download:' -ForegroundColor Cyan
    Write-Host '    https://ghostscript.com/releases/gsdnld.html'
    Write-Host '    Download and run the Windows installer, then restart PowerShell.'
    Write-Host ''
    Write-Host 'After installing, run this script again.' -ForegroundColor Yellow
    Write-Host ''
}

# --- Locate Ghostscript ---
$gsPath = Find-Ghostscript
if (-not $gsPath) {
    Show-InstallInstructions
    exit 1
}

Write-Host "Using Ghostscript: $gsPath" -ForegroundColor DarkGray

# --- Validate input ---
if (-not (Test-Path -LiteralPath $InputPath -PathType Leaf)) {
    Write-Host "Input file not found: $InputPath" -ForegroundColor Red
    exit 1
}

$resolvedInput = (Resolve-Path -LiteralPath $InputPath).Path

if (-not $OutputPath) {
    $dir = Split-Path -Parent $resolvedInput
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($resolvedInput)
    $OutputPath = Join-Path $dir "$baseName-compressed.pdf"
}

if ((Resolve-Path -LiteralPath (Split-Path -Parent $OutputPath) -ErrorAction SilentlyContinue).Path -eq (Split-Path -Parent $resolvedInput) -and
    [System.IO.Path]::GetFileName($OutputPath) -eq [System.IO.Path]::GetFileName($resolvedInput)) {
    Write-Host 'Output path must be different from the input path.' -ForegroundColor Red
    exit 1
}

if (Test-Path -LiteralPath $OutputPath) {
    $answer = Read-Host "Output file '$OutputPath' already exists. Overwrite? (y/N)"
    if ($answer -notmatch '^[Yy]') {
        Write-Host 'Cancelled.' -ForegroundColor Yellow
        exit 0
    }
}

# --- Run Ghostscript ---
$gsArgs = @(
    '-sDEVICE=pdfwrite'
    "-dCompatibilityLevel=$CompatibilityLevel"
    '-dDownsampleColorImages=true'
    "-dColorImageResolution=$Resolution"
    '-dDownsampleGrayImages=true'
    "-dGrayImageResolution=$Resolution"
    '-dDownsampleMonoImages=true'
    "-dMonoImageResolution=$Resolution"
    '-dNOPAUSE'
    '-dBATCH'
    "-o$OutputPath"
    $resolvedInput
)

Write-Host "Compressing '$resolvedInput' -> '$OutputPath' (target ${Resolution} DPI)..." -ForegroundColor Cyan

& $gsPath @gsArgs
$exitCode = $LASTEXITCODE

if ($exitCode -ne 0) {
    Write-Host "Ghostscript exited with code $exitCode." -ForegroundColor Red
    exit $exitCode
}

if (-not (Test-Path -LiteralPath $OutputPath)) {
    Write-Host 'Ghostscript reported success but no output file was found.' -ForegroundColor Red
    exit 1
}

# --- Report results ---
$inputSize = (Get-Item -LiteralPath $resolvedInput).Length
$outputSize = (Get-Item -LiteralPath $OutputPath).Length
$savedPct = if ($inputSize -gt 0) { [math]::Round((1 - ($outputSize / $inputSize)) * 100, 1) } else { 0 }

function Format-Size([long]$bytes) {
    if ($bytes -ge 1MB) { return '{0:N2} MB' -f ($bytes / 1MB) }
    return '{0:N0} KB' -f ($bytes / 1KB)
}

Write-Host ''
Write-Host 'Done.' -ForegroundColor Green
Write-Host ("  Input:  {0} ({1})" -f $resolvedInput, (Format-Size $inputSize))
Write-Host ("  Output: {0} ({1})" -f $OutputPath, (Format-Size $outputSize))
Write-Host ("  Saved:  {0}%" -f $savedPct)
