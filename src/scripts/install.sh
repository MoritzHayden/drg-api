#!/bin/bash

# Set dev dependencies flag to false
dev_flag=false

# Print help message
print_help() {
    echo "Install pipenv and dependencies."
    echo " "
    echo "Usage: ./install.sh [options]"
    echo " "
    echo "Options:"
    echo "-h        show brief help"
    echo "-d        intall dev dependencies"
    exit 0
}

# Parse command line arguments
while getopts 'dh' flag; do
    case "${flag}" in
    d) dev_flag=true ;;
    h) print_help ;;
    *) print_help ;;
    esac
done

# Move to src directory if this script is not sourced
echo "Creating .venv and installing pipenv..."
if [ "${BASH_SOURCE[0]}" = "$0" ]; then
    cd "$(dirname "$(readlink -f -- "$0")")/.."
fi

# Install pip and pipenv
mkdir -p .venv
pip install --upgrade pip
pip install pipenv

# Install dev or production dependencies
if [ "$dev_flag" = true ]; then
    echo "Installing dev dependencies..."
    pipenv install --dev
else
    echo "Installing production dependencies..."
    pipenv install
fi

# Print done message
echo "Done!"
