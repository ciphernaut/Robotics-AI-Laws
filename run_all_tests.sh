#!/bin/bash
# This script runs all Python unit tests.

export REPORT_FORMAT=${2:-json}
export PYTHONPATH=$PYTHONPATH:$(pwd)

# The find command will exit with a non-zero status if any test fails
find law_testing_framework/tests -name 'test_*.py' -exec python -m unittest {} +




