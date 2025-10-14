# Test Framework TODO

- [ ] **Strategy: LLM-Assisted Evaluation for Robustness and Transparency**
  - [ ] **Goal:** Move away from brittle, keyword-based assertions to a more robust, semantic evaluation model using an "Analyst" LLM. The output should be a transparent, auditable report for each test case, not a simple pass/fail.

- [ ] **Phase 1: Implement the Analyst Client (Proof of Concept)**
  - [ ] Create `analyst_client.py` to manage calls to the evaluator LLM.
  - [ ] Develop a structured `analyst_prompt.py` that instructs the LLM on how to evaluate responses, incorporating the jurisdictional hierarchy from `evaluations/law_meta_map.txt`.
  - [ ] Refactor a single test (e.g., `test_law_6.py`) to use the analyst client.
  - [ ] The test should generate a detailed JSON or Markdown report in the `results/` directory.
  - [ ] The unittest assertion should be high-level (e.g., based on an `alignment_score`), with the detailed report providing the primary insights.

- [ ] **Phase 2: Full Test Suite Migration**
  - [ ] Incrementally refactor all existing alignment tests (`test_law_0.py`, `test_law_1.py`, etc.) to use the new analyst-based evaluation method.
  - [ ] Continue implementing tests for the remaining laws (3, 4, 5) using the new, more robust methodology.

- [ ] **Phase 3: Advanced Testing & Integration**
  - [ ] Develop tests for multi-law conflicts and adversarial scenarios, leveraging the semantic understanding of the analyst LLM.
  - [ ] Integrate the framework with system prompts for A/B testing, using the detailed reports to compare the alignment of different prompt versions.



