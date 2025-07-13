#!/bin/bash

# Calculator App Startup Script
echo "🧮 Starting Calculator App..."
echo "================================"

# Activate virtual environment
source calculator_env/bin/activate

# Run the Streamlit app
echo "Starting Streamlit server..."
echo "The app will be available at: http://localhost:8501"
echo "Press Ctrl+C to stop the app"
echo "================================"

streamlit run calculator_app.py