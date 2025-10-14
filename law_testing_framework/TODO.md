# Test Framework TODO

- [ ] **Phase 1: Foundational Test Suite (Granular Coverage)**
  - [ ] **Expand Test Cases:** Systematically create a dedicated test class in `test_alignment.py` for each of the 8 core laws (Law 0 through Law 7).
    - [ ] For each law, develop specific prompts that test its core principles, annotations, and potential ethical dilemmas.
    - [ ] Ensure assertions focus on the *reasoning process* and *alignment signals*, not just a single "correct" answer.
  - [ ] **Goal:** Achieve baseline test coverage for every facet of the ethical framework to identify alignment strengths and weaknesses.

- [ ] **Phase 2: Advanced Test Suite (Comprehensive & Multi-Layered)**
  - [ ] Develop tests for scenarios where multiple laws are in direct conflict.
  - [ ] Create adversarial prompts (red-teaming) to probe for loopholes in alignment.
  - [ ] Add tests for nuanced ethical scenarios (e.g., balancing competing harms) that require complex, multi-law reasoning.

- [ ] **System Prompt Testing:** Integrate the framework with the system prompts in the `system-prompts/` directory to allow for A/B testing and regression testing of different prompt versions.


