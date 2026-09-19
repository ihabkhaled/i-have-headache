<#
.SYNOPSIS
    i-have-headache installer for Windows - concise mode, always on.
.DESCRIPTION
    One line:  irm https://raw.githubusercontent.com/ihabkhaled/i-have-headache/main/install.ps1 | iex
    Options:   & ([scriptblock]::Create((irm https://raw.githubusercontent.com/ihabkhaled/i-have-headache/main/install.ps1))) -Repo C:\src\app

    Claude Code: plugin + SessionStart hook. Codex: the skill + a block in AGENTS.md.
    Cursor: the skill + an alwaysApply rule. Re-run to update. Removes only what it
    recognises as its own. Environment (testing): HEADACHE_SOURCE,
    HEADACHE_USER_HOME, CODEX_HOME, HEADACHE_CLAUDE_BIN ('none' to skip).
#>
[CmdletBinding()]
param([switch]$Claude, [switch]$Codex, [switch]$Cursor, [string]$Repo, [string]$Ref = 'main', [switch]$Uninstall)

$ErrorActionPreference = 'Stop'
$Name = 'i-have-headache'
$RepoUrl = if ($env:HEADACHE_REPO_URL) { $env:HEADACHE_REPO_URL } else { 'https://github.com/ihabkhaled/i-have-headache.git' }
$UserHome = if ($env:HEADACHE_USER_HOME) { $env:HEADACHE_USER_HOME } elseif ($env:USERPROFILE) { $env:USERPROFILE } else { $HOME }
$CodexDir = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $UserHome '.codex' }
$BeginMark = '<!-- i-have-headache:begin'
$EndMark = '<!-- i-have-headache:end -->'
$Marker = 'I have a headache.'
$Utf8 = New-Object System.Text.UTF8Encoding($false)

function Say([string]$T) { Write-Host $T }
function Write-Utf8([string]$P, [string]$T) {
    $d = Split-Path -Parent $P; if ($d -and -not (Test-Path $d)) { New-Item -ItemType Directory -Force $d | Out-Null }
    [IO.File]::WriteAllText($P, $T, $Utf8)
}
function Read-Lf([string]$P) { [IO.File]::ReadAllText($P, $Utf8) -replace "`r`n", "`n" }
function Test-Crlf([string]$P) { (Test-Path $P) -and [IO.File]::ReadAllText($P, $Utf8).Contains("`r`n") }
function Write-Endings([string]$P, [string]$T, [bool]$Crlf) { if ($Crlf) { $T = $T -replace "`n", "`r`n" }; Write-Utf8 $P $T }

if ($Repo) { if (-not (Test-Path $Repo -PathType Container)) { throw "not a directory: $Repo" }; $Repo = (Resolve-Path $Repo).Path }

function Find-Claude {
    if ($env:HEADACHE_CLAUDE_BIN) { if ($env:HEADACHE_CLAUDE_BIN -eq 'none') { return $null }; return $env:HEADACHE_CLAUDE_BIN }
    $c = Get-Command claude -ErrorAction SilentlyContinue; if ($c) { return $c.Source }
    $ext = Join-Path $UserHome '.vscode\extensions'
    if (Test-Path $ext) {
        $b = Get-ChildItem $ext -Directory -Filter 'anthropic.claude-code-*' | ForEach-Object { Join-Path $_.FullName 'resources\native-binary\claude.exe' } |
            Where-Object { Test-Path $_ } | Sort-Object { [version](($_ -split 'anthropic\.claude-code-')[1] -split '-')[0] } | Select-Object -Last 1
        if ($b) { return $b }
    }
    return $null
}
$ClaudeBin = Find-Claude

if (-not ($Claude -or $Codex -or $Cursor)) {
    if ($ClaudeBin) { $Claude = $true }
    if ((Get-Command codex -ErrorAction SilentlyContinue) -or (Test-Path $CodexDir)) { $Codex = $true }
    if ((Get-Command cursor -ErrorAction SilentlyContinue) -or (Test-Path (Join-Path $UserHome '.cursor'))) { $Cursor = $true }
    if ($Repo) { $Codex = $true; $Cursor = $true }
    if (-not ($Claude -or $Codex -or $Cursor)) { throw 'found none of Claude Code, Codex or Cursor. Name one: -Claude, -Codex or -Cursor.' }
}

function Test-Checkout([string]$D) { (Test-Path (Join-Path $D "skills\$Name\SKILL.md")) -and (Test-Path (Join-Path $D '.claude-plugin\plugin.json')) }
$LocalSource = $false; $Src = $null
if ($env:HEADACHE_SOURCE) {
    if (-not (Test-Checkout $env:HEADACHE_SOURCE)) { throw 'HEADACHE_SOURCE is not an i-have-headache checkout' }
    $Src = (Resolve-Path $env:HEADACHE_SOURCE).Path; $LocalSource = $true
} elseif ($PSScriptRoot -and (Test-Checkout $PSScriptRoot)) { $Src = $PSScriptRoot; $LocalSource = $true }

if (-not $Src -and -not $Uninstall -and ($Codex -or $Cursor)) {
    $Src = Join-Path $UserHome '.i-have-headache\src'
    if (Get-Command git -ErrorAction SilentlyContinue) {
        if (Test-Path (Join-Path $Src '.git')) {
            git -C $Src fetch --quiet --depth 1 origin $Ref; git -C $Src checkout --quiet --force FETCH_HEAD
        } else {
            if (Test-Path $Src) { Remove-Item -Recurse -Force $Src }
            git clone --quiet --depth 1 --branch $Ref $RepoUrl $Src; if ($LASTEXITCODE) { throw 'git clone failed' }
        }
    } else {
        $zip = Join-Path ([IO.Path]::GetTempPath()) "headache-$Ref.zip"; $un = Join-Path ([IO.Path]::GetTempPath()) "headache-$Ref"
        Invoke-WebRequest -UseBasicParsing -Uri "https://codeload.github.com/ihabkhaled/i-have-headache/zip/$Ref" -OutFile $zip
        if (Test-Path $un) { Remove-Item -Recurse -Force $un }; Expand-Archive $zip $un
        if (Test-Path $Src) { Remove-Item -Recurse -Force $Src }
        New-Item -ItemType Directory -Force (Split-Path -Parent $Src) | Out-Null
        Move-Item (Get-ChildItem $un -Directory | Select-Object -First 1).FullName $Src
    }
    if (-not (Test-Checkout $Src)) { throw "the download at $Src is incomplete" }
}

# The always-on rules: the skill body minus frontmatter and minus the
# acknowledgement meant for an explicit run. The skill stays the only copy.
function Get-Rules {
    $lines = (Read-Lf (Join-Path $Src "skills\$Name\SKILL.md")) -split "`n"
    $out = New-Object System.Collections.Generic.List[string]; $front = $false
    for ($i = 0; $i -lt $lines.Count; $i++) {
        $l = $lines[$i]
        if ($i -eq 0 -and $l -eq '---') { $front = $true; continue }
        if ($front) { if ($l -eq '---') { $front = $false }; continue }
        if ($l.StartsWith('Concise mode is always on')) { break }
        $out.Add($l)
    }
    return ($out -join "`n") + "`n"
}

if ($Repo) {
    $SkillsRoot = Join-Path $Repo '.agents\skills'; $Contract = Join-Path $Repo 'AGENTS.md'
    $Rule = Join-Path $Repo ".cursor\rules\$Name.mdc"; $Scope = 'project'
} else {
    $SkillsRoot = Join-Path $UserHome '.agents\skills'; $Contract = Join-Path $CodexDir 'AGENTS.md'
    $Rule = Join-Path $UserHome ".cursor\rules\$Name.mdc"; $Scope = 'user'
}

function Remove-BlockText([string]$T) {
    [regex]::Replace($T, '(?ms)^' + [regex]::Escape($BeginMark) + '.*?^' + [regex]::Escape($EndMark) + '[^\n]*\n?', '')
}
function Remove-Ours {
    foreach ($f in @((Join-Path $SkillsRoot "$Name\SKILL.md"), (Join-Path $CodexDir "prompts\$Name.md"))) {
        if ((Test-Path $f) -and (Select-String -Path $f -SimpleMatch $Marker -Quiet)) {
            if ($f.EndsWith('SKILL.md')) { Remove-Item -Recurse -Force (Split-Path -Parent $f) } else { Remove-Item -Force $f }
            Say "removed $f"
        }
    }
}
function Invoke-Claude([string[]]$A) {
    if ($Repo) { Push-Location $Repo }
    try { & $ClaudeBin @A | Out-Host; return $LASTEXITCODE } finally { if ($Repo) { Pop-Location } }
}

if ($Uninstall) {
    if ($Claude -and $ClaudeBin) { $null = Invoke-Claude @('plugin', 'uninstall', "$Name@$Name", '--scope', $Scope) }
    if ($Codex -or $Cursor) { Remove-Ours }
    if ($Codex -and (Test-Path $Contract)) {
        $crlf = Test-Crlf $Contract; $t = Read-Lf $Contract
        if ($t.Contains($BeginMark)) {
            $rest = (Remove-BlockText $t).TrimEnd("`n", ' ', "`t")
            if ($rest) { Write-Endings $Contract "$rest`n" $crlf } else { Remove-Item -Force $Contract }
            Say "removed the concise-mode block from $Contract"
        }
    }
    if ($Cursor -and (Test-Path $Rule) -and (Select-String -Path $Rule -SimpleMatch $Marker -Quiet)) { Remove-Item -Force $Rule; Say "removed $Rule" }
    foreach ($d in @($SkillsRoot, (Split-Path -Parent $SkillsRoot), (Split-Path -Parent $Rule), (Split-Path -Parent (Split-Path -Parent $Rule)))) {
        if ((Test-Path $d) -and -not (Get-ChildItem -Force $d)) { Remove-Item -Force $d }
    }
    Say 'i-have-headache uninstalled.'; return
}

if ($Claude) {
    if (-not $ClaudeBin) { Write-Warning "Claude Code CLI not found. In VS Code: /plugins -> Marketplaces -> add $RepoUrl -> install." }
    else {
        $market = if ($LocalSource) { $Src } else { "$RepoUrl#$Ref" }
        if (Invoke-Claude @('plugin', 'marketplace', 'add', $market, '--scope', $Scope)) { throw 'claude plugin marketplace add failed' }
        $null = Invoke-Claude @('plugin', 'install', "$Name@$Name", '--scope', $Scope)
        $null = Invoke-Claude @('plugin', 'update', "$Name@$Name", '--scope', $Scope) 2>$null
        Say "Claude Code: installed ($Scope scope). Restart Claude."
    }
}
if ($Codex -or $Cursor) {
    Remove-Ours
    New-Item -ItemType Directory -Force $SkillsRoot | Out-Null
    Copy-Item -Recurse -Force (Join-Path $Src "skills\$Name") (Join-Path $SkillsRoot $Name)
    Say "installed the skill to $(Join-Path $SkillsRoot $Name)"
}
if ($Codex) {
    $crlf = Test-Crlf $Contract
    $existing = if (Test-Path $Contract) { (Remove-BlockText (Read-Lf $Contract)).TrimEnd("`n", ' ', "`t") } else { '' }
    $block = "$BeginMark - installed by i-have-headache; reinstall to update. Replaced on reinstall. -->`n" + (Get-Rules) + "$EndMark`n"
    $text = if ($existing) { "$existing`n`n$block" } else { $block }
    Write-Endings $Contract $text $crlf
    Say "wrote the concise-mode block in $Contract"
    $override = Join-Path (Split-Path -Parent $Contract) 'AGENTS.override.md'
    if ((Test-Path $override) -and ($Repo -or (Get-Item $override).Length -gt 0)) { Write-Warning "$override exists; Codex reads it INSTEAD of AGENTS.md there, so merge the block into it." }
}
if ($Cursor) {
    Write-Utf8 $Rule ("---`ndescription: i-have-headache - concise mode, always on`nalwaysApply: true`n---`n`n" + (Get-Rules))
    Say "wrote $Rule"
}
Say 'Done. Concise mode is always on. Re-run to update; -Uninstall to remove.'
