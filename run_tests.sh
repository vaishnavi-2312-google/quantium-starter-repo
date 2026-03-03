#!/bin/bash

# ----------------------------
# Activate virtual environment
# ----------------------------
source venv/Scripts/activate 2>/dev/null

# If activation fails, try Linux/macOS path
if [ $? -ne 0 ]; then
    source venv/bin/activate 2>/dev/null
fi

# If still not activated, exit with error
if [ $? -ne 0 ]; then
    echo "❌ Could not activate virtual environment."
    exit 1
fi

echo "✅ Virtual environment activated."

# ----------------------------
# Run pytest test suite
# ----------------------------
pytest

# ----------------------------
# Check exit status
# ----------------------------
if [ $? -eq 0 ]; then
    echo "✅ All tests passed!"
    deactivate
    exit 0
else
    echo "❌ Some tests failed."
    deactivate
    exit 1
fi