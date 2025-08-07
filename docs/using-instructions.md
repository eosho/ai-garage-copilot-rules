# Using Instructions

This guide explains how to use the instruction files in this repository to customize GitHub Copilot's behavior for your development projects.

## How Instructions Work

Instruction files (`.instructions.md`) automatically guide GitHub Copilot when generating code. They are applied based on:

1. **File patterns** specified in the `applyTo` front matter
2. **Language-specific settings** in VS Code configuration
3. **Workspace-wide rules** from the main copilot instructions

## Instruction File Structure

### Front Matter
Each instruction file starts with YAML front matter:

```yaml
---
description: "Brief description of what this instruction covers"
applyTo: "**/*.py"  # File pattern where this applies
---
```

### Content
- Clear, concise guidelines
- Practical examples
- Best practices specific to the domain

## Available Instructions

### Python-Specific Instructions
Located in `.github/instructions/python/`:

- **`general.instructions.md`** - PEP 8, naming conventions, project structure
- **`classes.instructions.md`** - Class design and method patterns
- **`functions.instructions.md`** - Function design and return values
- **`error-handling.instructions.md`** - Exception handling patterns
- **`typing.instructions.md`** - Type hints and annotations
- **`documentation.instructions.md`** - Docstring standards
- **`configuration.instructions.md`** - Settings and environment management
- **`imports.instructions.md`** - Import organization and best practices
- **`logging.instructions.md`** - Logging patterns and configuration
- **`testing.instructions.md`** - Pytest patterns and test structure
- **`performance.instructions.md`** - Optimization and async patterns

### Shared Instructions
Located in `.github/instructions/shared/`:

- **`security-first.instructions.md`** - Security-focused development
- **`documentation-standards.instructions.md`** - General documentation guidelines
- **`code-review-checklist.instructions.md`** - Code review standards
- **`git-message.instructions.md`** - Commit message conventions
- **`pull-request-description.instructions.md`** - Pull request description template

## How Instructions are Applied

### Automatic Application
Instructions are automatically applied when:

1. **File type matches** the `applyTo` pattern
2. **Language-specific settings** reference the instruction file
3. **Copilot generates code** in the relevant context

### VS Code Configuration
The `.vscode/settings.json` file configures instruction application:

```json
{
  "[python]": {
    "github.copilot.enable": true,
    "github.copilot.chat.codeGeneration.instructions": [
      { "file": ".github/instructions/python/general.instructions.md" },
      { "file": ".github/instructions/python/functions.instructions.md" },
      // ... other instructions
    ]
  }
}
```

### Manual Reference
You can explicitly reference instructions in chat:

```
@workspace Follow the error-handling.instructions.md patterns
```

## Best Practices

### Writing Effective Instructions
1. **Be specific** - Provide concrete examples
2. **Be concise** - Avoid lengthy explanations
3. **Be consistent** - Follow established patterns
4. **Include examples** - Show both good and bad patterns

### Using Instructions Effectively
1. **Review generated code** - Instructions guide but don't guarantee perfect output
2. **Iterate and refine** - Update instructions based on results
3. **Combine instructions** - Let multiple instruction files work together
4. **Test thoroughly** - Validate that generated code follows your standards

## Troubleshooting

### Instructions Not Applied
1. **Check file patterns** - Ensure `applyTo` matches your files
2. **Verify VS Code settings** - Confirm instruction files are referenced
3. **Restart VS Code** - Reload window to refresh instruction cache
4. **Check file syntax** - Ensure YAML front matter is valid

### Conflicting Instructions
1. **Review overlapping patterns** - Check for conflicting `applyTo` patterns
2. **Prioritize instructions** - More specific patterns take precedence
3. **Consolidate similar rules** - Combine related instructions into single files

### Performance Issues
1. **Limit instruction files** - Too many instructions can slow generation
2. **Keep instructions focused** - Each file should cover specific domain
3. **Use language-specific settings** - Apply instructions only when relevant

## Customization

### Adding New Instructions
1. Create new `.instructions.md` file in appropriate directory
2. Add front matter with description and applyTo pattern
3. Include the file in VS Code settings if needed
4. Test with sample code generation

### Modifying Existing Instructions
1. Edit the instruction file content
2. Keep examples up-to-date
3. Test changes with code generation
4. Update related documentation

### Language-Specific Instructions
To add support for new languages:

1. Create new directory: `.github/instructions/{language}/`
2. Add language-specific instruction files
3. Update `.vscode/settings.json` with new language section
4. Reference instructions in main copilot-instructions.md

## Examples

### Python Function Generation
With instructions active, asking Copilot to "create a function to calculate user age" will automatically:

- Use proper type hints
- Include comprehensive docstring
- Follow PEP 8 naming conventions
- Include error handling
- Add appropriate logging

### API Endpoint Creation
Instructions ensure generated FastAPI endpoints include:

- Input validation with Pydantic models
- Proper HTTP status codes
- Authentication and authorization
- Error handling and logging
- OpenAPI documentation

This systematic approach ensures consistent, production-ready code generation across your entire development team.
