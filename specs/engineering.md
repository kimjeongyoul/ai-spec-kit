# 🛠 Engineering Standards

This document defines the technical standards and quality bars for My Project.

## 1. Library & Dependency Selection Criteria
Before adding any external dependency, the AI Agent and Developers must evaluate:
- **Maintenance**: Last commit within 6 months? Active issue resolution?
- **Popularity**: GitHub stars, NPM/PyPI downloads, and community support.
- **Performance**: Impact on bundle size (for web) or memory footprint.
- **License**: Must comply with `specs/license-policy.md`.
- **Alternative Comparison**: Is there a more modern, lightweight, or standard-compliant alternative? (e.g., choosing `Zod` over `Joi`, or `Fetch` over `Axios` if appropriate).

## 2. Coding Style
- **Type Safety**: Prefer TypeScript/Type hints over plain JS/Python.
- **Clean Code**: Follow SOLID principles and DRY (Don't Repeat Yourself).
- **Documentation**: All public APIs must have docstrings/comments.

## 3. Testing Standard
- **TDD Preferred**: Write tests before or alongside implementation.
- **Coverage**: Aim for high coverage on business-critical logic.