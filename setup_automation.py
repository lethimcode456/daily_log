#!/usr/bin/env python3
"""
Setup Script for Daily Commit Automation
========================================

This script helps set up the daily commit automation on different operating systems.
It provides interactive setup options and creates necessary configuration files.

Author: AI Assistant
Version: 1.0
"""

import os
import sys
import platform
import subprocess
from pathlib import Path

def detect_os():
    """Detect the operating system"""
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "darwin":
        return "macos"
    elif system == "linux":
        return "linux"
    else:
        return "unknown"

def create_windows_batch_file(repo_path, python_path):
    """Create Windows batch file for startup"""
    batch_content = f"""@echo off
cd /d "{repo_path}"
"{python_path}" daily_commit_automation.py
pause
"""
    
    batch_file = Path(repo_path) / "daily_commit.bat"
    with open(batch_file, 'w') as f:
        f.write(batch_content)
    
    print(f"✅ Created Windows batch file: {batch_file}")
    print("To set up automatic startup:")
    print("1. Press Win+R, type 'shell:startup'")
    print("2. Copy the batch file to the startup folder")
    print("3. Or use Task Scheduler for more advanced options")

def create_macos_command_file(repo_path, python_path):
    """Create macOS command file for startup"""
    command_content = f"""#!/bin/bash
cd "{repo_path}"
{python_path} daily_commit_automation.py
"""
    
    command_file = Path(repo_path) / "daily_commit.command"
    with open(command_file, 'w') as f:
        f.write(command_content)
    
    # Make executable
    os.chmod(command_file, 0o755)
    
    print(f"✅ Created macOS command file: {command_file}")
    print("To set up automatic startup:")
    print("1. Open System Preferences > Users & Groups > Login Items")
    print("2. Add the .command file to login items")

def create_linux_systemd_service(repo_path, python_path, username):
    """Create Linux systemd service file"""
    service_content = f"""[Unit]
Description=Daily Commit Automation
After=network.target

[Service]
Type=simple
User={username}
WorkingDirectory={repo_path}
ExecStart={python_path} daily_commit_automation.py
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
"""
    
    service_file = Path(repo_path) / "daily-commit.service"
    with open(service_file, 'w') as f:
        f.write(service_content)
    
    print(f"✅ Created systemd service file: {service_file}")
    print("To set up automatic startup:")
    print("1. Copy the service file: sudo cp daily-commit.service /etc/systemd/system/")
    print("2. Enable the service: sudo systemctl enable daily-commit.service")
    print("3. Start the service: sudo systemctl start daily-commit.service")

def create_cron_setup(repo_path, python_path):
    """Create cron setup instructions"""
    cron_command = f"@reboot cd {repo_path} && {python_path} daily_commit_automation.py"
    
    cron_file = Path(repo_path) / "cron_setup.txt"
    with open(cron_file, 'w') as f:
        f.write(f"""Cron Setup Instructions
=====================

To set up automatic startup with cron:

1. Open crontab: crontab -e
2. Add this line:
   {cron_command}
3. Save and exit

Alternative: Add to system crontab:
1. Edit: sudo nano /etc/crontab
2. Add: {cron_command}
""")
    
    print(f"✅ Created cron setup file: {cron_file}")

def check_git_setup(repo_path):
    """Check if git is properly set up"""
    try:
        # Check if it's a git repository
        result = subprocess.run(['git', 'status'], cwd=repo_path, 
                              capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Not a git repository. Please initialize git first:")
            print(f"   cd {repo_path}")
            print("   git init")
            print("   git remote add origin <your-repo-url>")
            return False
        
        # Check for remote
        result = subprocess.run(['git', 'remote', '-v'], cwd=repo_path,
                              capture_output=True, text=True)
        if not result.stdout.strip():
            print("⚠️  No remote repository configured.")
            print("   Add a remote: git remote add origin <your-repo-url>")
        
        print("✅ Git repository looks good")
        return True
        
    except FileNotFoundError:
        print("❌ Git not found. Please install git first.")
        return False

def main():
    """Main setup function"""
    print("Daily Commit Automation Setup")
    print("=" * 40)
    
    # Get current directory
    repo_path = os.getcwd()
    print(f"Repository path: {repo_path}")
    
    # Check Python path
    python_path = sys.executable
    print(f"Python path: {python_path}")
    
    # Check git setup
    if not check_git_setup(repo_path):
        print("\nPlease set up git first, then run this script again.")
        return
    
    # Detect OS and create appropriate setup files
    os_type = detect_os()
    print(f"\nDetected OS: {os_type}")
    
    if os_type == "windows":
        create_windows_batch_file(repo_path, python_path)
        
    elif os_type == "macos":
        create_macos_command_file(repo_path, python_path)
        
    elif os_type == "linux":
        # Get username for systemd service
        username = os.getenv('USER', 'root')
        create_linux_systemd_service(repo_path, python_path, username)
        create_cron_setup(repo_path, python_path)
        
    else:
        print("Unknown operating system. Please set up automation manually.")
        print("See the README.md for instructions.")
    
    print("\n" + "=" * 40)
    print("Setup complete! Next steps:")
    print("1. Test the script: python daily_commit_automation.py")
    print("2. Follow the OS-specific instructions above")
    print("3. Check daily_commit.log for any issues")

if __name__ == "__main__":
    main()

