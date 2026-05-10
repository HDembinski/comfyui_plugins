param(
    [Parameter(Mandatory = $true)]
    [string]$ComfyUIPath,

    [switch]$Force
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
$customNodesPath = Join-Path $ComfyUIPath "custom_nodes"
$targetPath = Join-Path $customNodesPath "comfyui_plugins"

if (-not (Test-Path $customNodesPath)) {
    throw "Could not find custom_nodes at: $customNodesPath"
}

if (Test-Path $targetPath) {
    if (-not $Force) {
        throw "Target already exists: $targetPath. Re-run with -Force to replace it."
    }

    Remove-Item -Path $targetPath -Recurse -Force
}

try {
    New-Item -ItemType SymbolicLink -Path $targetPath -Target $repoRoot | Out-Null
    Write-Host "Created symlink: $targetPath -> $repoRoot"
}
catch {
    Write-Warning "Symbolic link failed. Falling back to junction."
    New-Item -ItemType Junction -Path $targetPath -Target $repoRoot | Out-Null
    Write-Host "Created junction: $targetPath -> $repoRoot"
}
