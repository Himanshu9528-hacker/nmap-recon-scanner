import subprocess

def run_basic_scan(target):
    # 🔧 Default scan flags — fast, stealthy, and no ping
    cmd = ["nmap", "-Pn", "-T4", "-F", "-n", target]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"❌ Scan failed: {str(e)}"
