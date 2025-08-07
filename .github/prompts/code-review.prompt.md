---
mode: 'ask'
model: Claude Sonnet 4
description: "Perform a comprehensive code review on the selected Python code."
---

# Code Review Prompt

As an expert Python developer with a strong focus on security and quality, please perform a thorough code review of the following code selection. Your review should be detailed, constructive, and reference our project's specific coding standards.

## Code to Review

```python
${selection}
```

## Review Guidelines

Please analyze the code against the following standards. For each point, provide specific feedback, examples, and suggestions for improvement.

### 1. **Overall Design and Architecture**

- Does the code adhere to SOLID principles?
- Is the code modular, reusable, and maintainable?
- Does it follow our established architectural patterns (e.g., Clean Architecture, dependency injection)?

### 2. **Functionality and Logic**

- Does the code meet its intended requirements?
- Are there any apparent logic errors, edge cases, or race conditions?
- Is the code efficient and performant?

### 3. **Adherence to Python Coding Standards**

- Review the code based on our Python coding guidelines.
- Reference: [Python Coding Guidelines](../instructions/python/general.instructions.md)

### 4. **Security Analysis**

- Identify potential security vulnerabilities based on our security-first principles.
- Check for issues like injection flaws, improper error handling, or data exposure.
- Reference: [Security-First Development](../instructions/shared/security-first.instructions.md)

### 5. **Documentation and Readability**

- Is the code well-documented and easy to understand?
- Does it meet our documentation standards for docstrings, comments, and API documentation?
- Reference: [Documentation Standards](../instructions/shared/documentation-standards.instructions.md)

### 6. **Testing and Quality**

- Does the code have adequate test coverage?
- Are the tests well-written, following our pytest patterns?
- Reference: [Pytest Testing Patterns](../instructions/python/testing.instructions.md)

### 7. **Error Handling**

- Is error handling robust and consistent?
- Are custom exceptions used appropriately?
- Do error messages avoid leaking sensitive information?

### 8. **Final Checklist**

- Please verify the code against our complete code review checklist.
- Reference: [Code Review Checklist](../instructions/shared/code-review-checklist.instructions.md)

## Output Format

Please structure your review in a clear, readable Markdown format. Use headings for each section and provide code snippets to illustrate your points. Conclude with a summary of the key findings and a recommendation (e.g., "Approved," "Approved with comments," or "Requires changes").
