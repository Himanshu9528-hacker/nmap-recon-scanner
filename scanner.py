from modules.basic_scan import run_scan as run_basic_scan
from modules.full_scan import run_full_scan
from modules.stealth_scan import run_stealth_scan
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
scan_type = input("\n🧪 Choose scan type (basic/full/stealth): ").strip().lower()

# 🚀 Start scanning
print("\n✅ Permission confirmed. Starting scan...\n")

# 🔧 Run selected scan
if scan_type == "basic":
    print("[+] Running basic scan...")
    basic_result = run_basic_scan(target)
elif scan_type == "full":
    print("[+] Running full scan...")
    basic_result = run_full_scan(target)
elif scan_type == "stealth":
    print("[+] Running stealth scan...")
    basic_result = run_stealth_scan(target)
else:
    print("❌ Invalid scan type. Defaulting to basic scan.")
    basic_result = run_basic_scan(target)

# 🔧 Run service and vulnerability scans
print("[+] Running service scan...")
service_result = run_service_scan(target)

print("[+] Running vulnerability scan...")
vuln_result = run_vuln_scan(target)

# 💾 Save results
save_output(target, {
    "Basic Scan": basic_result,
    "Service Scan": service_result,
    "Vulnerability Scan": vuln_result
})

print("\n✅ Scan complete. Results saved in results/scan_logs.txt")
