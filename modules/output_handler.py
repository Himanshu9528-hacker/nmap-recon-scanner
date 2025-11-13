def save_output(target, basic, service, vuln):
    with open("results/scan_logs.txt", "a") as f:
        f.write(f"\n=== Scan for {target} ===\n")
        f.write("\n--- Basic Scan ---\n" + basic)
        f.write("\n--- Service Scan ---\n" + service)
        f.write("\n--- Vulnerability Scan ---\n" + vuln)
        f.write("\n=============================\n")
