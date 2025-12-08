# Hegardt.se Deployment Script
# PowerShell version with beautiful output

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
    Write-Host "| " -ForegroundColor Blue -NoNewline
    Write-Host "Step $Step" -ForegroundColor Green -NoNewline
    Write-Host " $Message" -ForegroundColor White
    if ($Extra) {
        Write-Host "| " -ForegroundColor Blue -NoNewline
        Write-Host "$Extra" -ForegroundColor 
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

# Step 1: Install dependencies
Write-Box "1/5:" "Installing npm dependencies..."
npm i
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to install dependencies!"
    exit 1
}
Write-Success "Dependencies installed successfully"

# Step 2: Build distribution
Write-Box "2/5:" "Building distribution..."
npm run build
if ($LASTEXITCODE -ne 0) {
    Write-Error "Build failed!"
    exit 1
}
Write-Success "Build completed successfully"

# Step 3: Transfer files
Write-Box "3/5:" "Transferring dist/ to server..." "Target: root@134.209.240.67:/var/www/hegardt.se/html/"
scp -r "dist/*" root@134.209.240.67:/var/www/hegardt.se/html/
if ($LASTEXITCODE -ne 0) {
    Write-Error "File transfer failed!"
    exit 1
}
Write-Success "Files transferred successfully"

# Step 4: Set permissions
Write-Box "4/5:" "Setting file permissions..."
ssh root@134.209.240.67 "sudo chmod -R 755 /var/www/hegardt.se"
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to set permissions!"
    exit 1
}
Write-Success "Permissions set successfully"

# Step 5: Restart Nginx
Write-Box "5/5:" "Restarting Nginx..."
ssh root@134.209.240.67 "sudo systemctl restart nginx"
if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to restart Nginx!"
    exit 1
}
Write-Success "Nginx restarted successfully"

# Deployment complete
$endTime = Get-Date
$duration = $endTime - $startTime
Write-Host ""
Write-Host "================================================================================" -ForegroundColor Green
Write-Host "                    DEPLOYMENT COMPLETED SUCCESSFULLY" -ForegroundColor Green
Write-Host "================================================================================" -ForegroundColor Green
Write-Host "Finished at: " -NoNewline -ForegroundColor Yellow
Write-Host $endTime.ToString("yyyy-MM-dd HH:mm:ss") -ForegroundColor White
Write-Host "Duration: " -NoNewline -ForegroundColor Yellow
Write-Host "$($duration.Minutes)m $($duration.Seconds)s" -ForegroundColor White
Write-Host "Site URL: " -NoNewline -ForegroundColor Cyan
Write-Host "https://hegardt.se" -ForegroundColor White
Write-Host "================================================================================" -ForegroundColor Green
Write-Host ""

Read-Host "Press Enter to exit"