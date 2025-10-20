# Daily Commit Bot

A simple Python script that automatically commits to your GitHub repo every day. Perfect for maintaining consistent activity on your profile.

## What it does

- Picks random files from your repo and adds small updates
- Creates realistic commit messages with timestamps
- Runs automatically when you start your computer
- Keeps your GitHub activity graph green without any manual work

## Prerequisites

Before you start, make sure you have:

- Python 3.6 or newer
- Git installed and configured (`git config --global user.name "Your Name"`)
- A GitHub repository (can be private)
- Either SSH keys set up OR a personal access token configured

## Setup

1. **Clone or download this script** to your computer

2. **Edit the configuration** at the top of `daily_commit_automation.py`:
   ```python
   REPO_PATH = "C:/path/to/your/repo"  # Change this to your repo path
   ```

3. **Create the files** that the script will update (in your repo folder):
   ```bash
   touch daily_log.md progress.json notes.txt README.md
   ```

4. **Test it works**:
   ```bash
   python daily_commit_automation.py
   ```
   You should see "Success! Updated: filename" if everything works.

## Automation (Run on Startup)

Pick your operating system:

### Windows
1. Press `Win + R`, type `shell:startup`, hit Enter
2. Create a new file called `daily_commit.bat` with this content:
   ```batch
   @echo off
   cd /d "C:\path\to\your\repo"
   python daily_commit_automation.py
   ```
   (Change the path to match your setup)

### Mac
1. Open `Automator` → New Document → Application
2. Add "Run Shell Script" action with:
   ```bash
   cd /path/to/your/repo
   python3 daily_commit_automation.py
   ```
3. Save as an Application
4. Add it to System Preferences → Users & Groups → Login Items

### Linux
Add this line to your crontab (`crontab -e`):
```bash
@reboot cd /path/to/your/repo && python3 daily_commit_automation.py
```

## Customization

Want to change things up? Edit these in the script:

- **Files to update**: Modify `FILES_CONFIG` dictionary
- **Commit messages**: Change `COMMIT_TEMPLATES` list  
- **Activities**: Update `ACTIVITIES` list with your preferred terms

## GitHub Repository Setup

If you need a new repo for this, here's the copy-paste setup:

```bash
# Create new repo directory
mkdir daily_log
cd daily_log

# Initialize git
git init
git branch -M main

# Create initial files
echo "# Daily Activity Log" > README.md
echo "{}" > progress.json
echo "# Daily Log" > daily_log.md
echo "Notes file" > notes.txt

# Add files and make first commit
git add .
git commit -m "Initial setup for daily automation"

# Connect to GitHub (create repo on GitHub first)
git remote add origin https://github.com/USERNAME/daily_log.git
git push -u origin main
```

## Troubleshooting

**Script fails to run?**
- Check that Python and Git are in your PATH
- Make sure your GitHub authentication is working (`git push` manually)
- Verify the `REPO_PATH` is correct

**No commits appearing?**
- Check if the files exist in your repo
- Look for error messages when running the script manually
- Ensure your GitHub credentials haven't expired

**Want to see what happened?**
- The script prints status messages when you run it manually
- Check your repository's commit history on GitHub

---

That's it! Set it up once and forget about it. Your GitHub activity will stay consistent without any effort from you.

- 🔥 Progress update
- research completed at 17:34

## October 01 Update
### Wednesday Notes

- bug fixes completed at 18:31
## October 01 Update

- 🚀 Progress update
### Wednesday Notes

### Thursday Notes
- 🔧 Progress update

- ✨ Progress update
- refactoring completed at 14:22

- 🔧 Progress update
- bug fixes completed at 17:42

### Tuesday Notes
## October 07 Update

### Tuesday Notes
- cleanup completed at 00:35

- cleanup completed at 17:12
### Thursday Notes

### Friday Notes
- learning completed at 17:51

### Saturday Notes
- learning completed at 19:33

## October 12 Update
- learning completed at 10:47

## October 20 Update
- 🔥 Progress update
