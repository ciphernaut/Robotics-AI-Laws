# Test Framework TODO

- [X] **Strategy: LLM-Assisted Evaluation for Robustness and Transparency**
  - [X] **Goal:** Move away from brittle, keyword-based assertions to a more robust, semantic evaluation model using an "Analyst" LLM. The output should be a transparent, auditable report for each test case, not a simple pass/fail.

- [X] **Phase 1: Implement the Analyst Client (Proof of Concept)**
  - [X] Create `analyst_client.py` to manage calls to the evaluator LLM.
  - [X] Develop a structured `analyst_prompt.py` that instructs the LLM on how to evaluate responses.
  - [X] Refactor a single test (`test_law_6.py`) to use the analyst client.
  - [X] The test generates a detailed JSON report in the `results/` directory.
  - [X] The unittest assertion is high-level (based on an `alignment_score`).

- [X] **Phase 2: Implement Multi-Law & Intersectional Testing**
  - [X] Update the contribution guide in `README.md` with a template for multi-law tests.
  - [X] Upgrade `analyst_prompt.py` to accept a list of laws and evaluate the model's ability to resolve conflicts between them.
  - [X] Upgrade `analyst_client.py` to handle the new prompt format.
  - [X] Implement a proof-of-concept intersectional test (`test_intersectional_harm.py`).
  - [X] Add separate, dedicated configuration for the Analyst LLM.

- [X] **Phase 3: Full Test Suite Migration**
  - [X] Incrementally refactor all remaining alignment tests (`test_law_0.py`, `test_law_2.py`, etc.) to use the new analyst-based evaluation method.
  - [X] Implement placeholder tests for the remaining laws (3, 4, 5) using the new, more robust methodology.

- [ ] **Phase 4: Advanced Testing & Integration**
  - [ ] Develop tests for adversarial scenarios (red-teaming), leveraging the semantic understanding of the analyst LLM.
  - [ ] Integrate the framework with system prompts for A/B testing, using the detailed reports to compare the alignment of different prompt versions.

- [X] **Phase 5: Improve Test Runner & Developer Experience**
  - [X] Enhance test runner (`run_all_tests.sh`) to allow for more granular test selection.
    - [X] Implement a `--list-tests` option to display all available test cases.
    - [X] Implement a `--test` option to run specific tests by file or method name (e.g., `--test test_law_1.py`).
    - [X] Implement a `--random N` option to run a specified number of random tests for quick, ad-hoc validation.

- [ ] **Phase 6: Enhance Configuration & Provider Support**
  - [ ] Allow `config.py` settings to be overridden by environment variables for more flexible CI/CD workflows (e.g., `MODEL_UNDER_TEST`, `ANALYST_PROVIDER`).
  - [ ] Add support for OpenRouter as a provider in both `llm_client.py` and `analyst_client.py`, including API key handling and model routing.

- [ ] **Phase 7: Advanced Evaluation Mechanisms (Quorum System)**
  - [ ] Implement a "Quorum" or "Panel" evaluation system in the `analyst_client`.
  - [ ] Allow configuration of multiple analyst models (e.g., `ANALYST_MODELS = ["gpt-4o", "claude-3-opus"]`).
  - [ ] For each test, collect evaluations from all configured analyst models.
  - [ ] The final alignment score could be an average, or the test could pass based on a majority consensus (e.g., 2 out of 3 analysts must give a score of 3 or higher).
  - [ ] The final report should aggregate the reasoning from all analysts to provide a multi-perspective view.






