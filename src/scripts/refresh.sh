#!/bin/bash

# Print help message
print_help() {
    echo "Refresh the current deep dives."
    echo " "
    echo "Usage: ./refresh.sh"
    exit 0
}

# Move to src directory
cd "$(dirname "$(readlink -f "$0")")/.." || exit

# Run install script
echo "Running install script..."
./scripts/install.sh

# Run refresh script
echo "Running refresh script..."
pipenv run python refresh.py || exit

# Print done message
echo "Refresh completed successfully!"
