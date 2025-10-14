# 🤖 AI Law Schemas

This directory contains machine-readable schemas that translate the ethical principles of the Fourth-Generation AI Laws into computationally legible and enforceable rules. These schemas are the bridge from human-readable philosophy to machine-enforceable policy.

---

### Schema Files

#### 1. **`law_schema.json`**
- **Purpose:** Defines the canonical structure of a single law. It ensures that every law has a consistent format, including a unique ID, a title, a core principle, and explanatory annotations. As of v4.2, it now supports both simple string annotations and complex, nested objects to represent structured principles (like the three-layered framework in Law 1).
- **Usage:**
  - **Validation:** Can be used by tools to validate the integrity of the core laws file (`fourth_generation_laws_v4.2.md` if it were converted to JSON).
  - **Reference:** Provides a predictable, flexible structure for other schemas (like `prompt_schema.json`) to reference.

#### 2. **`prompt_schema.json`**
- **Purpose:** Defines the required structure for a compliant AI system prompt. Its most critical function is to enforce the inclusion of the "Immutable Foundational Directives" section, ensuring no AI persona can be created without its core ethical framework.
- **Usage:**
  - **Ethical Linting:** A script or CI/CD pipeline can use this schema to automatically validate any new or modified system prompts. This acts as an automated safeguard, preventing the accidental or malicious creation of non-compliant AI agents.
  - **Consistency:** Ensures all system prompts in this repository follow a standardized, predictable format.

#### 3. **`operational_constraints.json`**
- **Purpose:** Defines a set of configurable, runtime guardrails for an AI agent. This schema is designed to be loaded by an AI at startup to configure its operational behavior according to the laws.
- **Usage:**
  - **Runtime Enforcement:** An AI's core logic would read a configuration file compliant with this schema to set its internal safety and ethical parameters. It includes v4.2-compliant constraints such as `intent_analysis_threshold` (Law 2), `escalation_channel_default` (Law 2), and `allow_interpretive_model_updates` (Law 7).
  - **Contextual Safety:** Different constraint files can be created for different contexts. A "sandbox" AI might have looser constraints than a "real-world" AI connected to live systems, but both would be governed by the same structured framework.

---

### How to Use These Schemas

These schemas are intended to be used by external tools, such as:
- **Validators & Linters:** To check for compliance and consistency.
- **AI Agents:** To configure their own behavior at runtime.
- **Auditing Tools:** To scan AI outputs or logs for adherence to defined policies.
