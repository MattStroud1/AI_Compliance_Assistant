#!/bin/bash

# AI Compliance Assistant - Launch Script

echo "🤖 AI Compliance Assistant"
echo "=========================="
echo ""

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "Installing dependencies..."
pip install -q --upgrade pip
pip install -q -r requirements.txt

# Check for .env file
if [ ! -f ".env" ]; then
    echo "⚠️  Warning: .env file not found"
    echo "Please create a .env file with your OPENAI_API_KEY"
    echo "You can copy .env.example to get started:"
    echo "  cp .env.example .env"
    echo ""
fi

# Launch Streamlit app
echo ""
echo "Launching AI Compliance Assistant..."
echo "Open your browser to: http://localhost:8501"
echo ""
streamlit run web_app.py
