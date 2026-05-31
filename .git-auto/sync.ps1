param(
    [ValidateSet("sync", "push")]
    [string]$Mode = "sync"
)

$RepoPath = "D:\codingFiles"
$LogFile = "$RepoPath\.git-auto\sync.log"
$SshKey = "$env:USERPROFILE\.ssh\id_ed25519"

# 设置 SSH 认证（绕过 ssh-agent，直接指定密钥）
$env:GIT_SSH_COMMAND = "ssh -i `"$SshKey`" -o BatchMode=yes -o StrictHostKeyChecking=accept-new"

function Write-Log {
    param([string]$Message)
    $Time = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$Time | $Message" | Out-File -FilePath $LogFile -Append -Encoding UTF8
}

function Invoke-Git {
    param([string]$Command)
    $result = & git -C $RepoPath $Command.Split(" ", [StringSplitOptions]::RemoveEmptyEntries) 2>&1
    $output = $result -join "`n"
    if ($LASTEXITCODE -ne 0) {
        Write-Log "ERROR: git $Command => $output"
        return $false
    }
    Write-Log "OK: git $Command"
    if ($output) { Write-Log "  $output" }
    return $true
}

Write-Log "===== START ($Mode) ====="

# 检查 SSH 连通性
# GitHub SSH 认证成功返回 exit code 1（"不提供 shell 访问"），失败才返回 255
$sshTest = ssh -i "$SshKey" -o BatchMode=yes -o StrictHostKeyChecking=accept-new -T git@github.com 2>&1
if ($LASTEXITCODE -eq 255) {
    Write-Log "ERROR: SSH connection to GitHub failed"
    Write-Log "  $sshTest"
    Write-Log "===== END (FAILED) ====="
    exit 1
}

# Step 1: 总是先 fetch
$ok = Invoke-Git "fetch origin"

if ($Mode -eq "sync") {
    # 每2小时自动同步：pull --rebase
    if ($ok) {
        Invoke-Git "pull --rebase origin main" | Out-Null
    }
}
elseif ($Mode -eq "push") {
    # 晚上 11 点：自动 commit + push
    # 先 pull --rebase 避免冲突
    if ($ok) {
        Invoke-Git "pull --rebase origin main" | Out-Null
    }

    # 检查是否有变化
    $status = & git -C $RepoPath status --porcelain
    if ($status) {
        $timeStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $commitMsg = "auto commit $timeStr"

        & git -C $RepoPath add -A 2>&1 | Out-Null
        $commitResult = & git -C $RepoPath commit -m "$commitMsg" 2>&1
        if ($LASTEXITCODE -eq 0) {
            Write-Log "OK: git commit -m '$commitMsg'"
        } else {
            Write-Log "INFO: commit skipped or failed: $commitResult"
        }

        # push
        Invoke-Git "push origin main"
    } else {
        Write-Log "INFO: No changes to commit"
        # 虽然没有更改，仍然做一次 push（确保远端有最新的本地 fetch 结果，虽然其实不需要）
        Invoke-Git "push origin main"
    }
}

Write-Log "===== END (SUCCESS) ====="
