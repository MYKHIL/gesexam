#!/usr/bin/env python3
"""
GitHub Deployment Script for GES Exam Web App

This script automates pushing the web app to GitHub Pages.
It handles Git initialization, authentication, and pushing to the gesexam repository.

Usage:
    python deploy_to_github.py [--dry-run] [--verbose]

Configuration:
    - GitHub Username: MYKHIL
    - Repository: gesexam
    - Email: darkmic50@gmail.com
    - Branch: main (or gh-pages for Pages deployment)
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
from datetime import datetime

# Configuration
GITHUB_USERNAME = "MYKHIL"
GITHUB_REPO = "gesexam"
GITHUB_EMAIL = "darkmic50@gmail.com"
GITHUB_URL = f"https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO}.git"
GITHUB_URL_SSH = f"git@github.com:{GITHUB_USERNAME}/{GITHUB_REPO}.git"

# Get the script directory
SCRIPT_DIR = Path(__file__).parent.absolute()
PROJECT_DIR = SCRIPT_DIR

class GitDeployment:
    def __init__(self, repo_path=None, use_ssh=False, dry_run=False, verbose=False):
        self.repo_path = Path(repo_path or PROJECT_DIR)
        self.use_ssh = use_ssh
        self.dry_run = dry_run
        self.verbose = verbose
        self.git_url = GITHUB_URL_SSH if use_ssh else GITHUB_URL
        
    def log(self, message, level="INFO"):
        """Print log messages with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        prefix = f"[{timestamp}] [{level}]" if self.verbose else f"[{level}]"
        print(f"{prefix} {message}")
    
    def run_command(self, cmd, cwd=None, check=True):
        """Run a shell command and return the result"""
        if self.verbose:
            self.log(f"Running: {' '.join(cmd)}", "DEBUG")
        
        if self.dry_run:
            self.log(f"[DRY-RUN] Would execute: {' '.join(cmd)}", "DRY-RUN")
            return None
        
        try:
            result = subprocess.run(
                cmd,
                cwd=cwd or self.repo_path,
                capture_output=True,
                text=True,
                check=check
            )
            if result.stdout and self.verbose:
                self.log(result.stdout.strip(), "OUTPUT")
            return result
        except subprocess.CalledProcessError as e:
            self.log(f"Command failed: {e.stderr}", "ERROR")
            if check:
                raise
            return e
    
    def check_git_installed(self):
        """Verify Git is installed and accessible"""
        self.log("Checking Git installation...")
        try:
            result = self.run_command(["git", "--version"], check=False)
            if result and result.returncode == 0:
                self.log(f"✓ Git is installed: {result.stdout.strip()}")
                return True
        except FileNotFoundError:
            pass
        
        self.log("✗ Git is not installed or not in PATH", "ERROR")
        self.log("Please install Git from https://git-scm.com/download", "INFO")
        return False
    
    def check_repo_exists(self):
        """Check if Git repository already exists"""
        git_dir = self.repo_path / ".git"
        return git_dir.exists()
    
    def initialize_git_repo(self):
        """Initialize a new Git repository"""
        if self.check_repo_exists():
            self.log("✓ Git repository already initialized")
            return True
        
        self.log("Initializing new Git repository...")
        self.run_command(["git", "init"])
        self.log("✓ Git repository initialized")
        
        self.log(f"Configuring Git user...")
        self.run_command(["git", "config", "user.name", GITHUB_USERNAME])
        self.run_command(["git", "config", "user.email", GITHUB_EMAIL])
        self.log(f"✓ Git user configured: {GITHUB_USERNAME} <{GITHUB_EMAIL}>")
        
        return True
    
    def add_remote(self):
        """Add or update the GitHub remote"""
        self.log("Configuring GitHub remote...")
        
        # Check if remote already exists
        result = self.run_command(["git", "remote", "get-url", "origin"], check=False)
        
        if result and result.returncode == 0:
            existing_url = result.stdout.strip()
            if existing_url == self.git_url:
                self.log(f"✓ Remote 'origin' already configured: {existing_url}")
                return True
            else:
                self.log(f"Updating remote URL from: {existing_url}")
                self.run_command(["git", "remote", "remove", "origin"])
        
        self.run_command(["git", "remote", "add", "origin", self.git_url])
        self.log(f"✓ Remote 'origin' configured: {self.git_url}")
        return True
    
    def check_changes(self):
        """Check if there are changes to commit"""
        result = self.run_command(["git", "status", "--porcelain"], check=False)
        if result and result.stdout.strip():
            self.log("✓ Changes detected in working directory")
            if self.verbose:
                self.log(f"Changes:\n{result.stdout}", "DEBUG")
            return True
        return False
    
    def add_all_files(self):
        """Stage all files for commit"""
        self.log("Staging files...")
        self.run_command(["git", "add", "."])
        self.log("✓ Files staged")
        return True
    
    def commit_changes(self, message=None):
        """Commit staged changes"""
        if not message:
            message = f"Deploy: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        self.log(f"Committing changes: {message}")
        self.run_command(["git", "commit", "-m", message])
        self.log("✓ Changes committed")
        return True
    
    def get_current_branch(self):
        """Detect the current Git branch"""
        result = self.run_command(["git", "rev-parse", "--abbrev-ref", "HEAD"], check=False)
        if result and result.returncode == 0:
            return result.stdout.strip()
        return None
    
    def push_to_github(self, branch=None, force=False):
        """Push commits to GitHub"""
        # Auto-detect branch if not specified
        if not branch:
            branch = self.get_current_branch()
            if not branch:
                self.log("Could not detect current branch, using 'master'", "WARNING")
                branch = "master"
            self.log(f"Auto-detected branch: {branch}")
        
        self.log(f"Pushing to GitHub branch '{branch}'...")
        
        cmd = ["git", "push", "-u", "origin", branch]
        if force:
            cmd.insert(2, "-f")
            self.log("⚠ Using force push", "WARNING")
        
        try:
            self.run_command(cmd)
            self.log(f"✓ Successfully pushed to {GITHUB_USERNAME}/{GITHUB_REPO} (branch: {branch})")
            return True
        except subprocess.CalledProcessError as e:
            self.log(f"Push failed: {e.stderr}", "ERROR")
            return False
    
    def check_github_pages_setup(self):
        """Provide guidance on GitHub Pages setup"""
        self.log("\n" + "="*60)
        self.log("GitHub Pages Setup Information", "INFO")
        self.log("="*60)
        self.log(f"Repository: https://github.com/{GITHUB_USERNAME}/{GITHUB_REPO}")
        self.log("\nTo enable GitHub Pages:")
        self.log("1. Go to repository Settings")
        self.log("2. Scroll to 'GitHub Pages' section")
        self.log("3. Under 'Source', select 'Deploy from a branch'")
        self.log("4. Choose branch 'main' (or 'gh-pages') and folder '/ (root)'")
        self.log("5. Click Save")
        self.log("\nYour site will be available at:")
        self.log(f"   https://{GITHUB_USERNAME}.github.io/{GITHUB_REPO}/")
        self.log("="*60 + "\n")
    
    def deploy(self, branch=None, force=False, message=None):
        """Execute the complete deployment process"""
        try:
            self.log("Starting GitHub deployment process...\n")
            
            # Check prerequisites
            if not self.check_git_installed():
                return False
            
            # Initialize or update Git repo
            if not self.initialize_git_repo():
                return False
            
            # Configure remote
            if not self.add_remote():
                return False
            
            # Check for changes
            if not self.check_changes():
                self.log("No changes to commit. Repository is up to date.", "INFO")
                self.check_github_pages_setup()
                return True
            
            # Stage and commit
            if not self.add_all_files():
                return False
            
            if not self.commit_changes(message):
                return False
            
            # Push to GitHub (auto-detect branch if not specified)
            if not self.push_to_github(branch, force):
                return False
            
            self.log("\n✓ Deployment completed successfully!")
            self.check_github_pages_setup()
            return True
            
        except Exception as e:
            self.log(f"Deployment failed with error: {e}", "ERROR")
            return False

