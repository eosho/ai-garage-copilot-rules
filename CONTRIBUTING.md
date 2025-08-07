# Contributing to AI Garage Copilot Rules

Thank you for your interest in contributing to the AI Garage Copilot Rules project! This repository contains coding instructions, prompts, and best practices for GitHub Copilot to enhance development workflows.

## 🎯 Project Overview

This project provides:
- **Coding Instructions**: Language-specific guidelines in `.github/instructions/`
- **Interactive Prompts**: Workflow prompts in `.github/prompts/`
- **Documentation**: Comprehensive guides in `docs/`
- **VS Code Integration**: Settings and configurations for optimal Copilot experience

## 🚀 Getting Started

### Prerequisites
- Git installed and configured
- VS Code with GitHub Copilot extension
- Basic understanding of GitHub Copilot workflows

### Setting Up Development Environment

1. **Fork and Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-garage-copilot-rules.git
   cd ai-garage-copilot-rules
   ```

2. **Enable Instructions in VS Code**
   - Copy `.vscode/settings.json` to your workspace
   - Restart VS Code to apply Copilot instruction settings

3. **Test the Setup**
   - Open any Python file and verify Copilot uses the custom instructions
   - Try running one of the prompts from `.github/prompts/`

## 📝 How to Contribute

### Types of Contributions

1. **Coding Instructions** (`.github/instructions/`)
   - Language-specific best practices
   - Framework guidelines
   - Security and performance patterns

2. **Interactive Prompts** (`.github/prompts/`)
   - Workflow automation prompts
   - Development process guides
   - Architecture and design prompts

3. **Documentation** (`docs/`)
   - Usage guides
   - Examples and tutorials
   - Workflow documentation

4. **VS Code Configuration**
   - Settings optimization
   - Extension recommendations
   - Workspace configuration

### Contribution Process

#### 1. Choose Your Contribution Type

**🔧 Adding New Instructions**
- Create `.instructions.md` files in appropriate language folders
- Follow the established format and structure
- Include practical examples and code snippets

**🤖 Creating New Prompts**
- Create `.prompt.md` files in `.github/prompts/`
- Include proper YAML front matter with metadata
- Make prompts interactive with discovery questions

**📚 Improving Documentation**
- Update guides in `docs/` folder
- Add examples and use cases
- Improve clarity and completeness

#### 2. File Naming Conventions

**Instructions Files:**
```
.github/instructions/{language}/{topic}.instructions.md
```
Examples:
- `.github/instructions/python/testing.instructions.md`
- `.github/instructions/typescript/react.instructions.md`

**Prompt Files:**
```
.github/prompts/{workflow-name}.prompt.md
```
Examples:
- `.github/prompts/api-development.prompt.md`
- `.github/prompts/database-design.prompt.md`

#### 3. Required File Structure

**Instructions Files:**
```markdown
---
description: "Brief description of the instructions"
applyTo: "**/*.py"  # File pattern where instructions apply
---

# Title

## Section 1
Content with examples...

## Example
```language
// Code example
```
```

**Prompt Files:**
```markdown
---
description: "Brief description of the prompt"
mode: "ask|agent"  # ask = interactive, agent = autonomous
model: "gpt-4"     # Optional: specific model requirement
tools: ["tool1"]   # Optional: required tools
---

# Prompt Title

Prompt content with clear instructions...
```

### 4. Quality Standards

#### Code Quality
- Follow language-specific best practices
- Include comprehensive examples
- Ensure code is production-ready
- Add proper error handling and validation

#### Documentation Standards
- Use clear, concise language
- Include practical examples
- Provide context and rationale
- Keep content up-to-date

#### Prompt Guidelines
- Make prompts interactive and discoverable
- Include discovery questions for "ask" mode prompts
- Provide clear success criteria
- Ensure prompts are reusable across projects

## 🧪 Testing Your Contributions

### Testing Instructions
1. **Apply Instructions**: Create a test file matching the `applyTo` pattern
2. **Verify Behavior**: Confirm Copilot follows the new instructions
3. **Test Examples**: Ensure all code examples work correctly

### Testing Prompts
1. **Run Prompts**: Test prompts in VS Code with Copilot
2. **Verify Interactivity**: Ensure "ask" mode prompts ask appropriate questions
3. **Check Output**: Confirm "agent" mode prompts produce expected results

### Testing Documentation
1. **Follow Guides**: Walk through documentation step-by-step
2. **Verify Links**: Ensure all links and references work
3. **Test Examples**: Confirm all examples are accurate

## 📋 Submission Guidelines

### Pull Request Process

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-contribution-name
   ```

2. **Make Your Changes**
   - Follow the file structure and naming conventions
   - Include comprehensive documentation
   - Add examples and test cases

3. **Commit with Clear Messages**
   ```bash
   git commit -m "feat: add Python async performance instructions"
   git commit -m "docs: update prompt usage examples"
   git commit -m "fix: correct TypeScript interface guidelines"
   ```

4. **Test Thoroughly**
   - Verify instructions work with Copilot
   - Test prompts end-to-end
   - Check documentation accuracy

5. **Submit Pull Request**
   - Use descriptive title and description
   - Reference any related issues
   - Include testing steps

### Pull Request Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] New coding instructions
- [ ] New interactive prompt
- [ ] Documentation update
- [ ] Configuration improvement
- [ ] Bug fix

## Testing Checklist
- [ ] Instructions tested with Copilot
- [ ] Prompts tested end-to-end
- [ ] Documentation verified
- [ ] Examples work correctly

## Additional Notes
Any additional context or considerations
```

## 🏷️ Coding Standards

### Language-Specific Guidelines
- **Python**: Follow PEP 8, use type hints, include docstrings
- **TypeScript**: Use strict mode, prefer interfaces over types
- **JavaScript**: Use modern ES6+ syntax, include JSDoc
- **General**: Security-first, performance-optimized, well-documented

### Documentation Standards
- Use clear headings and structure
- Include practical examples
- Provide context and rationale
- Keep content concise but comprehensive

### Prompt Design Principles
- Make prompts discoverable through questions
- Include clear success criteria
- Ensure reusability across projects
- Provide comprehensive output specifications

## 🐛 Reporting Issues

### Bug Reports
Use the issue template to report:
- Instructions not working with Copilot
- Prompts producing incorrect output
- Documentation inaccuracies
- Configuration problems

### Feature Requests
Suggest improvements for:
- New language support
- Additional workflow prompts
- Enhanced documentation
- Better VS Code integration

## 💬 Community Guidelines

### Code of Conduct
- Be respectful and inclusive
- Provide constructive feedback
- Help others learn and grow
- Focus on improving the project

### Communication
- Use clear, professional language
- Provide context for suggestions
- Be patient with new contributors
- Share knowledge and experience

## 🏆 Recognition

Contributors will be recognized through:
- GitHub contributor statistics
- Mentions in release notes
- Community acknowledgments
- Project documentation credits

## 📚 Additional Resources

### Learning Materials
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Guide](https://code.visualstudio.com/docs/editor/github-copilot)
- [Project Documentation](./docs/)

### Getting Help
- Create an issue for questions
- Check existing documentation
- Review similar contributions
- Ask in discussions

---

**Thank you for contributing to AI Garage Copilot Rules!** Your contributions help developers worldwide build better software faster. 🚀
