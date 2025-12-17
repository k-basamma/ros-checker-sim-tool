import os
import subprocess
import re
import json

def run_validation(file_path):
    report = {"status": "Passed", "errors": [], "warnings": [], "components": []}
    
    # Syntax validation (flake8 for Python) [cite: 13]
    syntax = subprocess.run(['flake8', file_path], capture_output=True, text=True)
    if syntax.stdout:
        report["status"] = "Failed"
        report["errors"].append(f"Syntax Error: {syntax.stdout}")

    # Safety checks: joint values in safe range [cite: 16]
    with open(file_path, 'r') as f:
        content = f.read()
        matches = re.findall(r"\[([0-9.,\s-]+)\]", content)
        for match in matches:
            values = [float(x.strip()) for x in match.split(',') if x.strip()]
            if any(abs(v) > 3.14 for v in values):
                report["warnings"].append("Safety Warning: Joint value > 3.14 rad detected.")

    # ROS structure check: detect publishers/subscribers [cite: 14, 15]
    if "create_publisher" in content: report["components"].append("Publisher")
    if "create_subscription" in content: report["components"].append("Subscriber")

    return report
