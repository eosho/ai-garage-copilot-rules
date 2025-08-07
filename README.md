# Agentic Development Pattern for GitHub Copilot

This repository provides a comprehensive, production-grade pattern for guiding GitHub Copilot to build secure, scalable, and maintainable applications. It provides a structured framework of instructions, prompts, and configurations to ensure consistency, quality, and adherence to best practices across any development team and technology stack.

The primary goal is to leverage GitHub Copilot effectively by providing it with a rich, project-specific context of coding standards, architectural patterns, and security requirements. This enables Copilot to generate code that is not only functional but also perfectly aligned with your team's established practices.

## Core Concepts

This pattern is built on three core concepts for customizing Copilot's behavior:

1.  **Instructions (`.github/instructions`)**: These files are the foundation of your coding standards. They contain the specific rules, best practices, and style guides for your project. By creating granular instruction files for different aspects of your codebase (e.g., error handling, testing, documentation), you can provide Copilot with a detailed "rulebook" to follow.

2.  **Prompts (`.github/prompts`)**: These are powerful, reusable templates for automating complex and repetitive development tasks. Prompts can be chained together to create sophisticated, standardized workflows for activities like planning new features, generating boilerplate code, or performing comprehensive code reviews.

3.  **Configuration (`.vscode/settings.json`)**: This file wires everything together. It tells the VS Code Copilot extension where to find your instruction and prompt files and how to apply them, whether globally, for specific languages, or for particular tasks like generating commit messages.

## How to Use This Repository

This repository is a template that can be adapted for any project or language.

1.  **Explore the Structure**: Familiarize yourself with the directories and the example files within them.
    *   `.github/instructions/`: Contains coding standards. Note the `shared` and `python` subdirectories as an example of organizing rules.
    *   `.github/prompts/`: Contains reusable workflow prompts.
    *   `.vscode/settings.json`: Contains the configuration that activates the instructions and prompts.
2.  **Adapt for Your Project**:
    *   Modify or replace the example instruction files in `.github/instructions` with your own team's standards for your chosen language (e.g., C#, Go, TypeScript).
    *   Customize the workflow prompts in `.github/prompts` to match your development process.
    *   Update `.vscode/settings.json` to point to your new or modified instruction files.

## Example Implementation: Python & FastAPI

To demonstrate the pattern in a real-world scenario, this repository comes pre-configured with a set of instructions and prompts for a modern Python backend stack.

-   **Technology Stack**: FastAPI, Pydantic, and SQLAlchemy.
-   **Instructions**: The `.github/instructions/python/` directory contains specific rules for Python development, covering topics from function definitions and error handling to testing with `pytest`.
-   **Prompts**: The prompts in `.github/prompts/` are tailored for this stack, including a powerful prompt for generating complete FastAPI CRUD endpoints.

This example serves as a practical guide for creating your own set of customizations.

## Core Development Principles

While the implementation can change, the guiding principles of this pattern are universal:

-   **Security First**: All code must be developed with security as the primary consideration.
-   **Production Ready**: Code should be deployment-ready with proper error handling, logging, and documentation.
-   **Customer Adaptable**: Solutions should be flexible and configurable to meet diverse requirements.
-   **Documentation Driven**: All code must be thoroughly documented with clear explanations and examples.

By adopting this pattern, you can transform GitHub Copilot from a simple code completion tool into a true pair programmer that understands and adheres to your team's unique way of working.
