#service monitoring
import subprocess

services = ["ssh", "cron", "amazon-ssm-agent"]

for service in services:

    result = subprocess.run(
        ["systemctl", "is-active", service],
        capture_output=True,
        text=True
    )
    status = result.stdout.strip()

    if status == "active":
        print(f"{service} is running.")
    else:
        print(f"{service} is not running.")


