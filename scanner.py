from modules.basic_scan import run_basic_scan
from modules.service_scan import run_service_scan
from modules.vuln_scan import run_vuln_scan
from modules.output_handler import save_output

import shutil
import subprocess

# 🔍 Check if Nmap is installed
if not shutil.which("nmap"):
    raise EnvironmentError("❌ Nmap not found. Run: sudo apt install nmap")

print("✅ Import successful")

# 🎯 Target input
target = input("🎯 Enter target IP or domain: ")

# 🚧 Ethical permission gate
permission = input("\n⚠️ Type 'I have permission to scan' to continue: ")
if permission.strip().lower() != "i have permission to scan":
    print("\n⛔ Scan aborted. Permission not confirmed.")
    exit()

# 🧪 Ask for scan type
scan_type = input("\n🧪 Choose scan type (fast/full/stealth): ").strip().lower()

# 🔧 Basic scan logic with mode selection
def run_basic_scan(target, mode="fast"):
    if mode == "fast":
        cmd = ["nmap", "-Pn", "-T4", "-F", "-n", target]
    elif mode == "full":
        cmd = ["nmap", "-Pn", "-T4", "-p-", "-n", target]
    elif mode == "stealth":
        cmd = ["nmap", "-sS", "-Pn", "-n", target]
    else:
        cmd = ["nmap", "-Pn", "-T4", "-F", "-n", target]

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

# 🚀 Start scanning
print("\n✅ Permission confirmed. Starting scan...\n")

print("[+] Running basic scan...")
basic_result = run_basic_scan(target, scan_type)

print("[+] Running service scan...")
service_result = run_service_scan(target)

print("[+] Running vulnerability scan...")
vuln_result = run_vuln_scan(target)

# 💾 Save results
save_output(target, basic_result, service_result, vuln_result)
print("\n✅ Scan complete. Results saved in results/scan_logs.txt")
