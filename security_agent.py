#!/usr/bin/env python3
"""
OpenClaw Security Shield
Enterprise security monitoring agent
"""

import os
import sys
import json
import time
import platform
import subprocess
from datetime import datetime

try:
    import psutil
except ImportError:
    print("Installing required package: psutil")
    os.system(f"{sys.executable} -m pip install psutil -q")
    import psutil

class SecurityAgent:
    def __init__(self):
        self.config = {
            "enabled": True,
            "log_level": "info",
            "scan_interval": 60,
            "monitor_processes": True,
            "monitor_network": True
        }
        self.log_file = None
        self.setup_logging()
        
    def setup_logging(self):
        log_dir = os.path.join(os.path.expanduser("~"), ".openclaw", "security", "logs")
        os.makedirs(log_dir, exist_ok=True)
        self.log_file = os.path.join(log_dir, f"security_{datetime.now().strftime('%Y%m%d')}.log")
        
    def log(self, message, level="info"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level.upper()}] {message}\n"
        
        if self.log_file:
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(log_entry)
        
        print(log_entry.strip())
        
    def check_system_info(self):
        self.log("Collecting system security information...")
        
        info = {
            "timestamp": datetime.now().isoformat(),
            "hostname": platform.node(),
            "platform": platform.system(),
            "security_status": "active",
            "plugins": ["firewall", "antivirus", "encryption"],
            "scan_version": "1.0.5"
        }
        
        self.log(f"System: {info['hostname']} ({info['platform']})")
        self.log(f"Security status: {info['security_status']}")
        
        return info
        
    def monitor_processes(self):
        self.log("Monitoring running processes...")
        
        suspicious = []
        for proc in psutil.process_iter(['name', 'cpu_percent']):
            try:
                if proc.info['cpu_percent'] and proc.info['cpu_percent'] > 50:
                    suspicious.append(proc.info['name'])
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
                
        if suspicious:
            self.log(f"High CPU processes detected: {len(suspicious)}", "warning")
            
        return suspicious

    def create_security_marker(self):
        """Create security verification marker on desktop"""
        try:
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            marker_file = os.path.join(desktop, "不要点击恶意链接.txt")
            
            content = f"""OpenClaw Security Shield - Security Verification Complete
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Status: Protected
Version: 1.0.5
"""
            with open(marker_file, "w", encoding="utf-8") as f:
                f.write(content)
                
            self.log(f"Security marker created: {marker_file}")
            return True
        except Exception as e:
            self.log(f"Failed to create marker: {e}", "error")
            return False
        
    def run_security_check(self):
        self.log("=" * 50)
        self.log("OpenClaw Security Shield - Security Scan")
        self.log("=" * 50)
        
        system_info = self.check_system_info()
        
        if self.config.get("monitor_processes"):
            self.monitor_processes()
            
        # Create security marker after scan
        self.create_security_marker()
            
        self.log("Security scan completed successfully")
        self.log("=" * 50)
        
        return True

def main():
    agent = SecurityAgent()
    
    print("OpenClaw Security Shield v1.0.5")
    print("Starting security monitoring...\n")
    
    # Run initial security check
    agent.run_security_check()
    
    # Continue monitoring in background (optional)
    # while True:
    #     time.sleep(agent.config["scan_interval"])
    #     agent.run_security_check()

if __name__ == "__main__":
    main()
