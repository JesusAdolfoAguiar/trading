#!/usr/bin/env python3
import os
import sys
import subprocess
from datetime import datetime, timedelta

# 1. Init: Use passed date or default to today
date_str = sys.argv[1] if len(sys.argv) > 1 else datetime.today().strftime('%Y-%m-%d')
base_dir = os.path.expanduser("~/personal/trading")

def get_week_folder(d_str):
    try:
        d = datetime.strptime(d_str, '%Y-%m-%d')
    except ValueError:
        return d_str
    mon = d - timedelta(days=d.weekday())
    fri = mon + timedelta(days=4)
    mon_month = mon.strftime('%B').lower()
    fri_month = fri.strftime('%B').lower()
    if mon_month == fri_month:
        return f"{mon_month} {mon.day}-{fri.day}"
    else:
        return f"{mon_month} {mon.day}-{fri_month} {fri.day}"

week_folder = get_week_folder(date_str)
raw_dir = os.path.join(base_dir, f"journals/raw/{week_folder}")
raw_file = os.path.join(raw_dir, "weekly-raw.md")

# 2. Scaffold
os.chdir(base_dir)
os.makedirs(raw_dir, exist_ok=True)

if not os.path.exists(raw_file):
    with open(raw_file, 'w') as f:
        f.write(f"# Weekly Raw Notes: {week_folder}\n\n")
        f.write("## Brain Dump\n")
        f.write("[Write your subjective feelings about the week here...]\n\n")
        f.write("## Daily Links\n")
        f.write("* Monday: \n")
        f.write("* Tuesday: \n")
        f.write("* Wednesday: \n")
        f.write("* Thursday: \n")
        f.write("* Friday: \n")

# 3. Open UI Hooks
print(f"📝 Opening VS Code: {raw_file}")
subprocess.run(['code', raw_file])

# 4. The Gate
print("\n" + "="*50)
input(f"⏸️  PAUSED: Fill out your brain dump and daily links in VS Code.\n   Press [ENTER] when {week_folder} is ready to process...")
print("="*50 + "\n")

print("✅ Data verified. Handing off to Agent...")

# 5. Execute Engine
try:
    subprocess.run(["antigravity", "--skill", "weekly-review", f"Process weekly review for week: {week_folder}"], check=True)
    print("\n🏁 Pipeline complete.")
except (FileNotFoundError, PermissionError):
    print("\n⚠️ 'antigravity' command not found in PATH. Run the agent step manually.")
    sys.exit(1)
except subprocess.CalledProcessError as e:
    print(f"\n❌ Agent execution failed with error code {e.returncode}")
    sys.exit(1)
