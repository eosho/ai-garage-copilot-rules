---
applyTo: "**"
---

# Code Review Checklist Instructions

**Keywords**: #code-review #quality #standards #checklist #best-practices

---

## 🔍 Code Review Rule Directives

### General Code Quality

```
@review Rule - Readability First: Code should be written for humans to read, not just machines to execute.
```

```
@review Rule - Single Responsibility: Each function, class, and module should have a single, well-defined responsibility.
```

```
@review Rule - DRY Principle: Don't repeat yourself - extract common functionality into reusable components.
```

```
@review Rule - KISS Principle: Keep it simple, stupid - prefer simple solutions over complex ones.
```

```
@review Rule - YAGNI Principle: You aren't gonna need it - don't implement features until they're actually needed.
```

### Security Review

```
@review Rule - Security Validation: Verify all input validation, authentication, and authorization implementations.
```

```
@review Rule - Secret Management: Ensure no hardcoded secrets, passwords, or API keys in the code.
```

```
@review Rule - SQL Injection Check: Verify parameterized queries are used instead of string concatenation.
```

```
@review Rule - XSS Prevention Check: Verify output encoding and CSP implementation for web applications.
```

### Performance Review

```
@review Rule - Performance Impact: Consider the performance impact of changes, especially in critical paths.
```

```
@review Rule - Resource Management: Verify proper disposal of resources (database connections, file handles, etc.).
```

```
@review Rule - Async Patterns: Ensure proper use of async/await patterns and avoid blocking calls.
```

```
@review Rule - Database Efficiency: Review database queries for efficiency and proper indexing.
```

### Testing Review

```
@review Rule - Test Coverage: Ensure adequate test coverage for new and modified code.
```

```
@review Rule - Test Quality: Review test code for clarity, maintainability, and correctness.
```

```
@review Rule - Edge Cases: Verify tests cover edge cases and error conditions.
```

```
@review Rule - Integration Tests: Ensure integration tests cover critical user workflows.
```

## 📋 Comprehensive Review Checklist

### 🔧 Functionality
- [ ] Code meets all requirements specified in the task/issue
- [ ] All acceptance criteria are satisfied
- [ ] Edge cases and error conditions are handled
- [ ] Code follows the expected business logic
- [ ] Integration points work correctly

### 🏗️ Architecture & Design
- [ ] Code follows established architectural patterns
- [ ] Dependencies are properly managed and injected
- [ ] Separation of concerns is maintained
- [ ] Code follows SOLID principles
- [ ] Design patterns are used appropriately

### 🎯 Code Quality
- [ ] Code is readable and self-documenting
- [ ] Variable and function names are descriptive
- [ ] Functions are small and focused
- [ ] Code complexity is manageable
- [ ] Magic numbers and strings are avoided

### 🔐 Security
- [ ] Input validation is implemented correctly
- [ ] Output encoding prevents XSS
- [ ] SQL injection is prevented
- [ ] Authentication and authorization are correct
- [ ] Sensitive data is handled properly
- [ ] No secrets in code or logs

### ⚡ Performance
- [ ] No obvious performance bottlenecks
- [ ] Database queries are optimized
- [ ] Async operations are used appropriately
- [ ] Memory usage is reasonable
- [ ] Caching is implemented where beneficial

### 🧪 Testing
- [ ] Unit tests cover new/modified code
- [ ] Tests are meaningful and not trivial
- [ ] Integration tests cover critical paths
- [ ] Test names clearly describe what they test
- [ ] Mocks and stubs are used appropriately

### 📚 Documentation
- [ ] Code is properly documented
- [ ] API changes are documented
- [ ] README is updated if necessary
- [ ] Breaking changes are noted
- [ ] Examples are provided for complex features

### 🔄 Maintainability
- [ ] Code follows project conventions
- [ ] Error handling is consistent
- [ ] Logging is appropriate and informative
- [ ] Configuration is externalized
- [ ] Code is version control friendly

### 🚀 DevOps & Deployment
- [ ] CI/CD pipelines pass
- [ ] Database migrations are safe
- [ ] Environment configurations are correct
- [ ] Monitoring and alerting are configured
- [ ] Rollback procedures are considered

## 🔬 Technology-Specific Checks

### Python-Specific
- [ ] PEP 8 style guidelines followed
- [ ] Type hints are used appropriately
- [ ] Virtual environments are used
- [ ] Requirements are properly specified
- [ ] Error handling uses appropriate exceptions

### .NET-Specific
- [ ] C# coding conventions followed
- [ ] Proper use of nullable reference types
- [ ] Dependency injection configured correctly
- [ ] Entity Framework queries are efficient
- [ ] Proper exception handling implemented

### Frontend-Specific
- [ ] Component structure is logical
- [ ] State management is appropriate
- [ ] Accessibility standards met
- [ ] Performance optimizations implemented
- [ ] Cross-browser compatibility considered

### API-Specific
- [ ] RESTful principles followed
- [ ] HTTP status codes used correctly
- [ ] Request/response schemas validated
- [ ] Rate limiting implemented
- [ ] API versioning considered

## 🚨 Critical Issues (Must Fix)

### Security Critical
- Exposed secrets or credentials
- SQL injection vulnerabilities
- XSS vulnerabilities
- Authentication bypasses
- Authorization failures

### Functionality Critical
- Code doesn't meet requirements
- Breaking changes without migration
- Data corruption risks
- Memory leaks or resource leaks
- Critical business logic errors

### Performance Critical
- Blocking operations in async code
- N+1 query problems
- Unbounded resource usage
- Inefficient algorithms in hot paths
- Missing database indexes

## 💡 Review Best Practices

### For Reviewers
- Be constructive and specific in feedback
- Explain the "why" behind suggestions
- Distinguish between must-fix and nice-to-have
- Review code in small, focused chunks
- Consider the broader impact of changes

### For Authors
- Provide context in pull request descriptions
- Respond to feedback promptly and professionally
- Ask questions when feedback isn't clear
- Make requested changes in separate commits
- Thank reviewers for their time and input

## 📊 Review Metrics

### Quality Metrics
- Defect density (bugs per KLOC)
- Code coverage percentage
- Technical debt ratio
- Security vulnerability count
- Performance regression incidents

### Process Metrics
- Average review time
- Review participation rate
- Rework percentage
- Review comments per change
- Time to fix issues

## 🎯 Review Outcomes

### Approved ✅
- Code meets all standards
- No critical issues identified
- Minor suggestions addressed
- Ready for deployment

### Approved with Comments 🔄
- Code is acceptable overall
- Minor improvements suggested
- Non-blocking issues identified
- Can proceed with deployment

### Changes Requested ❌
- Critical issues must be addressed
- Security vulnerabilities found
- Significant quality concerns
- Requires another review round

### Blocked 🛑
- Fundamental design issues
- Major security vulnerabilities
- Doesn't meet requirements
- Requires architectural discussion

---

**Remember**: Code review is a collaborative process aimed at improving code quality, sharing knowledge, and maintaining standards. Focus on the code, not the person, and always be constructive in feedback.
