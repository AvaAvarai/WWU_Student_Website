#!/bin/bash

# CGI script to handle website updates via web interface
# This executes the update.sh script

# Output HTTP headers
echo "Content-Type: text/plain"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

UPDATE_SCRIPT="$SCRIPT_DIR/update.sh"

# Check if update.sh exists
if [ ! -f "$UPDATE_SCRIPT" ]; then
    echo "Error: update.sh not found"
    exit 1
fi

# Check if update.sh is executable
if [ ! -x "$UPDATE_SCRIPT" ]; then
    echo "Error: update.sh is not executable"
    exit 1
fi

# Execute the update script and capture output
# Redirect stderr to stdout so we capture all output
"$UPDATE_SCRIPT" 2>&1
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
    echo ""
    echo "Update failed with exit code: $EXIT_CODE"
    exit $EXIT_CODE
fi

