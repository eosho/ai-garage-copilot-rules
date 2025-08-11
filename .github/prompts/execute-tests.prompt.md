---
description: "Execute development tests to make sure everything is working correctly."
mode: "agent"
---

# Test Automation and Fixing Prompt

## Context

This prompt is designed to execute tests, analyze failures, and iteratively fix issues until all tests pass successfully. The approach varies based on project type and scope.

## Project Types

1. **Greenfield Project**:
   - Comprehensive test setup
   - Full CI/CD integration
   - Complete code coverage goals
   - Extensive documentation

2. **Existing Project**:
   - Focus on affected areas
   - Match existing patterns
   - Minimal disruption
   - Targeted fixes

## Response Levels

1. **Quick Check** (default):
   - Focus on specific file/error
   - Minimal tool usage
   - Fast iteration cycle
   - Basic validation

2. **Standard Analysis**:
   - Related file checks
   - Common edge cases
   - Test dependencies
   - Basic regression testing

3. **Deep Dive**:
   - Full repository analysis
   - All edge cases
   - Complete regression testing
   - Performance impact

## Workflow

1. **Test Execution**: Run tests and capture failures
2. **Analysis**: Analyze each failure to determine root cause
3. **Fix Strategy**: Develop solutions for each failure
4. **Implementation**: Apply fixes methodically
5. **Verification**: Re-run tests to confirm fixes
6. **Iteration**: Repeat until all tests pass

## Commands

Execute the workflow with:
```
#test-automation
goal: Execute and fix tests
project: [greenfield|existing]
scope: [path to test files or directory]
mode: [quick|standard|deep]
```

Examples:

Quick check for existing project:
```
#test-automation
goal: Execute and fix tests
project: existing
scope: ./tests/test_api.py
mode: quick
```

Full analysis for greenfield project:
```
#test-automation
goal: Execute and fix tests
project: greenfield
scope: ./tests
mode: deep
```

## Analyzing Test Failures

For each test failure, analyze:

1. **Error Type**:
   - Import errors
   - Assertion failures
   - Type errors
   - Runtime errors

2. **Context**:
   - Test setup
   - Fixtures
   - Dependencies
   - Environment configuration

3. **Root Cause Categories**:
   - Configuration issues
   - Environment setup
   - Code logic
   - Test data
   - Dependencies
   - Async/sync issues
   - Resource cleanup

## Common Fixes

### Import Errors
1. Check project structure
2. Verify PYTHONPATH
3. Check package installation
4. Update import statements

### Assertion Failures
1. Check test data
2. Verify test setup
3. Review business logic
4. Update assertions

### Type Errors
1. Update type hints
2. Fix parameter types
3. Add type conversions
4. Update fixture types

### Runtime Errors
1. Check resource cleanup
2. Verify async/await usage
3. Check error handling
4. Review state management

## Fix Implementation Strategy

1. **Prioritize Fixes**:
   - Fix environment/setup issues first
   - Address import errors next
   - Fix type errors
   - Address logic errors
   - Fix assertion failures

2. **Apply Fixes**:
   - One error type at a time
   - Most critical first
   - Least invasive solutions first
   - Document changes

3. **Verify Fixes**:
   - Run affected tests
   - Check for regressions
   - Verify error resolution

## Best Practices

1. **Test Isolation**:
   - Each test should be independent
   - Clean up resources after tests
   - Use fresh fixtures for each test

2. **Error Handling**:
   - Use appropriate assertions
   - Handle expected errors
   - Clean up in finally blocks

3. **Async Testing**:
   - Use proper async fixtures
   - Await all async operations
   - Clean up async resources

4. **Configuration**:
   - Use test-specific settings
   - Mock external services
   - Use appropriate test data

## Example Workflow

1. Initial run:
```python
# Run tests
pytest --verbose

# Analyze failures
for failure in failures:
    analyze_error_type(failure)
    determine_root_cause(failure)
    propose_fix(failure)

# Apply fixes systematically
for fix in prioritized_fixes:
    apply_fix(fix)
    verify_fix(fix)
    run_affected_tests(fix)

# Final verification
pytest --verbose
```

## Common Fix Patterns

### Import Error Fix
```python
# Before
from app import module

# After
from myproject.app import module
```

### Async Fixture Fix
```python
# Before
@pytest.fixture
async def client():
    yield AsyncClient()

# After
@pytest.fixture
async def client():
    async with AsyncClient() as c:
        yield c
```

### Resource Cleanup Fix
```python
# Before
def test_resource():
    resource = create_resource()
    use_resource(resource)

# After
def test_resource():
    resource = create_resource()
    try:
        use_resource(resource)
    finally:
        cleanup_resource(resource)
```

### Type Error Fix
```python
# Before
def test_data(data: dict):
    process(data)

# After
def test_data(data: Dict[str, Any]):
    process(cast(Dict[str, Any], data))
```

## Success Criteria

Tests are considered fixed when:
1. All tests pass
2. No warnings or errors
3. Resources properly cleaned up
4. No regressions introduced
5. Code quality maintained

## Maintenance

After fixing:
1. Document fixes applied
2. Update test documentation
3. Add new test cases if needed
4. Review test performance
5. Update test dependencies
