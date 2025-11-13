# 🔍 Nmap Recon HackerProf

Modular Nmap scanning tool for ethical recon and awareness.  
Built by **Hacker Professor — Himanshu Yadav** for educational use only.

---

## 🚀 Features

- 🎯 IP/domain input with permission gate  
- 🧪 Multiple scan modes: `basic`, `full`, `stealth`  
- 🔧 Service fingerprinting (`-sV`)  
- ⚠️ Vulnerability detection (`--script vuln`)  
- 📁 Modular structure for easy upgrades  
- 📝 Logs saved in `results/scan_logs.txt`  

---

## 🛡️ Ethical Use

Before scanning, user must confirm permission by typing:
I have permission to scan


Unauthorized scanning is strictly prohibited.  
This tool is for awareness, education, and authorized testing only.

.You’ll be prompted to:

.Enter target IP or domain

.Confirm ethical permission

.Choose scan type: basic, full, or stealth


## 🧪 Scan Modes
#Mode	Flags Used	Description
#basic	-Pn -T4 -F -n	Fast scan on top 100 ports
#full	-Pn -T4 -p- -n	Full port scan (1–65535)
#stealth	-sS -Pn -n	SYN scan (stealthy and quiet)
## 📦 Modules

Module	Purpose  /
basic_scan.py	/ /Fast top-port scan
full_scan.py  // 	Full port scan
stealth_scan.py //	SYN stealth scan
service_scan.py  //	Service fingerprinting
vuln_scan.py	 // Vulnerability detection
output_handler.py //	Save results to file


🔮 Roadmap
🌐 WHOIS and DNS modules

🧠 CVE fetcher via NVD API

📊 HTML/JSON report generator

📁 Batch scan from targets.txt

🖥️ GUI version using Flask or Tkinter

## 🙌 Author
Himanshu Yadav — Hacker Professor 👨‍💻 GitHub: @Himanshu9528-hacker

💡 Scan smart. Stay ethical. Recon like a Professor.
---

## 🧠 Usage

```bash
python scanner.py



