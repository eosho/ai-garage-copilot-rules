---
description: "Guidelines for generating conventional Git commit messages."
---

# Git Commit Message Instructions

When generating a Git commit message, please follow the Conventional Commits specification. This ensures that commit messages are readable, consistent, and can be used for automated changelog generation.

## Commit Message Format

The commit message should be structured as follows:

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### 1. **Type**

- Must be one of the following:
  - **feat**: A new feature.
  - **fix**: A bug fix.
  - **docs**: Documentation only changes.
  - **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc).
  - **refactor**: A code change that neither fixes a bug nor adds a feature.
  - **perf**: A code change that improves performance.
  - **test**: Adding missing tests or correcting existing tests.
  - **chore**: Changes to the build process or auxiliary tools and libraries such as documentation generation.
  - **ci**: Changes to our CI configuration files and scripts.
  - **build**: Changes that affect the build system or external dependencies.

### 2. **Scope** (Optional)

- The scope should be the name of the module/component affected by the change (e.g., `api`, `db`, `auth`, `ui`).
- Use a short, descriptive noun.

### 3. **Description**

- A short summary of the code changes.
- Use the imperative, present tense: "change" not "changed" nor "changes".
- Don't capitalize the first letter.
- No dot (.) at the end.
- Maximum 50 characters.

### 4. **Body** (Optional)

- Provide more context for the change.
- Explain the problem and the solution.
- Use the imperative, present tense.
- Wrap the body at 72 characters.

### 5. **Footer** (Optional)

- **Breaking Changes**: Start with `BREAKING CHANGE:` followed by a description of the change.
- **Issue References**: Reference issues that this commit closes, like `Closes #123` or `Fixes #456`.

## Example

```
feat(auth): add password reset functionality

Implement the complete password reset flow, including token generation, email sending, and password update logic.

- Add a new endpoint `/api/v1/auth/request-password-reset`.
- Create a secure, short-lived token for password resets.
- Integrate with the email service to send reset links.
- Add a new endpoint `/api/v1/auth/reset-password` to update the password.

BREAKING CHANGE: The user authentication response now includes a `password_last_changed` field.

Closes #42
```

## More Examples

### Fix

```
fix(api): correct user lookup logic in admin endpoint

The admin user lookup was incorrectly using the user's email instead of the user ID, causing 404 errors when the user existed. This change corrects the lookup to use the primary key.

Fixes #115
```

### Docs

```
docs(readme): update setup instructions and add prerequisites

Expanded the local development setup guide in the README.md to include details on setting up the Python virtual environment and installing dependencies. Added a section for required system-level prerequisites like PostgreSQL.
```

### Refactor

```
refactor(services): extract email sending logic into a dedicated service

To improve separation of concerns and reusability, the email sending functionality, previously duplicated in the user and notification services, has been extracted into a new `EmailService`. This simplifies the original services and centralizes email configuration.
```

### Test

```
test(auth): add unit tests for token validation edge cases

Added new unit tests to cover edge cases for JWT validation, including:
- Expired tokens
- Tokens with invalid signatures
- Tokens with incorrect issuer
- Malformed tokens
```

### Chore

```
chore(deps): upgrade fastapi to version 0.100.0

Upgraded the FastAPI dependency to the latest version to leverage new performance improvements and features.
```

Please generate all commit messages following these guidelines precisely.
