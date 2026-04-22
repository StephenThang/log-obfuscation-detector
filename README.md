# Log Obfuscation Detector

A Python-based log analysis tool that uses regular expressions to detect obfuscation techniques attackers use to hide malicious activity in network logs.

---

## Overview

Security analysts and threat hunters manually sift through thousands of log lines daily looking for suspicious activity. This tool automates that process by scanning log files for three common obfuscation techniques and generating a formatted threat report.

---

## Obfuscation Techniques Detected

| Technique | Example | What it means |
|---|---|---|
| Base64 Encoded Payload | `cmd=aGVsbG8gV29ybGQ=` | Attacker hiding commands in encoded strings |
| URL Encoding | `GET /%2e%2e%2f%65%74%63%2f%70%61%73%73%77%64` | Attacker encoding URLs to bypass filters |
| Hex Obfuscated IP | `connection from 0x7f000001` | Attacker hiding IP addresses in hexadecimal |

---

## Project Structure

```
log-obfuscation-detector/
│
├── log_scanner.py       # Main scanner class and logic
├── logs.txt             # Sample log file with suspicious entries
└── README.md            # Project documentation
```

---

## How to Run

**1. Clone the repository**
```bash
git clone https://github.com/StephenThang/log-obfuscation-detector.git
cd log-obfuscation-detector
```

**2. Make sure Python is installed**
```bash
python --version
```
Requires Python 3.10 or higher.

**3. Run the scanner**
```bash
python log_scanner.py
```

**4. Expected output**
```
==================================================
       OBFUSCATION THREAT REPORT
==================================================
  Total Suspicious Lines Found: 9
==================================================

  [1] ALERT: cmd=aGVsbG8gV29ybGQgdGhpcyBpcyBiYXNlNjQ=
       TYPE: Base64 Encoded Payload

  [2] ALERT: connection attempt from 0x7f000001
       TYPE: Hex Obfuscated IP

  [3] ALERT: GET /%2F%2F%65%76%69%6C 404 NOT FOUND
       TYPE: URL Encoding Obfuscation
...
==================================================
       END OF REPORT
==================================================
```

---

## Skills Demonstrated

- Python object oriented programming
- Regular expressions for pattern matching
- File I/O and log ingestion
- Cybersecurity threat detection concepts
- SOC analyst style log triage and reporting

---

## Author

**Stephen Vanlian Thang**  
Dual B.S. Psychology & Information Science (Cybersecurity) — University of Maryland  
Certified Ethical Hacker (CEH)  
[Portfolio](https://StephenThang.github.io) | [LinkedIn](https://linkedin.com/in/stephenthang)
