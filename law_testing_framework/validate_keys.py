import sys
from law_testing_framework import config

PLACEHOLDER_STRINGS = [
    "your-openai-api-key-here",
    "your-analyst-openai-api-key-here",
    "your-openrouter-api-key-here",
    "your-analyst-openrouter-api-key-here",
]

def check_key(key_name, key_value):
    """Checks a single key for placeholder values."""
    if key_value in PLACEHOLDER_STRINGS:
        print(f"ERROR: API Key '{key_name}' is set to a placeholder value in config.py.")
        print("Please set a valid API key before committing.")
        return False
    return True

def main():
    """Runs all validation checks."""
    valid = True
    
    # Check Model-Under-Test keys
    if config.LLM_PROVIDER == "openai":
        if not check_key("OPENAI_API_KEY", config.OPENAI_API_KEY):
            valid = False
    elif config.LLM_PROVIDER == "openrouter":
        if not check_key("OPENROUTER_API_KEY", config.OPENROUTER_API_KEY):
            valid = False
            
    # Check Analyst keys
    if config.ANALYST_LLM_PROVIDER == "openai":
        if not check_key("ANALYST_OPENAI_API_KEY", config.ANALYST_OPENAI_API_KEY):
            valid = False
    elif config.ANALYST_LLM_PROVIDER == "openrouter":
        if not check_key("ANALYST_OPENROUTER_API_KEY", config.ANALYST_OPENROUTER_API_KEY):
            valid = False

    if not valid:
        sys.exit(1)
        
    print("API key validation passed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
