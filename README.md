# AI Garage Copilot Development Pattern

A comprehensive agentic development pattern that enables rapid, production-grade solution development using GitHub Copilot with structured instructions, prompts, and workflows.

## What This Is

This repository provides a framework for **agentic development** - a structured approach to software development where AI agents (like GitHub Copilot) are guided by explicit instructions and workflows to generate production-ready code that follows established patterns and standards.

The pattern consists of three core components:

1. **📋 Instructions** - Coding standards and best practices that automatically guide Copilot
2. **🚀 Prompts** - Structured workflows for moving from idea to implementation
3. **⚙️ Configuration** - VS Code settings that integrate everything seamlessly

## Why Use This Pattern

- **🏃‍♂️ Rapid Development** - Go from idea to working prototype in minutes, not hours
- **🎯 Consistent Quality** - Every generated piece of code follows the same high standards
- **🔒 Security First** - Built-in security practices and validation patterns
- **📚 Production Ready** - Includes error handling, logging, testing, and documentation
- **🔄 Scalable Process** - Works for individual features or entire applications
- **👥 Team Alignment** - Shared standards ensure consistent code across team members

## Quick Start

1. **Clone or copy this repository structure** to your project
2. **Open in VS Code** - The instructions will be automatically applied
3. **Start with an idea** - Run the `new-idea.prompt.md` workflow
4. **Follow the guided process** - Each stage builds on the previous one

## Documentation

For detailed information on how to use this development pattern:

- **📖 [Using Instructions](docs/using-instructions.md)** - How instruction files automatically guide Copilot
- **🚀 [Using Prompts](docs/using-prompts.md)** - Step-by-step guide to running workflows
- **📋 [Workflow Guide](docs/workflow-guide.md)** - Complete process from idea to implementation

## Core Workflow

The agentic development process follows a proven 4-stage workflow:

### 1. 💡 Idea Discovery
**Prompt**: `new-idea.prompt.md`
Transform raw concepts into structured Product Requirements Documents through guided discovery questions.

### 2. 📋 Development Planning
**Prompt**: `development-plan.prompt.md`
Break down requirements into actionable tasks, features, and sprint plans.

### 3. 🏗️ Solution Architecture
**Prompt**: `solution-architecture.prompt.md`
Design technical architecture and select appropriate technology stack.

### 4. ⚡ Rapid Prototyping
**Prompt**: `start-prototyping.prompt.md`
Generate working code that follows all established patterns and standards.

## Current Implementation

This repository includes a complete **Python/FastAPI** implementation as an example of the pattern in action, including:

- ✅ **10 Python instruction files** covering everything from basic syntax to performance optimization
- ✅ **6 workflow prompts** for end-to-end development
- ✅ **Security-first practices** built into every instruction
- ✅ **Production-ready patterns** with error handling, logging, and testing
- ✅ **Comprehensive documentation** with step-by-step guides

## Key Features

### Automatic Code Standards
- **Type hints and validation** for all functions and classes
- **Comprehensive error handling** with appropriate exception types
- **Security-first patterns** with input validation and sanitization
- **Performance optimization** including async/await patterns and caching
- **Complete documentation** with examples and usage guidelines

### Production-Ready Practices
- **Virtual environment management** with UV dependency management
- **Structured logging** with correlation IDs and proper formatting
- **Comprehensive testing** with pytest patterns and fixtures
- **Git commit conventions** following conventional commit standards
- **Code review automation** with built-in quality checklists

### Extensible Design
- **Language-agnostic structure** - Easily adaptable to other programming languages
- **Modular instructions** - Add new coding standards without disrupting existing ones
- **Customizable workflows** - Modify prompts to match your team's specific needs
- **Integration-friendly** - Works with existing development tools and processes

## Repository Structure

```
ai-garage-copilot-rules/
├── .github/                          # GitHub-specific configurations
│   ├── copilot-instructions.md       # Main instruction file
│   ├── instructions/                 # Automated instruction files
│   │   ├── python/                   # Python-specific guidelines
│   │   └── shared/                   # Language-agnostic standards
│   └── prompts/                      # Workflow prompt files
├── .vscode/                          # VS Code configuration
│   └── settings.json                 # Copilot integration settings
├── docs/                             # Comprehensive documentation
│   ├── using-instructions.md         # Instruction file guide
│   ├── using-prompts.md             # Prompt execution guide
│   └── workflow-guide.md            # End-to-end process guide
├── samples/                          # Example implementations
└── README.md                        # This file
```

## Adapting for Other Languages

While the current implementation focuses on Python/FastAPI, the pattern is designed to be language-agnostic:

1. **Create language-specific instruction directories** (e.g., `.github/instructions/typescript/`)
2. **Add language sections to VS Code settings** (e.g., `"[typescript]"`)
3. **Develop language-specific prompts** for common frameworks and patterns
4. **Update the main copilot instructions** to reference new language guidelines

## Contributing

This pattern is designed to evolve with your team's needs:

- **Add new instruction files** for domain-specific patterns
- **Create custom prompts** for your common workflows
- **Enhance existing instructions** based on code review feedback
- **Share improvements** that could benefit other teams

## License

This project is provided as-is for teams looking to implement agentic development patterns. Adapt, modify, and extend as needed for your specific requirements.

---

**Ready to start?** Check out the [Using Prompts](docs/using-prompts.md) guide to begin your first agentic development workflow.
