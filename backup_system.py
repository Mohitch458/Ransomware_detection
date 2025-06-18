import os
import shutil
import time
import logging

# Ensure logging is set up
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def backup_file(file_path, backup_dir):
    """Backs up a file to the specified directory"""
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        shutil.copy(file_path, backup_dir)
        logging.info(f"File {file_path} backed up to {backup_dir}")
    except Exception as e:
        logging.error(f"Error backing up {file_path}: {e}")

def backup_system(directory_to_backup, backup_dir="backups"):
    """Periodically backs up files from the specified directory"""
    while True:
        if not os.path.exists(directory_to_backup):
            logging.error(f"Backup source directory {directory_to_backup} does not exist!")
            return
        
        for file in os.listdir(directory_to_backup):
            file_path = os.path.join(directory_to_backup, file)
            if os.path.isfile(file_path):
                backup_file(file_path, backup_dir)
        
        logging.info("Backup process completed. Sleeping for 24 hours before next backup...")
        time.sleep(86400)  # Sleep for 1 day before backing up again

# Example usage (comment out when integrating with `main.py`)
# backup_system('/path/to/important/files')
