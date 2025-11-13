import subprocess

def run_scan(target):
    cmd = ["nmap", "-Pn", "-T4", "-F", "-n", target]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
