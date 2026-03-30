# Hegardt.se tag script

# Function to write colored output
function Write-Step
{
    param(
        [string]$Message,
        [string]$Color = "Cyan"
    )
    Write-Host $Message -ForegroundColor $Color
}

function Write-Success
{
    param([string]$Message)
    Write-Host "✅ $Message" -ForegroundColor Green
}

function Write-Error
{
    param([string]$Message)
    Write-Host "❌ $Message" -ForegroundColor Red
}

function Write-Box
{
    param(
        [string]$Step,
        [string]$Message,
        [string]$Extra = ""
    )
    Write-Host ""
    Write-Host "┌───────────────────────────────────────────────────────────────────┐" -ForegroundColor Blue
    Write-Host "Step $Step" -ForegroundColor Green -NoNewline
    Write-Host " $Message" -ForegroundColor White
    if ($Extra)
    {
        Write-Host "$Extra" -ForegroundColor Yellow
    }
    Write-Host "└───────────────────────────────────────────────────────────────────┘" -ForegroundColor Blue
}
# Get the latest tag matching v*.*.* pattern
git fetch --tags
$latestTag = git tag |
    Where-Object { $_ -match '^v(\d+)\.(\d+)\.(\d+)$' } |
    Sort-Object {
        $parts = ($_ -replace '^v', '') -split '\.'
        [int]$parts[0] * 1000000 + [int]$parts[1] * 1000 + [int]$parts[2]
    } |
    Select-Object -Last 1

# Calculate suggested version
if (-not $latestTag)
{
    # No existing tags, start with v0.1.0
    $suggestedVersion = "0.1.0"
}
else
{
    # Extract version numbers (remove 'v' prefix)
    $version = $latestTag -replace '^v', ''

    # Split into major.minor.patch
    $parts = $version -split '\.'
    $major = [int]$parts[0]
    $minor = [int]$parts[1]
    $patch = [int]$parts[2]

    # Bump patch version
    $patch++

    $suggestedVersion = "$major.$minor.$patch"
}

# Prompt for version
Write-Host "Latest tag: " -NoNewline -ForegroundColor Yellow
if ($latestTag)
{
    Write-Host $latestTag -ForegroundColor White
}
else
{
    Write-Host "(none)" -ForegroundColor Gray
}
Write-Host "Suggested version: " -NoNewline -ForegroundColor Cyan
Write-Host "v$suggestedVersion" -ForegroundColor White
Write-Host ""
Write-Host "Enter version (without 'v' prefix) or press Enter to use suggested: " -NoNewline -ForegroundColor Yellow
$userInput = Read-Host

# Determine final version
if ( [string]::IsNullOrWhiteSpace($userInput))
{
    $newVersion = $suggestedVersion
    Write-Host "Using suggested version: v$newVersion" -ForegroundColor Cyan
}
else
{
    $newVersion = $userInput -replace '^v', ''
    Write-Host "Using provided version: v$newVersion" -ForegroundColor Cyan
}

# Create the tag with 'v' prefix
$tagName = "v$newVersion"

Write-Host ""
Write-Host "Creating annotated tag: $tagName" -ForegroundColor Yellow
git tag -a $tagName -m "Release $tagName"

if ($LASTEXITCODE -ne 0)
{
    Write-Error "Failed to create tag!"
    exit 1
}

Write-Success "Created tag $tagName"

# Step 6: Push tag to remote
Write-Box "Pushing tag to remote..."
git push origin $tagName
if ($LASTEXITCODE -ne 0)
{
    Write-Error "Failed to push tag to remote!"
    exit 1
}
Write-Success "Tag pushed to remote successfully"

Read-Host "Press Enter to exit"