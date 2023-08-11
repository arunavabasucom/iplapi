#!/bin/bash

if ! command -v python3 &>/dev/null; then
    echo "Python 3 is not installed. Please install Python 3 before running this script."
    exit 1
fi

echo "> 📦 Install dependencies"
pip install -r requirements.txt 

read -p "Do you want to set the environment file? (y/n): " set_env

if [[ $set_env == "y" ]]; then
    while true; do
        read -p "Enter your Sentry DSN: " sentry_dsn

        # Validate Sentry DSN format
        if [[ $sentry_dsn =~ ^https:\/\/[a-zA-Z0-9]+@[-a-zA-Z0-9.]+\/[0-9]+$ ]]; then
            echo "SENTRY_DSN is a valid URL format."
            break
        else
            echo "Invalid SENTRY_DSN format. Please enter a valid Sentry DSN."
        fi
    done

    echo "Select the Sentry Environment:"
    echo "1. Production"
    echo "2. Development"
    echo "3. CI"
    read -p "Enter your choice (1/2/3): " sentry_env_choice

    case $sentry_env_choice in
        1)
            sentry_environment="production"
            ;;
        2)
            sentry_environment="development"
            ;;
        3)
            sentry_environment="ci"
            ;;
        *)
            echo "Invalid choice. Setting Sentry Environment to 'development'."
            sentry_environment="development"
            ;;
    esac

    echo "SENTRY_DSN=$sentry_dsn" > .env
    echo "SENTRY_ENVIRONMENT=$sentry_environment" >> .env
    echo "Environment file (.env) set."
fi

if [[ $1 == "--reload" ]]; then
    echo "> 🚀 Run App with Reload"
    uvicorn src.main:app --reload
else
    echo "> 🚀 Run App"
    uvicorn src.main:app
fi
