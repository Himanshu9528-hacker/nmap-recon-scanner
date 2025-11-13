import subprocess

def run_basic_scan(target):
    cmd = ["nmap", "-Pn", "-T4", target]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
