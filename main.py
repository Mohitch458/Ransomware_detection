import os
import logging
from backup_system import backup_system
from decryptor import Decryptor
from health_monitor import monitor_system_health
from HoneypotSystem import honeypot_listener
from MemoryForensics import perform_memory_forensics
from monitor import monitor_system
from network_sniffer import start_network_traffic_analysis
from ransomware_detector import detect_ransomware
from sanitize import overwrite_file
from utils import create_directory, log_event, read_config

# Initialize logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Read configuration
config = read_config("config.json")

if config is None:
    logging.error("Configuration loading failed. Exiting program.")
    exit()

# Create necessary directories
create_directory(config['backup_dir'])
create_directory(config['quarantine_dir'])

# Function to start all modules
def start_ransomware_recovery():
    logging.info("Starting ransomware recovery system...")

    # Start monitoring system and network traffic
    monitor_system()
    start_network_traffic_analysis()


    # Start the honeypot listener
    honeypot_listener()

    # Perform memory forensics
    perform_memory_forensics()

    # Detect ransomware activity
    detect_ransomware(config['directory_to_monitor'])

    # Monitor system health
    monitor_system_health(cpu_threshold=90, memory_threshold=90, disk_threshold=90)

    # Start the backup system
    backup_system(config['directory_to_backup'], config['backup_dir'])

    # Decrypt encrypted files
    decryptor = Decryptor()
    decryptor.decrypt_files(config['encrypted_files_directory'])

    # Sanitization of suspicious files
    for file in os.listdir(config['quarantine_dir']):
        file_path = os.path.join(config['quarantine_dir'], file)
        overwrite_file(file_path)

    log_event("Ransomware recovery system started and running smoothly.")

if __name__ == "__main__":
    try:
        start_ransomware_recovery()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        log_event(f"Error: {e}")
