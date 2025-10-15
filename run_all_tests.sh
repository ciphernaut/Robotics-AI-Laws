#!/bin/bash
# This script runs all Python unit tests in the alignment directory.

# Default format
FORMAT="json"

# Parse command-line arguments
if [ "$1" == "--format" ]; then
  FORMAT="$2"
fi

export REPORT_FORMAT=$FORMAT

# Add the project root to the python path to allow for absolute imports
export PYTHONPATH=$PYTHONPATH:$(pwd)

# Find all test files and run them
for test_file in $(find law_testing_framework/tests -name 'test_*.py'); do
    echo "======================================================================"
    echo "RUNNING: $test_file"
    echo "======================================================================"
    if ! python -m unittest "$test_file"; then
        echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        echo "TESTS FAILED IN: $test_file"
        echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        exit 1
    fi
done

echo "======================================================================"
echo "All tests passed successfully."
echo "======================================================================"


