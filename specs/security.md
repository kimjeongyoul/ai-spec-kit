# 🛡 Security Specification (OWASP & LLM Focus)

This project follows strict security guidelines to protect data and system integrity.

## 1. Core Principles
- **Least Privilege**: Grant only the minimum permissions required.
- **Defense in Depth**: Multiple layers of security controls.
- **Fail Securely**: Systems should fail in a state that maintains security.

## 2. OWASP LLM Top 10 Guardrails
- **Prompt Injection Defense**: Never trust user input as instructions. Use delimiters and system-level enforcement.
- **Insecure Output Handling**: AI-generated code must be sanitized before execution.
- **Sensitive Information**: Never include API keys, passwords, or PII in prompts or generated code.

## 3. Web Security (OWASP Top 10)
- **Injection**: Prevent SQL, NoSQL, and command injection.
- **Broken Access Control**: Ensure proper authorization for all resources.
- **Cryptographic Failures**: Use strong encryption for sensitive data at rest and in transit.
