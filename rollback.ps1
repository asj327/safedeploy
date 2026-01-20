Write-Host "Checking v2 health..."

try {
    # Health check
    $health = Invoke-WebRequest -Uri http://127.0.0.1:8001/health -UseBasicParsing

    if ($health.StatusCode -ne 200) {
        throw "Health endpoint failed"
    }

    # Canary API check (simulates real traffic)
    $api = Invoke-WebRequest -Uri http://127.0.0.1:8001/api -UseBasicParsing

    if ($api.StatusCode -ne 200) {
        throw "API check failed"
    }

    Write-Host "v2 passed canary checks. No rollback needed."
}
catch {
    Write-Host "v2 failed canary checks ❌ Rolling back..."

    docker stop safedeploy_v2 | Out-Null
    docker rm safedeploy_v2 | Out-Null

    Write-Host "Rollback complete. v1 is still serving traffic ✅"
}
