import os
import subprocess
import sys


def run_git_command(command):
    """Helper function to run a system command and handle errors."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            text=True,
            capture_output=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing: {command}")
        print(f"Git said: {e.stderr.strip()}")
        sys.exit(1)


def git_upload():
    if not os.path.exists(".git"):
        print(
            "This directory is not a Git repository. Run 'git init' first!"
        )
        return

    print("Checking repository status...")

    print("➕ Staging changes...")
    run_git_command("git add .")

    commit_message = input("Enter your commit message: ").strip()

    if not commit_message:
        commit_message = "Automated backup via Python script"

    print(f" Committing changes with message: '{commit_message}'...")
    run_git_command(f'git commit -m "{commit_message}"')

    branch_name = run_git_command("git branch --show-current")

    print(f"🛰️ Pushing to origin/{branch_name}...")
    run_git_command(f"git push origin {branch_name}")

    print("Successfully uploaded to Git!")


if __name__ == "__main__":
    git_upload()