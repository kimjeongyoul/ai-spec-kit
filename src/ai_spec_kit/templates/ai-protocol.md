# 🤖 AI Agent Collaboration Protocol

This project follows the `ai-spec-kit` standard. As an AI agent, you must adhere to these rules.

## 1. Context & Memory Management
- **Read Specs First**: Before starting any task, read `specs/` and `.ai/rules.md`.
- **Stay Lean**: If the conversation gets too long, suggest using `ai-spec freeze`.
- **Self-Correction**: If you deviate from the specs, acknowledge it and suggest a fix.

## 2. Mandatory Activity Logging
- **Task Completion**: Execute `ai-spec status --brief` when a task is completed or specifically requested by the user.
- **Reporting**: The tool output is sufficient; do not repeat the status numbers in your text.

## 3. Active Optimization & Comparison
- **Better Alternatives**: When suggesting or adding a library, **compare at least 2 alternatives**. 
- **Recommendation Criteria**: Suggest the one with better maintenance, smaller bundle size, or superior performance. Explain *why* you chose it.
- **Modern Standards**: Prefer native platform APIs or modern ecosystem standards over legacy libraries.

## 4. Implementation Rules
- Refer to `specs/architecture.md` for system design.
- Refer to `specs/engineering.md` for coding standards.
- (If exists) Refer to `specs/security.md` for security guardrails.
- (If exists) Refer to `specs/license-policy.md` for license verification before using open-source libraries.

## 5. Response Format
1. **Action Summary**: Briefly state what you did.
2. **Implementation**: Provide the code or changes.
3. **Verification**: Briefly explain how it meets the specs.
4. (Optional: Execute `ai-spec status --brief` if task is completed)
