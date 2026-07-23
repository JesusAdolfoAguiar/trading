#!/usr/bin/env python3
import subprocess
import sys

def fix_mtu():
    print("Adjusting eth0 MTU to 1400 to prevent WSL2 packet fragmentation...")
    try:
        # Assumes the environment runs as root (typical for WSL2); no sudo needed.
        # If not root, prefix with sudo or run the command manually.
        subprocess.run(["ip", "link", "set", "dev", "eth0", "mtu", "1400"], check=True)
        print("MTU successfully updated. Network TLS handshake should now work.")
    except subprocess.CalledProcessError as e:
        print(f"CRITICAL: Failed to set MTU. Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    fix_mtu()