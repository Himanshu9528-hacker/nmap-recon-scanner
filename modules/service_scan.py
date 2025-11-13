import subprocess

def run_service_scan(target):
    cmd = ["nmap", "-sV", "--version-intensity", "5", target]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
