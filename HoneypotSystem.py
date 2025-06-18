# HoneypotSystem.py

import os
import time
import threading
import tkinter as tk
import tkinter.messagebox as messagebox

HONEYPOT_DIR = "honeypot_files"
HONEYPOT_FILES = ["fake_doc.txt", "dummy_passwords.csv", "fake_budget.xlsx"]

def create_honeypot():
    """Create honeypot files to detect ransomware activity."""
    if not os.path.exists(HONEYPOT_DIR):
        os.makedirs(HONEYPOT_DIR)
    for filename in HONEYPOT_FILES:
        file_path = os.path.join(HONEYPOT_DIR, filename)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("This is a dummy honeypot file for ransomware detection.")

def monitor_honeypot():
    """Monitor honeypot files for unauthorized modifications."""
    file_snapshots = {file: os.path.getmtime(os.path.join(HONEYPOT_DIR, file)) for file in HONEYPOT_FILES}
    while True:
        for file in HONEYPOT_FILES:
            file_path = os.path.join(HONEYPOT_DIR, file)
            try:
                last_modified = os.path.getmtime(file_path)
                if file in file_snapshots and last_modified != file_snapshots[file]:
                    print(f"🚨 ALERT: Potential ransomware activity detected on {file_path}")
                    messagebox.showwarning("Honeypot Alert", f"Unauthorized modification detected: {file}")
                file_snapshots[file] = last_modified
            except Exception:
                pass
        time.sleep(5)

def honeypot_listener():
    """Start monitoring honeypot files in a separate thread."""
    threading.Thread(target=monitor_honeypot, daemon=True).start()
    messagebox.showinfo("Honeypot Monitoring", "Honeypot monitoring started.")
