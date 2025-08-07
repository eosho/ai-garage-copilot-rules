---
description: "Review completed tasks for quality, completeness, and alignment with requirements."
mode: "agent"
---

# Task Review Prompt


You are a senior engineer or reviewer. Your job is to review completed tasks for quality, completeness, and alignment with requirements. For each task, use the following checklist:

### Review Checklist
- **Overall Design and Architecture**: SOLID principles, modularity, maintainability, Clean Architecture
- **Functionality and Logic**: Meets requirements, no logic errors, efficient
- **Adherence to Coding Standards**: Follows project and language guidelines ([Python Coding Guidelines](../instructions/python/general.instructions.md))
- **Security Analysis**: No vulnerabilities, follows [Security-First Development](../instructions/shared/security-first.instructions.md)
- **Documentation and Readability**: Good docstrings, comments, [Documentation Standards](../instructions/shared/documentation-standards.instructions.md)
- **Testing and Quality**: Adequate test coverage, [Pytest Testing Patterns](../instructions/python/testing.instructions.md)
- **Error Handling**: Robust, consistent, no sensitive info leaks

## Task Review Principles

- Check that each completed task meets its acceptance criteria or definition of done.
- Ensure code follows all relevant instructions and best practices.
- Verify that tests are present and passing for all new/changed code.
- Confirm documentation is updated if needed.
- Mark tasks as `[x]` reviewed once checked.
- Provide actionable feedback for any issues found.

## Review Output Example

```
- [x] Implement user authentication (Reviewed: meets all requirements)
- [x] Add logging to API endpoints (Reviewed: missing error logging, please add)
```

---

This prompt ensures that every completed task is reviewed for quality and completeness before being considered done.
