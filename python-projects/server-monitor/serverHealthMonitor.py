#this project will monitor the health of a server by checking its CPU usage, memory usage, and disk space. It will send an alert if any of these metrics exceed a certain threshold.
import psutil


cpu_usage = psutil.cpu_percent(interval=1)

memory = psutil.virtual_memory()

ram_usage = memory.percent

disk = psutil.disk_usage('/')
print(f"CPU Usage: {cpu_usage}%")
print(f"RAM Usage: {ram_usage}%")
print(f"Disk Usage: {disk.percent}%")

#real time scenario
if cpu_usage > 80:
    print("Alert: CPU usage is above 80%")
if ram_usage > 80:
    print("Alert: RAM usage is above 80%")
if disk.percent > 80:
    print("Alert: Disk usage is above 80%")