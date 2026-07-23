#!/usr/bin/env python3

import os
import sys
import subprocess

def run_command(command, capture_output=True):
    """Executes a shell command and returns the subprocess object."""
    try:
        # shell=True is generally discouraged for security, but necessary 
        # here to mirror the exact behavior of the bash script's pipeline.
        return subprocess.run(command, shell=True, text=True, capture_output=capture_output, check=False)
    except Exception as e:
        print(f"Subprocess execution failed: {e}")
        sys.exit(1)

def main():
    cwd = os.getcwd()

    # 1. Directory & Remote Validation (generic: derive the expected remote
    #    slug from the working-directory basename, then require the configured
    #    remote to reference it). This removes hardcoded repo names — any repo
    #    whose directory basename matches its remote name is validated.
    expected = os.path.basename(cwd.rstrip("/"))
    if not expected:
        print(f"Could not derive a repository slug from CWD: {cwd}")
        sys.exit(1)

    remote_check = run_command("git remote -v")
    if expected not in remote_check.stdout:
        print(f"CRITICAL: Remote mismatch! Expected remote referencing '{expected}' for CWD {cwd}")
        sys.exit(1)

    # 2. Branch Security Check
    branch_check = run_command("git rev-parse --abbrev-ref HEAD")
    branch = branch_check.stdout.strip()
    
    if branch == "main":
        print("Error: Cannot work on main. Please create a feature branch.")
        sys.exit(1)

    # 3. Quality Control (Linting)
    if os.path.isfile("package.json"):
        print("Running lint check...")
        # capture_output=False streams the npm logs directly to the terminal/agent
        lint_check = run_command("npm run lint", capture_output=False)
        
        if lint_check.returncode != 0:
            print("Linting failed! Please fix errors before proceeding.")
            sys.exit(1)

    # 4. Success Output for Agent
    print("Security and Linting checks PASSED.")

if __name__ == "__main__":
    main()