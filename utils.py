import os
import logging
from datetime import datetime
import json
import shutil

# Set up logging configuration for utility functions
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to create and set up directories
def create_directory(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            logging.info(f"Directory created: {path}")
        else:
            logging.info(f"Directory already exists: {path}")
    except Exception as e:
        logging.error(f"Error creating directory {path}: {e}")

# Function to log events with detailed information
def log_event(event_message, log_file="events_log.txt"):
    try:
        with open(log_file, 'a') as log:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log.write(f"{timestamp} - {event_message}\n")
        logging.info(f"Event logged: {event_message}")
    except Exception as e:
        logging.error(f"Error logging event: {e}")

# Function to read configuration settings from a JSON file
def read_config(config_file="config.json"):
    try:
        if not os.path.exists(config_file):
            logging.error(f"Configuration file {config_file} not found!")
            return None
        
        with open(config_file, 'r') as file:
            config_data = json.load(file)
        logging.info(f"Configuration loaded from {config_file}")
        return config_data
    except Exception as e:
        logging.error(f"Error reading configuration file {config_file}: {e}")
        return None

# Function to write configuration settings to a JSON file
def write_config(config_data, config_file="config.json"):
    try:
        with open(config_file, 'w') as file:
            json.dump(config_data, file, indent=4)
        logging.info(f"Configuration saved to {config_file}")
    except Exception as e:
        logging.error(f"Error saving configuration file {config_file}: {e}")

# Function to safely delete files
def delete_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            logging.info(f"File deleted: {file_path}")
        else:
            logging.info(f"File not found: {file_path}")
    except Exception as e:
        logging.error(f"Error deleting file {file_path}: {e}")

# Function to move files to a safe directory (e.g., quarantine folder)
def move_file_to_safe_directory(file_path, safe_directory="quarantine"):
    try:
        if not os.path.exists(safe_directory):
            os.makedirs(safe_directory)
        
        # Extract the file name from the path
        file_name = os.path.basename(file_path)
        safe_path = os.path.join(safe_directory, file_name)
        
        shutil.move(file_path, safe_path)
        logging.info(f"File moved to safe directory: {safe_path}")
    except Exception as e:
        logging.error(f"Error moving file to safe directory: {e}")

# Function to get the current timestamp (for naming files or logs)
def get_current_timestamp():
    return datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Function to check if a file is encrypted based on file extension or content
def is_encrypted(file_path):
    encrypted_extensions = ['.enc', '.locked', '.crypto']
    
    if any(file_path.endswith(ext) for ext in encrypted_extensions):
        return True
    
    # Optionally, check the first few bytes of the file for typical encryption signatures
    try:
        with open(file_path, 'rb') as file:
            file_start = file.read(16)
            if file_start == b'\x00\x00\x00\x00\x00\x00\x00\x00':  # Example check (adjust based on actual encryption method)
                return True
    except Exception as e:
        logging.error(f"Error checking file encryption: {e}")
    
    return False

# Function to check if a process is suspicious by name (example: looking for "ransomware")
def is_suspicious_process(process_name):
    suspicious_keywords = ['ransomware', 'encrypt', 'malware']
    return any(keyword.lower() in process_name.lower() for keyword in suspicious_keywords)

# Function to retrieve a list of all files in a directory (recursively)
def get_files_in_directory(directory_path):
    try:
        file_list = []
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_list.append(os.path.join(root, file))
        logging.info(f"Files in directory {directory_path}: {len(file_list)} files found.")
        return file_list
    except Exception as e:
        logging.error(f"Error retrieving files from directory {directory_path}: {e}")
        return []

# Function to print the current system usage statistics (optional helper)
def print_system_usage():
    try:
        import psutil
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        logging.info(f"CPU Usage: {cpu}% | Memory Usage: {memory}%")
    except ImportError:
        logging.warning("psutil module not found, skipping system usage stats.")
    except Exception as e:
        logging.error(f"Error retrieving system usage: {e}")

# Example utility function for timestamped file backup
def backup_file(file_path):
    try:
        if os.path.exists(file_path):
            timestamp = get_current_timestamp()
            backup_path = f"{file_path}_{timestamp}.bak"
            shutil.copy(file_path, backup_path)
            logging.info(f"File backup created: {backup_path}")
    except Exception as e:
        logging.error(f"Error creating backup for file {file_path}: {e}")

