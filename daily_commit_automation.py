#!/usr/bin/env python3
"""
Daily Commit Automation Script
==============================

This script automatically makes daily commits to a GitHub repository with realistic variations.
It updates files randomly, adds varied content, and handles git operations automatically.

Author: AI Assistant
Version: 1.0
"""

import os
import sys
import random
import json
import subprocess
import datetime
from pathlib import Path
from typing import List, Dict, Optional
import logging

# =============================================================================
# CONFIGURATION SECTION - MODIFY THESE VALUES
# =============================================================================

# Repository configuration
REPO_PATH = r"E:\daily_log"  # Path to your local git repository
GIT_BRANCH = "main"  # Branch to commit to
REMOTE_NAME = "origin"  # Remote repository name

# Files to update (relative to REPO_PATH)
FILES_TO_UPDATE = [
    "daily_log.md",
    "README.md", 
    "progress.json",
    "notes.txt",
    "activities.md"
]

# Commit message patterns with placeholders
COMMIT_MESSAGES = [
    "Daily update: {date}",
    "Progress log for {date}",
    "Update: {activity} - {date}",
    "Daily commit: {random_emoji} {date}",
    "Log entry: {timestamp}",
    "Daily sync: {file_updated}",
    "Update {file_updated}: {random_text}",
    "Daily progress: {activity}",
    "Commit: {random_emoji} {activity}",
    "Update: {random_text} - {date}"
]

# Activities for realistic commit messages
ACTIVITIES = [
    "code review", "bug fixes", "feature development", "documentation", 
    "testing", "refactoring", "optimization", "research", "planning",
    "debugging", "cleanup", "maintenance", "learning", "experimentation"
]

# Random text snippets for file updates
RANDOM_TEXTS = [
    "Quick update", "Minor changes", "Small improvement", "Tiny fix",
    "Quick note", "Brief update", "Small addition", "Minor tweak",
    "Quick edit", "Small change", "Brief note", "Minor update"
]

# Emojis for variation
EMOJIS = ["🚀", "✨", "📝", "🔧", "💡", "🎯", "⚡", "🔥", "💪", "🎉", "📚", "🛠️"]

# =============================================================================
# SCRIPT CONFIGURATION
# =============================================================================

# Logging configuration
LOG_LEVEL = logging.INFO
LOG_FILE = "daily_commit.log"

# Maximum number of files to update per day
MAX_FILES_PER_DAY = 3

# Minimum and maximum lines to add to files
MIN_LINES_TO_ADD = 1
MAX_LINES_TO_ADD = 5

# =============================================================================
# MAIN SCRIPT CLASS
# =============================================================================

