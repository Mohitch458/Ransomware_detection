import psutil
import logging

def monitor_system_health(cpu_threshold=80, memory_threshold=80, disk_threshold=80):
    """Monitor system health and alert if thresholds are exceeded"""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    
    if cpu > cpu_threshold:
        logging.warning(f"High CPU Usage: {cpu}%")
    if memory > memory_threshold:
        logging.warning(f"High Memory Usage: {memory}%")
    if disk > disk_threshold:
        logging.warning(f"High Disk Usage: {disk}%")

# Example usage
monitor_system_health(cpu_threshold=90, memory_threshold=90, disk_threshold=90)
