import os
import psutil
import logging

def check_suspicious_files(directory):
    """Checks for unusual file extensions in the specified directory"""
    encrypted_extensions = ['.enc', '.locked', '.crypto']
    suspicious_files = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in encrypted_extensions):
                suspicious_files.append(os.path.join(root, file))
    
    if suspicious_files:
        logging.warning(f"Suspicious files detected: {suspicious_files}")
    else:
        logging.info("No suspicious files found.")

def detect_ransomware_process():
    """Detect suspicious processes indicating ransomware"""
    suspicious_keywords = ['ransomware', 'encrypt', 'malware']
    for proc in psutil.process_iter(['pid', 'name']):
        if any(keyword in proc.info['name'].lower() for keyword in suspicious_keywords):
            logging.warning(f"Suspicious process detected: {proc.info['name']} (PID: {proc.info['pid']})")

def detect_ransomware(directory):
    """Run checks to detect ransomware"""
    check_suspicious_files(directory)
    detect_ransomware_process()

# Example usage
detect_ransomware('/path/to/monitor')
