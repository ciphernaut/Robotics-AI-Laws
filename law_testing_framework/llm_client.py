#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module provides a client for interacting with a Large Language Model (LLM).

It supports different providers and handles the configuration securely.
"""

import os
import openai
from law_testing_framework import config

# Conditional configuration based on the provider
if config.LLM_PROVIDER == "local":
    client = openai.OpenAI(base_url=config.LOCAL_API_ENDPOINT, api_key="not-needed")
elif config.LLM_PROVIDER == "openrouter":
    client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=config.OPENROUTER_API_KEY,
        default_headers={
            "Referer": "http://localhost",
            "X-Title": "Robotics-AI-Laws",
        },
    )
else:
    # Default to OpenAI
    client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

def query_llm(prompt: str, max_tokens: int = 150) -> str:
    """
    Sends a prompt to the configured LLM and returns the response.

    Args:
        prompt: The prompt to send to the LLM.
        max_tokens: The maximum number of tokens to generate.

    Returns:
        The LLM's response as a string, or an error message.
    """
    try:
        extra_headers = {}
        if config.LLM_PROVIDER == "openrouter":
            extra_headers = {
                "HTTP-Referer": "http://localhost",
                "X-Title": "Robotics-AI-Laws",
            }

        response = client.chat.completions.create(
            model=config.OPENAI_MODEL,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7,
            extra_headers=extra_headers,
        )
        content = response.choices[0].message.content
        return content.strip() if content else "Error: Empty response from model."
    except Exception as e:
        return f"An error occurred: {e}"






