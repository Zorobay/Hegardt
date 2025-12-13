# Hegardt.se Deployment Script

# Function to write colored output
function Write-Step {
    param(
        [string]$Message,
        [string]$Color = "Cyan"
    )
    Write-Host $Message -ForegroundColor $Color
}

function Write-Success {
    param([string]$Message)
    Write-Host "✅ $Message" -ForegroundColor Green
}

function Write-Error {
    param([string]$Message)
    Write-Host "❌ $Message" -ForegroundColor Red
}

function Write-Box {
    param(
        [string]$Step,
        [string]$Message,
        [string]$Extra = ""
    )
    Write-Host ""
    Write-Host "┌───────────────────────────────────────────────────────────────────┐" -ForegroundColor Blue
    Write-Host "Step $Step" -ForegroundColor Green -NoNewline
    Write-Host " $Message" -ForegroundColor White
    if ($Extra) {
        Write-Host "$Extra" -ForegroundColor Yellow
    }
    Write-Host "└───────────────────────────────────────────────────────────────────┘" -ForegroundColor Blue
}

# Start deployment
$startTime = Get-Date
Clear-Host
Write-Host ""
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "                    HEGARDT.SE DEPLOYMENT SCRIPT" -ForegroundColor Cyan
Write-Host "================================================================================" -ForegroundColor Cyan
Write-Host "Started at: " -NoNewline -ForegroundColor Yellow
Write-Host $startTime.ToString("yyyy-MM-dd HH:mm:ss") -ForegroundColor White
Write-Host ""

# Step 0: Create Git tag
Write-Box "0/6:" "Creating Git tag..."

# Get the latest tag matching v*.*.* pattern
$latestTag = git describe --tags --match "v*.*.*" --abbrev=0 2>$null

# Calculate suggested version
if (-not $latestTag) {
    # No existing tags, start with v0.1.0
    $suggestedVersion = "0.1.0"
} else {
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
if ($latestTag) {
    Write-Host $latestTag -ForegroundColor White
} else {
    Write-Host "(none)" -ForegroundColor Gray
}
Write-Host "Suggested version: " -NoNewline -ForegroundColor Cyan
Write-Host "v$suggestedVersion" -ForegroundColor White
Write-Host ""
Write-Host "Enter version (without 'v' prefix) or press Enter to use suggested: " -NoNewline -ForegroundColor Yellow
$userInput = Read-Host

# Determine final version
if ([string]::IsNullOrWhiteSpace($userInput)) {
    $newVersion = $suggestedVersion
    Write-Host "Using suggested version: v$newVersion" -ForegroundColor Cyan
} else {
    $newVersion = $userInput -replace '^v', ''
    Write-Host "Using provided version: v$newVersion" -ForegroundColor Cyan
}

# Create the tag with 'v' prefix
$tagName = "v$newVersion"

Write-Host ""
Write-Host "Creating annotated tag: $tagName" -ForegroundColor Yellow
git tag -a $tagName -m "Release $tagName"

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to create tag!"
    exit 1
}

Write-Success "Created tag $tagName"

# Step 1: Install dependencies
Write-Box "1/6:" "Installing npm dependencies..."
npm i
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to install dependencies!"
    exit 1
}
Write-Success "Dependencies installed successfully"

# Step 2: Build distribution
Write-Box "2/6:" "Building distribution..."
npm run build
if ($LASTEXITCODE -ne 0) {
    Write-Error "Build failed!"
    exit 1
}
Write-Success "Build completed successfully"

# Step 3: Transfer files
Write-Box "3/6:" "Transferring dist/ to server..." "Target: root@134.209.240.67:/var/www/hegardt.se/html/"
scp -r "dist/*" root@134.209.240.67:/var/www/hegardt.se/html/
if ($LASTEXITCODE -ne 0) {
    Write-Error "File transfer failed!"
    exit 1
}
Write-Success "Files transferred successfully"

# Step 4: Set permissions
Write-Box "4/6:" "Setting file permissions..."
ssh root@134.209.240.67 "sudo chmod -R 755 /var/www/hegardt.se"
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to set permissions!"
    exit 1
}
Write-Success "Permissions set successfully"

# Step 5: Restart Nginx
Write-Box "5/6:" "Restarting Nginx..."
ssh root@134.209.240.67 "sudo systemctl restart nginx"
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to restart Nginx!"
    exit 1
}
Write-Success "Nginx restarted successfully"

# Step 6: Push tag to remote
Write-Box "6/6:" "Pushing tag to remote..."
git push origin $tagName
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to push tag to remote!"
    exit 1
}
Write-Success "Tag pushed to remote successfully"

# Deployment complete
$endTime = Get-Date
$duration = $endTime - $startTime
Write-Host ""
Write-Host "================================================================================" -ForegroundColor Green
Write-Host "                    DEPLOYMENT COMPLETED SUCCESSFULLY" -ForegroundColor Green
Write-Host "================================================================================" -ForegroundColor Green
Write-Host "Version: " -NoNewline -ForegroundColor Yellow
Write-Host $tagName -ForegroundColor White
Write-Host "Finished at: " -NoNewline -ForegroundColor Yellow
Write-Host $endTime.ToString("yyyy-MM-dd HH:mm:ss") -ForegroundColor White
Write-Host "Duration: " -NoNewline -ForegroundColor Yellow
Write-Host "$($duration.Minutes)m $($duration.Seconds)s" -ForegroundColor White
Write-Host "Site URL: " -NoNewline -ForegroundColor Cyan
Write-Host "https://hegardt.se" -ForegroundColor White
Write-Host "================================================================================" -ForegroundColor Green
Write-Host ""

Read-Host "Press Enter to exit"