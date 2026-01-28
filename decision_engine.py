def decide_deployment(
    stable_error_rate,
    canary_error_rate,
    stable_latency,
    canary_latency,
    canary_healthy
):
    # Rule 1: Canary must be alive
    if not canary_healthy:
        return "ROLLBACK"

    # Rule 2: Error rate comparison
    if canary_error_rate > 2 * stable_error_rate:
        return "ROLLBACK"

    # Rule 3: Latency comparison
    if canary_latency > 1.5 * stable_latency:
        return "ROLLBACK"

    # If all checks pass
    return "PROMOTE"
