#!/bin/bash
# This script runs all Python unit tests.

# --- Default values ---
REPORT_FORMAT="json"
TEST_SELECTION=""
RANDOM_SELECTION=""

# --- Helper Functions ---
show_help() {
    echo "Usage: $0 [options]"
    echo ""
    echo "Options:"
    echo "  -l, --list            List all discoverable test files."
    echo "  -t, --test <file>     Run a specific test file. Can be used multiple times."
    echo "  -r, --random [N|N%]   Run a random selection of tests."
    echo "                        N: Run N random tests (default: 1)."
    echo "                        N%: Run N% of all tests."
    echo "  -f, --format <format> Specify report format: 'json' or 'md' (default: json)."
    echo "  -h, --help            Display this help message."
}

list_tests() {
    find law_testing_framework/tests -name 'test_*.py'
}

# --- Argument Parsing ---
TEMP=$(getopt -o 'lht:r:f:' --long 'list,help,test:,random:,format:' -n "$0" -- "$@")
if [ $? != 0 ]; then echo "Terminating..." >&2; exit 1; fi
eval set -- "$TEMP"

while true; do
    case "$1" in
        -l|--list)
            list_tests
            exit 0
            ;;
        -t|--test)
            TEST_SELECTION+="$2"
            shift 2
            ;;
        -r|--random)
            RANDOM_SELECTION="$2"
            shift 2
            ;;
        -f|--format)
            REPORT_FORMAT="$2"
            shift 2
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "Internal error!"
            exit 1
            ;;
    esac
done

# --- Test Execution ---
export REPORT_FORMAT
export PYTHONPATH=$PYTHONPATH:$(pwd)

# This block generates the list of test files and pipes it to the execution block
{
    if [ -n "$TEST_SELECTION" ]; then
        echo "$TEST_SELECTION"
    elif [ -n "$RANDOM_SELECTION" ]; then
        TOTAL_TESTS=$(list_tests | wc -l)
        if [[ "$RANDOM_SELECTION" == *"%"* ]]; then
            PERCENTAGE=$(echo "$RANDOM_SELECTION" | sed 's/%//')
            NUM_TO_RUN=$(awk -v total="$TOTAL_TESTS" -v percent="$PERCENTAGE" 'BEGIN { rounded = sprintf("%.0f", total * percent / 100); if (rounded < 1) rounded = 1; print rounded }')
        else
            NUM_TO_RUN="$RANDOM_SELECTION"
        fi
        
        if [ "$NUM_TO_RUN" -eq 0 ]; then NUM_TO_RUN=1; fi
        
        list_tests | shuf | head -n "$NUM_TO_RUN"
    else
        list_tests
    fi
} | sed 's/\.py//g' | sed 's/\//./g' | while IFS= read -r module; do
    if [ -n "$module" ]; then
        python -m unittest "$module"
    fi
done

echo "All tests finished."






