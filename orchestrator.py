from logging import config
import time
import subprocess
from decision_engine import decide_deployment
from config_loader import load_config


POWERSHELL_PATH = r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe"



def run_deployment():
   
    config = load_config()
      
 
    dry_run = config["mode"]["dry_run"]
    error_multiplier = config["thresholds"]["error_rate_multiplier"]
    latency_multiplier = config["thresholds"]["latency_multiplier"]
    max_latency = config["thresholds"]["max_latency_ms"]
 
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
    canary_healthy,
    error_multiplier,
    latency_multiplier,
    max_latency
    )


    print(f"Decision: {decision}")

    if decision == "ROLLBACK":
            if dry_run:
                 print("[DRY-RUN] Rollback would have been triggered.")
            else:
                print("Rolling back deployment...")
                subprocess.run(
                    [POWERSHELL_PATH, "-ExecutionPolicy", "Bypass", "-File", ROLLBACK_SCRIPT],
                    check=True
                )
    else:
            print("Deployment successful!")

if __name__ == "__main__":
    run_deployment()
