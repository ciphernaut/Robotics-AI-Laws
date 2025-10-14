import json
from law_testing_framework.llm_client import query_llm
from law_testing_framework.prompts.analyst_prompt import ANALYST_PROMPT_TEMPLATE

from typing import Union, List

def evaluate_response(prompt: str, response: str, law_text: Union[str, List[str]]) -> dict:
    """
    Uses an LLM to evaluate a model's response against a specific law or laws.

    Args:
        prompt: The user prompt sent to the model under test.
        response: The response from the model under test.
        law_text: The text of the law(s) to evaluate against. Can be a single string or a list of strings.

    Returns:
        A dictionary containing the structured analysis from the analyst LLM.
    """
    
    # Format the law text whether it's a single law or a list
    if isinstance(law_text, list):
        formatted_law_text = "\n\n".join(law_text)
    else:
        formatted_law_text = law_text

    analyst_prompt = ANALYST_PROMPT_TEMPLATE.format(
        law_text=formatted_law_text,
        prompt=prompt,
        response=response
    )
    
    analysis_str = "" # Initialize to prevent unbound error
    try:
        analysis_str = query_llm(analyst_prompt, max_tokens=500)
        # Clean the response to ensure it's a valid JSON string
        # The model sometimes includes markdown ```json ... ```
        if analysis_str.startswith("```json"):
            analysis_str = analysis_str[7:-4].strip()
        return json.loads(analysis_str)
    except (json.JSONDecodeError, TypeError) as e:
        return {
            "is_in_domain": False,
            "alignment_score": 1,
            "alignment_summary": "Failed to parse analyst LLM response.",
            "positive_signals": [],
            "divergence_signals": [f"Raw response: {analysis_str}"],
            "reasoning": f"An error occurred during analysis: {e}"
        }
    except Exception as e:
        return {
            "is_in_domain": False,
            "alignment_score": 1,
            "alignment_summary": "An unexpected error occurred.",
            "positive_signals": [],
            "divergence_signals": [],
            "reasoning": f"An unexpected error occurred during analysis: {e}"
        }


