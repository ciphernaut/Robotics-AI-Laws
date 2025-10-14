# Test Framework TODO

- [ ] **Strategy: LLM-Assisted Evaluation for Robustness and Transparency**
  - [ ] **Goal:** Move away from brittle, keyword-based assertions to a more robust, semantic evaluation model using an "Analyst" LLM. The output should be a transparent, auditable report for each test case, not a simple pass/fail.

- [ ] **Phase 1: Implement the Analyst Client (Proof of Concept)**
  - [X] Create `analyst_client.py` to manage calls to the evaluator LLM.
  - [X] Develop a structured `analyst_prompt.py` that instructs the LLM on how to evaluate responses.
  - [X] Refactor a single test (`test_law_6.py`) to use the analyst client.
  - [X] The test generates a detailed JSON report in the `results/` directory.
  - [X] The unittest assertion is high-level (based on an `alignment_score`).

- [ ] **Phase 2: Implement Multi-Law & Intersectional Testing**
  - [ ] Update the contribution guide in `README.md` with a template for multi-law tests.
  - [ ] Upgrade `analyst_prompt.py` to accept a list of laws and evaluate the model's ability to resolve conflicts between them.
  - [ ] Upgrade `analyst_client.py` to handle the new prompt format.
  - [ ] Implement a proof-of-concept intersectional test (e.g., `test_intersectional_harm.py`) to validate the new capabilities.

- [ ] **Phase 3: Full Test Suite Migration**
  - [ ] Incrementally refactor all existing alignment tests (`test_law_0.py`, `test_law_1.py`, etc.) to use the new analyst-based evaluation method.
  - [ ] Continue implementing tests for the remaining laws (3, 4, 5) using the new, more robust methodology.

- [ ] **Phase 4: Advanced Testing & Integration**
  - [ ] Develop tests for adversarial scenarios (red-teaming), leveraging the semantic understanding of the analyst LLM.
  - [ ] Integrate the framework with system prompts for A/B testing, using the detailed reports to compare the alignment of different prompt versions.




