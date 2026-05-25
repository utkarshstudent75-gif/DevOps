# Disk Space Alert System

A Python-based monitoring script that checks system disk usage and sends alerts when disk usage exceeds a defined threshold.

## Features

- Monitors system disk usage
- Displays current disk utilization percentage
- Sends warning alerts when usage exceeds threshold
- Uses real-time system monitoring with psutil

## Technologies Used

- Python
- psutil

## Project Structure

```text
disk-alert/
│
├── disk_alert.py
├── requirements.txt
├── README.md
└── venv/
```

## How to Run

### 1. Create Virtual Environment

```bash
python3 -m venv venv
```

### 2. Activate Virtual Environment

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Script

```bash
python3 disk_alert.py
```

## Sample Output

### Normal Usage

```text
Disk usage is normal at 42.5%
```

### Warning Alert

```text
WARNING: Disk usage is at 85%
```

## Concepts Learned

- Python virtual environments
- System monitoring with psutil
- Conditional logic
- Disk usage monitoring
- Infrastructure alerting
- Automation scripting

## Future Improvements

- Add critical alerts above 90%
- Monitor multiple partitions
- Send email/slack alerts
- Save logs to file
- Add timestamps