class DailyCommitAutomation:
    def __init__(self, repo_path: str):
        self.repo_path = Path(repo_path)
        self.setup_logging()
        self.ensure_repo_exists()
        
    def setup_logging(self):
        """Setup logging configuration"""
        logging.basicConfig(
            level=LOG_LEVEL,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(LOG_FILE),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)
        
    def ensure_repo_exists(self):
        """Ensure the repository path exists and is a git repository"""
        if not self.repo_path.exists():
            self.logger.error(f"Repository path does not exist: {self.repo_path}")
            sys.exit(1)
            
        if not (self.repo_path / ".git").exists():
            self.logger.error(f"Not a git repository: {self.repo_path}")
            sys.exit(1)
            
        self.logger.info(f"Repository validated: {self.repo_path}")
        
    def run_git_command(self, command: List[str], cwd: Optional[Path] = None) -> bool:
        """Run a git command and return success status"""
        try:
            result = subprocess.run(
                command, 
                cwd=cwd or self.repo_path,
                capture_output=True, 
                text=True, 
                check=True
            )
            self.logger.debug(f"Git command successful: {' '.join(command)}")
            return True
        except subprocess.CalledProcessError as e:
            self.logger.error(f"Git command failed: {' '.join(command)}")
            self.logger.error(f"Error: {e.stderr}")
            return False
            
    def get_random_commit_message(self, file_updated: str) -> str:
        """Generate a random commit message"""
        template = random.choice(COMMIT_MESSAGES)
        now = datetime.datetime.now()
        
        replacements = {
            '{date}': now.strftime('%Y-%m-%d'),
            '{timestamp}': now.strftime('%Y-%m-%d %H:%M:%S'),
            '{activity}': random.choice(ACTIVITIES),
            '{file_updated}': file_updated,
            '{random_emoji}': random.choice(EMOJIS),
            '{random_text}': random.choice(RANDOM_TEXTS)
        }
        
        message = template
        for placeholder, value in replacements.items():
            message = message.replace(placeholder, value)
            
        return message
        
    def create_or_update_file(self, file_path: Path) -> bool:
        """Create or update a file with random content"""
        try:
            # Determine file type and content
            if file_path.suffix == '.md':
                content = self.generate_markdown_content()
            elif file_path.suffix == '.json':
                content = self.generate_json_content()
            elif file_path.suffix == '.txt':
                content = self.generate_text_content()
            else:
                content = self.generate_generic_content()
                
            # Read existing content if file exists
            existing_content = ""
            if file_path.exists():
                with open(file_path, 'r', encoding='utf-8') as f:
                    existing_content = f.read()
                    
            # Append new content
            with open(file_path, 'a', encoding='utf-8') as f:
                if existing_content and not existing_content.endswith('\n'):
                    f.write('\n')
                f.write(content)
                
            self.logger.info(f"Updated file: {file_path.name}")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to update file {file_path}: {e}")
            return False
            
    def generate_markdown_content(self) -> str:
        """Generate markdown content"""
        now = datetime.datetime.now()
        lines = []
        
        # Add random number of lines
        num_lines = random.randint(MIN_LINES_TO_ADD, MAX_LINES_TO_ADD)
        
        for _ in range(num_lines):
            line_type = random.choice(['header', 'text', 'list', 'emoji'])
            
            if line_type == 'header':
                level = random.choice(['##', '###'])
                text = random.choice([
                    f"Update {now.strftime('%Y-%m-%d')}",
                    f"Daily Progress - {now.strftime('%B %d')}",
                    f"Quick Update {random.choice(EMOJIS)}",
                    f"Notes for {now.strftime('%A')}"
                ])
                lines.append(f"{level} {text}")
                
            elif line_type == 'text':
                text = random.choice([
                    f"- {random.choice(RANDOM_TEXTS)} at {now.strftime('%H:%M')}",
                    f"- {random.choice(ACTIVITIES)} in progress",
                    f"- {random.choice(EMOJIS)} {random.choice(RANDOM_TEXTS)}",
                    f"- Daily update: {now.strftime('%Y-%m-%d %H:%M')}"
                ])
                lines.append(text)
                
            elif line_type == 'list':
                lines.append(f"- {random.choice(ACTIVITIES)}")
                
            elif line_type == 'emoji':
                lines.append(f"{random.choice(EMOJIS)} {random.choice(RANDOM_TEXTS)}")
                
        return '\n'.join(lines) + '\n'
        
    def generate_json_content(self) -> str:
        """Generate JSON content for progress tracking"""
        now = datetime.datetime.now()
        
        # Try to read existing JSON
        existing_data = {}
        if self.repo_path.joinpath('progress.json').exists():
            try:
                with open(self.repo_path.joinpath('progress.json'), 'r') as f:
                    existing_data = json.load(f)
            except:
                existing_data = {}
                
        # Add new entry
        date_str = now.strftime('%Y-%m-%d')
        if 'daily_updates' not in existing_data:
            existing_data['daily_updates'] = {}
            
        existing_data['daily_updates'][date_str] = {
            'timestamp': now.isoformat(),
            'activity': random.choice(ACTIVITIES),
            'status': random.choice(['in_progress', 'completed', 'planned']),
            'notes': random.choice(RANDOM_TEXTS),
            'emoji': random.choice(EMOJIS)
        }
        
        # Update last_modified
        existing_data['last_modified'] = now.isoformat()
        existing_data['total_entries'] = len(existing_data['daily_updates'])
        
        return json.dumps(existing_data, indent=2)
        
    def generate_text_content(self) -> str:
        """Generate plain text content"""
        now = datetime.datetime.now()
        lines = []
        
        num_lines = random.randint(MIN_LINES_TO_ADD, MAX_LINES_TO_ADD)
        for _ in range(num_lines):
            line = f"[{now.strftime('%Y-%m-%d %H:%M')}] {random.choice(RANDOM_TEXTS)} - {random.choice(ACTIVITIES)}"
            lines.append(line)
            
        return '\n'.join(lines) + '\n'
        
    def generate_generic_content(self) -> str:
        """Generate generic content for unknown file types"""
        now = datetime.datetime.now()
        return f"# Update {now.strftime('%Y-%m-%d %H:%M')}\n{random.choice(RANDOM_TEXTS)}\n"
        
    def check_for_changes(self) -> bool:
        """Check if there are any uncommitted changes"""
        result = subprocess.run(
            ['git', 'status', '--porcelain'],
            cwd=self.repo_path,
            capture_output=True,
            text=True
        )
        return bool(result.stdout.strip())
        
    def make_commit(self) -> bool:
        """Make a commit with all changes"""
        # Add all changes
        if not self.run_git_command(['git', 'add', '.']):
            return False
            
        # Check if there are changes to commit
        if not self.check_for_changes():
            self.logger.info("No changes to commit")
            return False
            
        # Generate commit message
        files_changed = subprocess.run(
            ['git', 'diff', '--cached', '--name-only'],
            cwd=self.repo_path,
            capture_output=True,
            text=True
        ).stdout.strip().split('\n')
        
        file_updated = files_changed[0] if files_changed else "files"
        commit_message = self.get_random_commit_message(file_updated)
        
        # Make commit
        if not self.run_git_command(['git', 'commit', '-m', commit_message]):
            return False
            
        self.logger.info(f"Committed: {commit_message}")
        return True
        
    def push_changes(self) -> bool:
        """Push changes to remote repository"""
        return self.run_git_command(['git', 'push', REMOTE_NAME, GIT_BRANCH])
        
    def run_daily_automation(self):
        """Main method to run the daily automation"""
        self.logger.info("Starting daily commit automation...")
        
        # Select random files to update
        files_to_update = random.sample(
            FILES_TO_UPDATE, 
            min(random.randint(1, MAX_FILES_PER_DAY), len(FILES_TO_UPDATE))
        )
        
        self.logger.info(f"Selected files to update: {files_to_update}")
        
        # Update selected files
        updated_files = []
        for file_name in files_to_update:
            file_path = self.repo_path / file_name
            if self.create_or_update_file(file_path):
                updated_files.append(file_name)
                
        if not updated_files:
            self.logger.warning("No files were updated")
            return False
            
        # Make commit
        if not self.make_commit():
            self.logger.error("Failed to make commit")
            return False
            
        # Push changes
        if not self.push_changes():
            self.logger.error("Failed to push changes")
            return False
            
        self.logger.info(f"Successfully completed daily automation. Updated: {updated_files}")
        return True

# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main function"""
    print("Daily Commit Automation Script")
    print("=" * 40)
    
    # Validate configuration
    if not os.path.exists(REPO_PATH):
        print(f"ERROR: Repository path does not exist: {REPO_PATH}")
        print("Please update REPO_PATH in the configuration section")
        sys.exit(1)
        
    # Run automation
    automation = DailyCommitAutomation(REPO_PATH)
    success = automation.run_daily_automation()
    
    if success:
        print("✅ Daily commit automation completed successfully!")
    else:
        print("❌ Daily commit automation failed. Check the logs for details.")
        sys.exit(1)

if __name__ == "__main__":
    main()

# =============================================================================
# STARTUP INSTRUCTIONS
# =============================================================================

"""
HOW TO RUN THIS SCRIPT AUTOMATICALLY ON STARTUP:

WINDOWS:
1. Open Task Scheduler (taskschd.msc)
2. Create Basic Task
3. Name: "Daily Commit Automation"
4. Trigger: "When the computer starts"
5. Action: "Start a program"
6. Program: python.exe
7. Arguments: "E:\daily_log\daily_commit_automation.py"
8. Start in: E:\daily_log

ALTERNATIVE WINDOWS METHOD:
1. Press Win+R, type "shell:startup"
2. Create a batch file (.bat) with:
   @echo off
   cd /d E:\daily_log
   python daily_commit_automation.py
3. Save as "daily_commit.bat" in the startup folder

MACOS:
1. Open System Preferences > Users & Groups > Login Items
2. Add the script or create a .command file:
   #!/bin/bash
   cd /path/to/your/repo
   python3 daily_commit_automation.py
3. Make executable: chmod +x daily_commit.command

LINUX:
1. Create a systemd service file:
   sudo nano /etc/systemd/system/daily-commit.service
2. Add:
   [Unit]
   Description=Daily Commit Automation
   After=network.target
   
   [Service]
   Type=simple
   User=yourusername
   WorkingDirectory=/path/to/your/repo
   ExecStart=/usr/bin/python3 daily_commit_automation.py
   Restart=on-failure
   
   [Install]
   WantedBy=multi-user.target
3. Enable: sudo systemctl enable daily-commit.service
4. Start: sudo systemctl start daily-commit.service

CRON ALTERNATIVE (Linux/macOS):
1. Edit crontab: crontab -e
2. Add: @reboot cd /path/to/your/repo && python3 daily_commit_automation.py

REQUIREMENTS:
- Python 3.6+
- Git installed and configured
- Repository must be initialized and have a remote origin
- SSH keys or personal access token configured for GitHub

CONFIGURATION:
- Update REPO_PATH to your repository location
- Modify FILES_TO_UPDATE list to include your desired files
- Adjust COMMIT_MESSAGES, ACTIVITIES, and other settings as needed
- Ensure your repository has the files listed in FILES_TO_UPDATE

TROUBLESHOOTING:
- Check daily_commit.log for detailed logs
- Ensure git is configured with user.name and user.email
- Verify remote repository access
- Test the script manually before setting up automation
"""

