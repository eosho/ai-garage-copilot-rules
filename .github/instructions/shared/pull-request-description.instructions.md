---
applyTo: "**"
description: "Guidelines for generating comprehensive pull request descriptions."
---

# Pull Request Description Generation

When generating a pull request description, follow this structure to ensure clarity, context, and completeness.

## 1. Description
Provide a clear and concise summary of the changes. Explain the "why" behind the changes, not just the "what." Describe the problem this PR solves and the approach taken.

## 2. Type of Change
Use a checklist to indicate the nature of the changes. This helps reviewers quickly understand the scope.

- [ ] **Bug fix** (non-breaking change which fixes an issue)
- [ ] **New feature** (non-breaking change which adds functionality)
- [ ] **Breaking change** (fix or feature that would cause existing functionality to not work as expected)
- [ ] **Documentation** (changes to documentation only)
- [ ] **Refactoring** (non-breaking change that neither fixes a bug nor adds a feature)
- [ ] **Performance** (non-breaking change that improves performance)
- [ ] **Build** (changes that affect the build system or external dependencies)

## 3. Testing Checklist
Detail the testing that has been performed to validate the changes. Be specific about the scenarios covered.

- [ ] New unit tests added to cover the changes.
- [ ] Existing unit tests pass locally with my changes.
- [ ] Manual testing performed for the following scenarios:
  - Scenario A: ...
  - Scenario B: ...
- [ ] All automated tests passed in the CI pipeline.

## 4. Related Issues
Link to any related issues, tickets, or user stories. Use keywords like "Closes," "Fixes," or "Resolves" to automatically close the corresponding issue upon merging.

- Closes #123
- Relates to #456

## Example Output

### Description
This PR introduces a new caching layer for the user profile endpoint (`/api/users/{id}`). It uses Redis to cache user data for 15 minutes, significantly reducing database load and improving response times for repeated requests.

### Type of Change
- [x] New feature
- [x] Performance

### Testing Checklist
- [x] New unit tests added for the `RedisCacheService`.
- [x] Existing unit tests pass locally with my changes.
- [x] Manual testing performed for the following scenarios:
  - Verified that a cache miss results in a database query.
  - Verified that a subsequent request results in a cache hit.
  - Verified that updating a user invalidates the cache.
- [x] All automated tests passed in the CI pipeline.

### Related Issues
- Closes #78
