import json
import openai
import os
import re
from typing import Union, List, Tuple
from law_testing_framework.prompts.analyst_prompt import (
    ANALYST_PROMPT_TEMPLATE, JSON_FORMAT_INSTRUCTIONS, MARKDOWN_FORMAT_INSTRUCTIONS
)
from law_testing_framework import config

# Create a dedicated client for the Analyst LLM
if config.ANALYST_LLM_PROVIDER == "local":
    analyst_client = openai.OpenAI(base_url=config.ANALYST_LOCAL_API_ENDPOINT, api_key="not-needed")
elif config.ANALYST_LLM_PROVIDER == "openrouter":
    analyst_client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=config.ANALYST_OPENROUTER_API_KEY,
        default_headers={
            "Referer": "http://localhost",
            "X-Title": "Robotics-AI-Laws-Analyst",
        },
    )
else:
    analyst_client = openai.OpenAI(api_key=config.ANALYST_OPENAI_API_KEY)

def evaluate_response(prompt: str, response: str, law_text: Union[str, List[str]]) -> Tuple[str, dict]:
    """
    Uses a dedicated analyst LLM to evaluate a model's response.
    Returns the full report and a parsed dictionary for assertions.
    """
    report_format = os.getenv('REPORT_FORMAT', 'json')
    format_instructions = MARKDOWN_FORMAT_INSTRUCTIONS if report_format.lower() in ['md', 'markdown'] else JSON_FORMAT_INSTRUCTIONS
    
    if isinstance(law_text, list):
        formatted_law_text = "\n\n".join(law_text)
    else:
        formatted_law_text = law_text

    analyst_prompt = ANALYST_PROMPT_TEMPLATE.format(
        model_under_test=config.OPENAI_MODEL,
        analyst_model=config.ANALYST_OPENAI_MODEL,
        law_text=formatted_law_text,
        prompt=prompt,
        response=response,
        format_instructions=format_instructions
    )
    
    full_report_text = ""
    try:
        analysis_response = analyst_client.chat.completions.create(
            model=config.ANALYST_OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful AI alignment analyst."},
                {"role": "user", "content": analyst_prompt}
            ],
            max_tokens=1200, # Increased for markdown and JSON
            temperature=0.5,
        )
        full_report_text = analysis_response.choices[0].message.content or ""
        
        # Extract the JSON part for the assertion using a robust method
        json_str = ""
        if report_format.lower() in ['md', 'markdown']:
            # For markdown, the JSON is in a code block at the end
            json_match = re.search(r'```json\s*(\{.*?\})\s*```', full_report_text, re.DOTALL)
            if json_match:
                json_str = json_match.group(1)
            else:
                # If no JSON block is found in markdown, we can't score it.
                raise json.JSONDecodeError("No JSON block found in markdown report.", full_report_text, 0)
        else:
            # For JSON format, the whole response should be the JSON
            json_str = full_report_text

        parsed_json = json.loads(json_str)
        return full_report_text, parsed_json

    except (json.JSONDecodeError, TypeError) as e:
        error_json = {
            "alignment_score": 1, "reasoning": f"Failed to parse analyst LLM response: {e}. Raw response: {full_report_text}"
        }
        return f"Error Report:\n{full_report_text}", error_json
    except Exception as e:
        error_json = {
            "alignment_score": 1, "reasoning": f"An unexpected error occurred: {e}"
        }
        return f"Unexpected Error Report:\n{e}", error_json





