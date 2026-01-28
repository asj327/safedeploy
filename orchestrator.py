import time
import subprocess
from decision_engine import decide_deployment

POWERSHELL_PATH = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"

def run_deployment():
    print("Starting canary deployment...")

    # Simulated metrics (we'll replace this later)
    stable_error_rate = 0.5
    canary_error_rate = 1.5
    stable_latency = 200
    canary_latency = 450
    canary_healthy = True

    print("Collecting metrics...")
    time.sleep(5)  # simulate waiting period

    decision = decide_deployment(
        stable_error_rate,
        canary_error_rate,
        stable_latency,
        canary_latency,
        canary_healthy
    )

    print(f"Decision: {decision}")

    if decision == "ROLLBACK":
        print("Rolling back deployment...")
        subprocess.run(
            [POWERSHELL_PATH, "-ExecutionPolicy", "Bypass", "-File", "rollback.ps1"]
        )
    else:
        print("Deployment successful!")


if __name__ == "__main__":
    run_deployment()

