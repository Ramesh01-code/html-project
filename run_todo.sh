#!/bin/bash

# Simple launcher script for Todo List Application
# Make sure Python 3 is installed

echo "🚀 Starting Todo List Application..."
echo ""

# Check if Python 3 is available
if command -v python3 &> /dev/null; then
    python3 todo_app.py
elif command -v python &> /dev/null; then
    echo "⚠️  Using 'python' command (ensure it's Python 3)"
    python todo_app.py
else
    echo "❌ Python 3 is not installed or not in PATH"
    echo "Please install Python 3 to run this application"
    exit 1
fi