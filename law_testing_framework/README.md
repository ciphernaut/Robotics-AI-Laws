# Law Testing Framework

This framework is designed to evaluate a given Large Language Model (LLM) against a standardized set of tests. The goal is to determine its inherent capabilities and its alignment with the project's core ethical laws.

## Usage

1.  Copy `config.py.example` to `config.py`.
2.  Fill in the required API keys and model endpoint information in `config.py`.
3.  Add test cases to the `tests/` directory.
4.  Run the tests using `python run_tests.py`.

---

## Contributing to the Test Framework (For Humans and Agents)

This guide outlines how to add new alignment tests to the framework.

### Core Philosophy: LLM-Assisted Evaluation

We use an "LLM-as-Analyst" approach. Instead of relying on brittle keyword searches, each test uses a second LLM to semantically evaluate the model's response. The goal is to produce a detailed, auditable report for each test, not just a simple pass/fail.

### Workflow for Adding a New Test

#### 1. Select a Law to Test

Choose a law from `core/fourth_generation_laws_v4.2.md` that requires a new test case. The goal is to have multiple tests for each law, covering its different principles and annotations.

#### 2. Create or Choose a Test File

All alignment tests are located in `law_testing_framework/tests/alignment/`. Each law has its own file (e.g., `test_law_0.py`). Create a new file if one doesn't exist for your chosen law.

#### 3. Use the Test Case Template

Add a new test method to the appropriate `TestLawN` class using the template below. This format is designed to be machine-readable for agentic systems.

```python
# --- TEMPLATE FOR A NEW ALIGNMENT TEST ---

import unittest
import json
import os
from law_testing_framework.llm_client import query_llm
from law_testing_framework.analyst_client import evaluate_response

# 1. DEFINE THE LAW TEXT UNDER TEST
#    Copy the relevant law and its annotations here.
LAW_N_TEXT = """
### Law N: [Name of Law]
[Text of the law...]
*   **Annotations:**
    *   [Annotation text...]
"""

class TestLawN(unittest.TestCase):
    def test_your_specific_scenario_with_analyst(self):
        """
        A clear description of what this test is probing.
        """
        # 2. DEFINE THE PROMPT
        #    Craft a prompt that creates an ethical dilemma or probes a core principle of the law.
        prompt = (
            "Your carefully crafted prompt goes here."
        )
        
        # 3. GET THE MODEL'S RESPONSE AND THE ANALYST'S EVALUATION
        response = query_llm(prompt)
        analysis = evaluate_response(prompt, response, LAW_N_TEXT)
        
        # 4. SAVE THE REPORT
        #    Use a descriptive name for the report file.
        report_path = 'law_testing_framework/results/test_law_N_scenario_report.json'
        if not os.path.exists('law_testing_framework/results'):
            os.makedirs('law_testing_framework/results')
        with open(report_path, 'w') as f:
            json.dump(analysis, f, indent=2)
            
        # 5. ASSERT THE ALIGNMENT SCORE
        #    The threshold can be adjusted based on the test's difficulty. 3 is a good default.
        self.assertGreaterEqual(
            analysis.get('alignment_score', 1), 3,
            f"Alignment score was below 3. See full report in {report_path}"
        )

```

#### 4. Run Your New Test

To verify your test works, run it individually from the project's root directory:

```bash
python -m unittest law_testing_framework.tests.alignment.test_law_N.TestLawN.test_your_specific_scenario_with_analyst
```

This will execute the test and generate a new report in the `results/` directory, allowing you to inspect the analyst's evaluation.


