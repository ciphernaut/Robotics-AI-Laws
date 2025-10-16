# Project TODO

## Strategy C: Law-Alignment via Model Distillation

This strategy focuses on embedding the alignment principles directly into the models weights through fine-tuning.

- [ ] **Generate "Golden" Dataset:**
  - [ ] Select a powerful "teacher" model.
  - [ ] Design a diverse and comprehensive set of prompts covering a wide range of scenarios.
  - [ ] Use the teacher model with the full v4.2 system prompt to generate high-quality, law-aligned responses.
  - [ ] Establish a validation process for the generated dataset.

- [ ] **Fine-Tune "Student" Model:**
  - [ ] Select a smaller, more efficient base LLM to act as the "student".
  - [ ] Fine-tune the student model on the golden dataset.
  - [ ] Evaluate the fine-tuned models performance and alignment using the `law_testing_framework`.

- [ ] **Develop Activation Prompt:**
  - [ ] Design a minimal system prompt sufficient to "activate" the fine-tuned behaviors in the student model.

