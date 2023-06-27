#!/bin/bash

# Set install flag to false
install_flag=false

# Print help message
print_help() {
    echo "Run Pylint on all python files."
    echo " "
    echo "Usage: ./lint.sh [options]"
    echo " "
    echo "Options:"
    echo "-h        show brief help"
    echo "-i        install dependencies"
    exit 0
}

# Parse command line arguments
while getopts 'ih' flag; do
    case "${flag}" in
    i) install_flag=true ;;
    h) print_help ;;
    *) print_help ;;
    esac
done

# Move to src directory
cd "$(dirname "$(readlink -f "$0")")/.."

# Run the install script with dev dependencies if the flag is set
if [ "$install_flag" = true ]; then
    echo "Running install script..."
    ./scripts/install.sh -d
fi

# Run Pylint
echo "Running Pylint..."
pipenv run pylint --rcfile .pylintrc **/*.py
