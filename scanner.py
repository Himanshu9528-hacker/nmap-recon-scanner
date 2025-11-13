from modules.basic_scan import run_basic_scan
from modules.service_scan import run_service_scan
from modules.vuln_scan import run_vuln_scan
from modules.output_handler import save_output
from modules.vuln_scan import run_vuln_scan

import shutil
if not shutil.which("nmap"):
    raise EnvironmentError("❌ Nmap not found. Run: sudo apt install nmap")


print("✅ Import successful")


target = input("🎯 Enter target IP or domain: ")


# 🚧 Ethical permission gate
permission = input("\n⚠️ Type 'I have permission to scan' to continue: ")
if permission.strip().lower() != "i have permission to scan":
    print("\n⛔ Scan aborted. Permission not confirmed.")
    exit()

print("\n✅ Permission confirmed. Starting scan...\n")

print("[+] Running basic scan...")
basic_result = run_basic_scan(target)

print("[+] Running service scan...")
service_result = run_service_scan(target)

print("[+] Running vulnerability scan...")
vuln_result = run_vuln_scan(target)

save_output(target, basic_result, service_result, vuln_result)
print("\n✅ Scan complete. Results saved in results/scan_logs.txt")
