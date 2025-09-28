# Daily Commit Automation

An automated Python script that makes realistic daily commits to a GitHub repository with random variations.

## Features

- 🤖 **Automated Commits**: Makes daily commits when your PC starts up
- 🎲 **Random Variations**: Updates different files with varied content
- 📝 **Realistic Content**: Adds timestamps, emojis, activities, and random text
- 🔧 **Error Handling**: Gracefully handles network issues and git errors
- 📊 **Progress Tracking**: Maintains JSON and Markdown logs
- ⚙️ **Easy Configuration**: Simple setup with clear configuration section

## Quick Start

1. **Clone or download** this repository to your desired location
2. **Configure** the script by editing the configuration section in `daily_commit_automation.py`:
   ```python
   REPO_PATH = "https://github.com/lethimcode456/daily_log.git"  # Your repository path
   GIT_BRANCH = "main"          # Your branch name
   FILES_TO_UPDATE = [          # Files to update
       "daily_log.md",
       "README.md", 
       "progress.json",
       "notes.txt",
       "activities.md"
   ]
   ```

3. **Initialize** your git repository:
   ```bash
   git init
   git remote add origin https://github.com/lethimcode456/daily_log.git
   git add .
   git commit -m "Initial commit"
   git push -u origin main
   ```

4. **Test** the script:
   ```bash
   python daily_commit_automation.py
   ```

5. **Set up automation** (see instructions below)

## File Types Supported

- **Markdown (.md)**: Headers, lists, timestamps, emojis
- **JSON (.json)**: Structured progress tracking with timestamps
- **Text (.txt)**: Simple timestamped notes
- **Generic**: Basic content for any file type

## Configuration Options

### Commit Messages
The script uses realistic commit message patterns:
- "Daily update: 2024-01-15"
- "Progress log for 2024-01-15"
- "Update: code review - 2024-01-15"
- "Daily commit: 🚀 2024-01-15"

### Activities
Random activities for realistic commits:
- code review, bug fixes, feature development
- documentation, testing, refactoring
- optimization, research, planning, etc.

### Content Variations
- Random emojis and text snippets
- Timestamps and dates
- Different file types and formats
- Realistic commit patterns

## Automation Setup

### Windows
**Method 1: Task Scheduler**
1. Open Task Scheduler (`taskschd.msc`)
2. Create Basic Task → "Daily Commit Automation"
3. Trigger: "When the computer starts"
4. Action: Start a program
5. Program: `python.exe`
6. Arguments: `"E:\daily_log\daily_commit_automation.py"`

**Method 2: Startup Folder**
1. Press `Win+R`, type `shell:startup`
2. Create `daily_commit.bat`:
   ```batch
   @echo off
   cd /d E:\daily_log
   python daily_commit_automation.py
   ```

### macOS
1. Open System Preferences → Users & Groups → Login Items
2. Create `daily_commit.command`:
   ```bash
   #!/bin/bash
   cd /path/to/your/repo
   python3 daily_commit_automation.py
   ```
3. Make executable: `chmod +x daily_commit.command`

### Linux
**Systemd Service:**
```bash
sudo nano /etc/systemd/system/daily-commit.service
```
```ini
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
```
```bash
sudo systemctl enable daily-commit.service
sudo systemctl start daily-commit.service
```

**Cron Alternative:**
```bash
crontab -e
# Add: @reboot cd /path/to/your/repo && python3 daily_commit_automation.py
```

## Requirements

- Python 3.6+
- Git installed and configured
- GitHub repository with SSH keys or personal access token
- Files listed in `FILES_TO_UPDATE` must exist in your repository

## Troubleshooting

1. **Check logs**: Review `daily_commit.log` for detailed information
2. **Git configuration**: Ensure `user.name` and `user.email` are set
3. **Repository access**: Verify SSH keys or personal access token
4. **Test manually**: Run the script manually before setting up automation
5. **File permissions**: Ensure the script has write access to the repository

## Customization

### Adding New File Types
Extend the `generate_*_content()` methods to support new file types.

### Custom Commit Messages
Modify the `COMMIT_MESSAGES` list with your preferred patterns.

### Different Activities
Update the `ACTIVITIES` list with activities relevant to your project.

### File Selection
Adjust `MAX_FILES_PER_DAY` to control how many files are updated per day.

## Ethical Considerations

This script is designed for legitimate automation purposes:
- ✅ Personal project tracking
- ✅ Learning and experimentation
- ✅ Automated documentation
- ❌ Spam or artificial activity
- ❌ Violating GitHub terms of service

## License

This project is open source and available under the MIT License.

---

*This README will be automatically updated by the daily commit script.*

"# daily_log" 
