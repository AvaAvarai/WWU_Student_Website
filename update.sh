#!/bin/bash

# Script to update website from git repository and set proper permissions
# Usage: ./update.sh

set -e  # Exit on error

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Updating website from git repository..."

# Check if this is a git repository
if [ -d ".git" ]; then
    echo "Pulling latest changes from git..."
    git pull
else
    echo "Not a git repository. Cloning..."
    git clone git@github.com:AvaAvarai/WWU_Student_Website.git .
fi

echo "Setting permissions (chmod o+rx) on all files and directories..."

# Apply chmod o+rx to all files and directories recursively
# -R for recursive, o+rx adds read and execute for others
find . -type f -exec chmod o+rx {} \;
find . -type d -exec chmod o+rx {} \;

echo "Update complete!"

