import subprocess

def run_vuln_scan(target):
    cmd = ["nmap", "--script", "vuln", target]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
