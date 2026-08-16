import os
import shutil
from datetime import datetime, timedelta

base_dir = os.path.expanduser("~/personal/trading")

def get_week_folder(d_str):
    try:
        d = datetime.strptime(d_str, '%Y-%m-%d')
    except ValueError:
        return None
    mon = d - timedelta(days=d.weekday())
    fri = mon + timedelta(days=4)
    mon_month = mon.strftime('%B').lower()
    fri_month = fri.strftime('%B').lower()
    if mon_month == fri_month:
        return f"{mon_month} {mon.day}-{fri.day}"
    else:
        return f"{mon_month} {mon.day}-{fri_month} {fri.day}"

def process_dir(target_dir, is_screenshot=False):
    if not os.path.exists(target_dir):
        return
    for item in os.listdir(target_dir):
        item_path = os.path.join(target_dir, item)
        
        # Skip if it's already a week folder or legacy file
        if is_screenshot and not os.path.isdir(item_path):
            continue
        
        # Extract date string
        if is_screenshot:
            date_str = item
        else:
            if item.endswith('-p.md'):
                date_str = item.replace('-p.md', '')
            elif item.endswith('-raw.md'):
                date_str = item.replace('-raw.md', '')
            elif item.endswith('.md'):
                date_str = item.replace('.md', '')
            else:
                continue

        # Ignore non-date formatted files like legacy-untagged.md
        week_folder = get_week_folder(date_str)
        if not week_folder:
            continue

        week_dir = os.path.join(target_dir, week_folder)
        os.makedirs(week_dir, exist_ok=True)
        
        dest_path = os.path.join(week_dir, item)
        if item_path != dest_path:
            print(f"Moving {item_path} -> {dest_path}")
            shutil.move(item_path, dest_path)

print("Organizing raw...")
process_dir(os.path.join(base_dir, "journals/raw"))

print("Organizing processed...")
process_dir(os.path.join(base_dir, "journals/processed"))

print("Organizing screenshots...")
process_dir(os.path.join(base_dir, "journals/screenshots"), is_screenshot=True)

print("Done.")
