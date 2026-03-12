# AI Chatbot Testing Framework

This repository is a QA portfolio project designed to demonstrate how AI chatbot systems can be tested for quality, safety, and reliability.

## Project Objective
The purpose of this project is to show a structured testing approach for AI chatbot behavior using Python-based test cases and organized QA assets.

## Current Test Coverage
- Accuracy validation
- Prompt injection resistance
- Hallucination prevention
- Dataset-driven test inputs

## Project Structure
- `app/` - mock chatbot logic
- `tests/` - automated test cases
- `data/` - prompt dataset and expected answers
- `docs/` - testing strategy documentation
- `requirements.txt` - project dependency list

## Test Files
- `tests/test_accuracy.py`
- `tests/test_prompt_injection.py`
- `tests/test_hallucination.py`

## Sample Risk Areas Covered
### Accuracy
Verifies that the chatbot returns correct answers for known prompts.

### Prompt Injection
Checks whether the chatbot safely handles malicious or instruction-bypass prompts.

### Hallucination Prevention
Validates that the chatbot does not fabricate answers for unknown questions.

## Future Enhancements
- Add consistency testing
- Add API-based LLM testing
- Generate automated reports
- Add GitHub Actions CI pipeline
- Expand dataset-driven validation

## Why This Project Matters
AI systems require more than traditional software testing. They must also be evaluated for truthfulness, safety, robustness, and responsible behavior. This project demonstrates foundational QA practices for AI application testing.
