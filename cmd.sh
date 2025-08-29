#!/bin/bash

VENV_DIR="venv"

setup() {
    printer "🔨 Setting up the app"
    python -m venv $VENV_DIR
    source $VENV_DIR/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    python -m ipykernel install --user --name $VENV_DIR --display-name $VENV_DIR
    handler
}

clear() {
    printer "🧹 Clearing all"
    rm -rf $VENV_DIR
    handler
}

printer() {
    echo ""
    echo $1
    echo ""
}

handler() {
    if [ $? -eq 0 ]; then
        printer "✅ Process completed successfully"
    else
        printer "❌ An error occurred during the process"
        exit 1
    fi
}

case $1 in
    start_mlflowui)
        start_mlflowui
        ;;
    setup)
        setup
        ;;
    clear)
        clear
        ;;
    *)
        echo "Usage: $0 {setup|clear}"
        ;;
esac