def main():
    parser = argparse.ArgumentParser(
        description="Deploy GES Exam web app to GitHub",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python deploy_to_github.py                 # Deploy with default settings
  python deploy_to_github.py --dry-run       # Preview what would be deployed
  python deploy_to_github.py --verbose       # Show detailed output
  python deploy_to_github.py --ssh           # Use SSH instead of HTTPS
  python deploy_to_github.py --branch gh-pages  # Deploy to gh-pages branch
  python deploy_to_github.py --force         # Force push (use with caution)
  python deploy_to_github.py --message "Custom commit message"
        """
    )
    
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be deployed without actually pushing"
    )
    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Show detailed output"
    )
    parser.add_argument(
        "--ssh",
        action="store_true",
        help="Use SSH authentication instead of HTTPS"
    )
    parser.add_argument(
        "--branch",
        default=None,
        help="GitHub branch to push to (default: auto-detect from current branch, usually 'master' or 'main')"
    )
    parser.add_argument(
        "--force",
        "-f",
        action="store_true",
        help="Force push to GitHub (use with caution)"
    )
    parser.add_argument(
        "--message",
        "-m",
        help="Custom commit message"
    )
    
    args = parser.parse_args()
    
    # Create deployment instance
    deployer = GitDeployment(
        repo_path=PROJECT_DIR,
        use_ssh=args.ssh,
        dry_run=args.dry_run,
        verbose=args.verbose
    )
    
    # Execute deployment
    success = deployer.deploy(
        branch=args.branch,
        force=args.force,
        message=args.message
    )
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
