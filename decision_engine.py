def decide_deployment(
    stable_error_rate,
    canary_error_rate,
    stable_latency,
    canary_latency,
    canary_healthy,
    error_multiplier,
    latency_multiplier,
    max_latency
):
    if not canary_healthy:
        return "ROLLBACK"

    if canary_error_rate > stable_error_rate * error_multiplier:
        return "ROLLBACK"

    if canary_latency > stable_latency * latency_multiplier:
        return "ROLLBACK"

    if canary_latency > max_latency:
        return "ROLLBACK"

    return "CONTINUE"
