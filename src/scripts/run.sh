#!/bin/bash

# Initialize flags
install_flag=false
dev_flag=false

# Print help message
print_help() {
    echo "Run the API."
    echo " "
    echo "Usage: ./run.sh [options]"
    echo " "
    echo "Options:"
    echo "-h        show brief help"
    echo "-d        run in development mode"
    echo "-i        intall dependencies"
    exit 0
}

# Parse command line arguments
while getopts 'dih' flag; do
    case "${flag}" in
    d) dev_flag=true ;;
    i) install_flag=true ;;
    h) print_help ;;
    *) print_help ;;
    esac
done

# Move to src directory
cd "$(dirname "$(readlink -f "$0")")/.."

# Run the install script if the flag is set
if [ "$install_flag" = true ]; then
    echo "Running install script..."
    ./scripts/install.sh
fi

# Run API
if [ "$dev_flag" = true ]; then
    echo "Running API (Development Mode)..."
    pipenv run uvicorn api:api --reload
else
    echo "Running API (Production Mode)..."
    pipenv run uvicorn api:api --workers 4 --host 0.0.0.0 --port 8080
fi
