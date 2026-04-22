import re

class LogScanner():
    def __init__(self):
        self.logs = []
        self.findings = []

    def load_logs(self, filename):
        with open(filename, "r") as file:
            self.logs = file.readlines()

    def scan_base64(self):
        for line in self.logs:
            if re.search(r'[A-Za-z0-9+/=]{20,}', line):
                self.findings.append(line)

    def scan_url_encodings(self):
        for line in self.logs:
            if re.search(r'%[0-9a-fA-F]{2}', line):
                self.findings.append(line)

    def scan_hex_ip(self):
        for line in self.logs:
            if re.search(r'0x[0-9a-fA-F]+', line):
                self.findings.append(line)

    def run_all_scans(self):
        self.scan_base64()  
        self.scan_hex_ip()
        self.scan_url_encodings()
        return self.findings
    
    def __str__(self):
        report = ""
        report += "=" * 50 + "\n"
        report += "       OBFUSCATION THREAT REPORT\n"
        report += "=" * 50 + "\n"
        report += f"  Total Suspicious Lines Found: {len(self.findings)}\n"
        report += "=" * 50 + "\n\n"

        for i, line in enumerate(self.findings):
            report += f"  [{i+1}] ALERT: {line.strip()}\n"
            
            if re.search(r'[A-Za-z0-9+/=]{20,}', line):
                report += "       TYPE: Base64 Encoded Payload\n"
            if re.search(r'%[0-9a-fA-F]{2}', line):
                report += "       TYPE: URL Encoding Obfuscation\n"
            if re.search(r'0x[0-9a-fA-F]+', line):
                report += "       TYPE: Hex Obfuscated IP\n"
            report += "\n"

        report += "=" * 50 + "\n"
        report += "       END OF REPORT\n"
        report += "=" * 50 + "\n"
        return report
        
if __name__ == "__main__":
    Scanner = LogScanner()
    Scanner.load_logs("logs.txt")
    Scanner.run_all_scans()
    print(Scanner)