#this program will show the disk usage of the system and send an alert if the usage exceeds a certain threshold.
import psutil

disk_usage = psutil.disk_usage('/')
threshold = 80
usage_percent = disk_usage.percent
if usage_percent >= threshold:
    print(f"Disk usage is at {usage_percent}%, which exceeds the threshold of {threshold}%.")
else:
    print(f"Disk usage is at {usage_percent}%, which is within the threshold of {threshold}%.")

