import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def capture_memory_dump():
    """Capture memory dump using DumpIt (for Windows) or LiME (for Linux)."""
    dump_file = "memory_dump.raw"
    
    if os.name == "nt":
        dump_tool = "DumpIt.exe"  # Windows Memory Dump Tool
        if not os.path.exists(dump_tool):
            messagebox.showerror("Error", "DumpIt.exe not found! Please download it first.")
            return None
        subprocess.run([dump_tool, "/OUTPUT", dump_file])
    
    elif os.name == "posix":
        dump_tool = "lime"  # Linux Memory Dump Tool
        if not os.path.exists(dump_tool):
            messagebox.showerror("Error", "LiME not found! Install it first.")
            return None
        subprocess.run(["sudo", dump_tool, "-o", dump_file])
    
    messagebox.showinfo("Success", f"Memory dump saved as {dump_file}")
    return dump_file

def analyze_memory_dump(dump_file):
    """Analyze memory dump using Volatility."""
    if not dump_file:
        messagebox.showerror("Error", "No memory dump file found!")
        return
    
    volatility_cmd = f"volatility -f {dump_file} --profile=Win10x64 pslist"
    result = subprocess.run(volatility_cmd, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        analysis_result = result.stdout
        messagebox.showinfo("Memory Analysis", analysis_result)
    else:
        messagebox.showerror("Error", "Failed to analyze memory dump!")

def browse_dump_file():
    """Open file dialog to browse an existing memory dump."""
    dump_file = filedialog.askopenfilename(filetypes=[("Memory Dump Files", "*.raw;*.dmp")])
    if dump_file:
        analyze_memory_dump(dump_file)

def perform_memory_forensics():
    """Capture and analyze memory dump."""
    # Capture the memory dump
    dump_file = capture_memory_dump()
    
    # Analyze the dump if successfully captured
    if dump_file:
        analyze_memory_dump(dump_file)

def create_gui():
    """Create GUI for Memory Forensics."""
    root = tk.Tk()
    root.title("Memory Forensics Tool")
    root.geometry("400x300")

    tk.Label(root, text="Memory Forensics Analysis", font=("Arial", 14)).pack(pady=10)
    
    tk.Button(root, text="Capture Memory Dump", command=capture_memory_dump).pack(pady=5)
    tk.Button(root, text="Analyze Memory Dump", command=browse_dump_file).pack(pady=5)
    tk.Button(root, text="Perform Full Memory Forensics", command=perform_memory_forensics).pack(pady=5)
    
    root.mainloop()

if __name__ == "__main__":
    create_gui()
