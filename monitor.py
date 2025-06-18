import psutil
import time
import logging
import os
import threading

# Set up logging configuration
logging.basicConfig(filename='monitoring_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_system_usage():
    """Logs CPU, memory, disk, and network usage."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        net_io = psutil.net_io_counters()

        logging.info(f"CPU Usage: {cpu_usage}%")
        logging.info(f"Memory Usage: {memory.percent}%")
        logging.info(f"Disk Usage: {disk.percent}%")
        logging.info(f"Network Sent: {net_io.bytes_sent} bytes, Received: {net_io.bytes_recv} bytes")

        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
            if proc.info['cpu_percent'] > 50:
                logging.warning(f"High CPU process: {proc.info['name']} (PID: {proc.info['pid']})")
            
            if 'ransomware' in proc.info['name'].lower():
                logging.critical(f"Suspicious ransomware detected: {proc.info['name']} (PID: {proc.info['pid']})")

    except Exception as e:
        logging.error(f"Error in system monitoring: {e}")

def monitor_system():
    """Continuously logs system metrics in the background."""
    while True:
        log_system_usage()
        time.sleep(60)  # Monitor every 60 seconds

if __name__ == "__main__":
    monitor_system()
