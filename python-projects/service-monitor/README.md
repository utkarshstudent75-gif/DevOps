# Linux Service Monitor

A Python-based monitoring script that checks whether Linux services are running.

## Features

- Monitors Linux services
- Detects active/inactive services
- Uses systemctl automation
- Infrastructure monitoring automation

## Technologies Used

- Python
- subprocess
- Linux systemctl

## Services Checked

- ssh
- cron
- amazon-ssm-agent

## How to Run

```bash
python3 service_monitor.py
```

## Sample Output

```text
ssh is RUNNING
cron is RUNNING
amazon-ssm-agent is RUNNING
```

## Concepts Learned

- subprocess automation
- Linux services
- loops
- conditionals
- command execution from Python