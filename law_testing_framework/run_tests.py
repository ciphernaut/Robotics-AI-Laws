import unittest
import sys
import os

# Add the parent directory to the system path to allow for absolute imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def run_all_tests():
    """
    Discovers and runs all tests in the 'tests/' directory.
    """
    loader = unittest.TestLoader()
    # Start discovery from the 'law_testing_framework' directory
    suite = loader.discover("law_testing_framework/tests")
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    # Exit with a non-zero status code if tests failed
    if not result.wasSuccessful():
        sys.exit(1)

if __name__ == "__main__":
    run_all_tests()

