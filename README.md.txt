# 🛡️ Ransomware Recovery Suite

An advanced modular Python-based system designed to **detect**, **monitor**, **defend against**, and **recover from ransomware attacks**. This project integrates cybersecurity techniques like honeypots, memory forensics, network sniffing, automated backup, decryption, and cloud recovery into a complete solution.

---

## 🚀 Features

* 🎯 **Ransomware Detection**

  * YARA rule-based scanning of files.
  * Behavior-based monitoring of suspicious activities.

* 🐍 **Honeypot System**

  * Decoy files used to detect unauthorized access/modification.

* 🌐 **Network Sniffer**

  * Captures outgoing encryption keys and suspicious traffic.

* 💾 **Memory Forensics**

  * Scans live memory for encryption keys and ransomware indicators.

* 🗃️ **Automated Backup System**

  * Backs up critical files to a secure local folder.
  * Secure overwrite for sanitization of infected files.

* ☁️ **Cloud Integration**

  * Upload/download files to/from AWS S3 for disaster recovery.

* 🔐 **Decryption Tool**

  * Decrypts files if the encryption key is known or captured.

* ⚙️ **System Health Monitoring**

  * Monitors CPU, memory, and disk usage.

---

## 🧰 Tech Stack

* Python
* Tkinter (GUI)
* Scapy (Network analysis)
* YARA (Malware detection)
* Boto3 (AWS S3 integration)
* Crypto (AES Decryption)
* psutil (System health monitoring)

---

## 🗂️ Project Structure

```
📁 RansomwareRecovery
|
|├— main.py                       # Main launcher
|├— backup_system.py             # Backup logic
|├— cloud_recovery.py            # AWS S3 upload/download
|├— decryptor.py                 # AES decryption logic
|├— health_monitor.py            # System health monitoring
|├— HoneypotSystem.py            # Honeypot monitoring
|├— MemoryForensics.py           # Memory dump analysis
|├— monitor.py                   # File behavior monitor
|├— network_sniffer.py           # Packet capture and analysis
|├— ransomware_detector.py       # YARA based scanner
|├— sanitize.py                  # Secure file overwrite
|├— utils.py                     # Utilities (logging, config)
|├— ransomware.yara              # YARA rules file
|└— config.json                  # (Optional) Config file
```

---

## 🛠️ Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/ransomware-recovery-suite.git
   cd ransomware-recovery-suite
   ```

2. **Create virtual environment (optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the main app:**

   ```bash
   python main.py
   ```

---

## 📌 Note

> This tool is for **educational and research purposes** only. Do not deploy on production systems without extensive testing.

---

## 📊 License

MIT License. See `LICENSE` file for details.
