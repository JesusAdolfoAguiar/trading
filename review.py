#!/usr/bin/env python3
import os
import sys
import subprocess
from datetime import datetime, timedelta

# 1. Init: Use passed date or default to today
date_str = sys.argv[1] if len(sys.argv) > 1 else datetime.today().strftime('%Y-%m-%d')
base_dir = os.path.expanduser("~/personal/trading")

# 2. Paths
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

ss_dir = os.path.join(base_dir, f"journals/screenshots/{week_folder}/{date_str}")
raw_file = os.path.join(base_dir, f"journals/raw/{week_folder}/{date_str}-raw.md")
if not os.path.exists(raw_file):
    alt_raw_file = os.path.join(base_dir, f"journals/raw/{week_folder}/{date_str}.md")
    if os.path.exists(alt_raw_file):
        raw_file = alt_raw_file

# 3. Scaffold
os.chdir(base_dir)
os.makedirs(ss_dir, exist_ok=True)
os.makedirs(os.path.dirname(raw_file), exist_ok=True)

if not os.path.exists(raw_file):
    with open(raw_file, 'w') as f:
        f.write(f"# Raw Notes: {date_str}\n\n")

# WSL -> Windows Path Converter
def wsl_to_win_path(wsl_path):
    result = subprocess.run(['wslpath', '-w', wsl_path], capture_output=True, text=True)
    return result.stdout.strip()

win_ss_dir = wsl_to_win_path(ss_dir)

# 4. Open UI Hooks
print(f"📁 Opening Explorer: {win_ss_dir}")
subprocess.run(['explorer.exe', win_ss_dir])

print(f"📝 Opening VS Code: {raw_file}")
subprocess.run(['code', raw_file])

# 5. The Gate
print("\n" + "="*50)
input(f"⏸️  PAUSED: Paste your screenshots into Explorer and notes into VS Code.\n   Press [ENTER] when {date_str} is ready to process...")
print("="*50 + "\n")

# 6. Validation
if not os.listdir(ss_dir):
    print(f"❌ Error: No screenshots found in {ss_dir}. Aborting.")
    sys.exit(1)

if os.path.getsize(raw_file) < 25: 
    print(f"❌ Error: Raw file {raw_file} appears empty. Aborting.")
    sys.exit(1)

print("✅ Data verified. Handing off to Agent...")

# 7. Execute Engine
try:
    # Invokes your Antigravity agent CLI. Adjust arguments if your CLI syntax differs.
    subprocess.run(["agy", "--skill", "trade-review", "--date", date_str], check=True)
    print("\n🏁 Pipeline complete.")
except (FileNotFoundError, PermissionError):
    print("\n⚠️ 'agy' command not found in PATH. Run the agent step manually.")
    sys.exit(1)
except subprocess.CalledProcessError as e:
    print(f"\n❌ Agent execution failed with error code {e.returncode}")
    sys.exit(1)