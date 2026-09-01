<#
.SYNOPSIS
  Syncs local static_media/ (images, portraits, pdfs) to the Hegardt server
  using only ssh/scp (Windows 10's built-in OpenSSH client) - no rsync needed.

.DESCRIPTION
  Lists files already present on the server, diffs against local files, and
  uploads only what's missing - mirroring rsync's --ignore-existing behavior.
  Whole files are copied (no delta/byte-level sync), which is fine for a
  folder of static assets that rarely changes.

.PARAMETER DryRun
  Show what would be uploaded without transferring anything.

.PARAMETER Overwrite
  Upload every local file regardless of what's already on the server.

.EXAMPLE
  ./deploy-static-media.ps1

.EXAMPLE
  ./deploy-static-media.ps1 -DryRun
#>

param(
    [switch]$DryRun,
    [switch]$Overwrite
)

$ErrorActionPreference = 'Stop'

$SshPort    = 2223
$RemoteUser = 'root'
$RemoteHost = '134.209.240.67'
$RemotePath = '/root/Hegardt/static_media'
$LocalRoot  = Join-Path $PSScriptRoot 'static_media'

foreach ($cmd in 'ssh', 'scp') {
    if (-not (Get-Command $cmd -ErrorAction SilentlyContinue)) {
        Write-Error "'$cmd' not found. Enable it via Settings > Optional Features > OpenSSH Client, or 'Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0' (run as admin)."
        exit 1
    }
}

if (-not (Test-Path $LocalRoot)) {
    Write-Error "Local folder not found: $LocalRoot"
    exit 1
}

# Get remote file list (paths relative to $RemotePath) so we can diff against it
$remoteSet = [System.Collections.Generic.HashSet[string]]::new()
if (-not $Overwrite) {
    $findCmd = "find $RemotePath -type f 2>/dev/null | sed 's|^$RemotePath/||'"
    $remoteFiles = ssh -p $SshPort "${RemoteUser}@${RemoteHost}" $findCmd
    if ($LASTEXITCODE -ne 0) { throw 'Failed to list remote files over ssh.' }
    foreach ($f in $remoteFiles) { [void]$remoteSet.Add($f) }
}

$localFiles = Get-ChildItem -Path $LocalRoot -Recurse -File
$toUpload = foreach ($file in $localFiles) {
    $relative = $file.FullName.Substring($LocalRoot.Length + 1) -replace '\\', '/'
    if ($Overwrite -or -not $remoteSet.Contains($relative)) {
        [PSCustomObject]@{ Local = $file.FullName; Relative = $relative }
    }
}

if (-not $toUpload) {
    Write-Host 'Nothing new to upload.' -ForegroundColor Green
    exit 0
}

Write-Host 'Files to upload:' -ForegroundColor Cyan
$toUpload | ForEach-Object { Write-Host "  $($_.Relative)" }

if ($DryRun) {
    Write-Host '(dry run - nothing transferred)' -ForegroundColor Yellow
    exit 0
}

foreach ($item in $toUpload) {
    $relativeDir = Split-Path $item.Relative -Parent
    $remoteDir = if ($relativeDir) { "$RemotePath/$relativeDir" } else { $RemotePath }
    $remoteDir = $remoteDir -replace '\\', '/'

    ssh -p $SshPort "${RemoteUser}@${RemoteHost}" "mkdir -p '$remoteDir'"
    scp -P $SshPort $item.Local "${RemoteUser}@${RemoteHost}:$remoteDir/"
}

Write-Host 'Done.' -ForegroundColor Green