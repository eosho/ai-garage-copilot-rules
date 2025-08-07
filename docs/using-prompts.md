# Using Prompts

This guide explains how to use the prompt files to execute structured workflows for rapid solution development.

## What are Prompts?

Prompt files (`.prompt.md`) are specialized instructions that guide GitHub Copilot through specific workflows like:

- Gathering requirements for new ideas
- Creating development plans
- Designing solution architecture
- Generating code prototypes

## Available Prompts

### Workflow Prompts
Located in `.github/prompts/`:

- **`new-idea.prompt.md`** - Transform ideas into Product Requirements Documents
- **`development-plan.prompt.md`** - Create detailed project plans with features and tasks
- **`solution-architecture.prompt.md`** - Design technical architecture and system design
- **`start-prototyping.prompt.md`** - Guide prototype development approach

### Utility Prompts
- **`code-review.prompt.md`** - Comprehensive code review following project standards

## How to Run Prompts

### Method 1: Command Palette (Recommended)

1. **Open Command Palette**: `Ctrl+Shift+P` (Windows) or `Cmd+Shift+P` (Mac)
2. **Type**: "Chat: Run Prompt"
3. **Select**: Choose your desired prompt file from the list
4. **Follow the conversation**: Answer questions as Copilot guides you through the process

### Method 2: Chat Interface

1. **Open Copilot Chat**: Click the chat icon in VS Code sidebar
2. **Reference prompt**: Type `@workspace` followed by prompt reference
3. **Example**: `@workspace Follow the new-idea.prompt.md process for my mobile app idea`

### Method 3: Inline Chat

1. **Open inline chat**: `Ctrl+I` (Windows) or `Cmd+I` (Mac)
2. **Reference prompt**: Type `@workspace` and reference the prompt file
3. **Example**: `@workspace Use start-prototyping.prompt.md to create user management API`

## Workflow Execution

### Complete Development Workflow

#### 1. New Idea → PRD
**Prompt**: `new-idea.prompt.md`
**Purpose**: Transform raw ideas into structured Product Requirements Documents
**Output**: `PRD.md` file with comprehensive requirements

**Example Usage**:
```
Run Command: Chat: Run Prompt → new-idea.prompt.md
Input: "I want to build a task management app for remote teams"
Process: Answer discovery questions about users, features, constraints
Output: Detailed PRD.md with specifications
```

#### 2. PRD → Development Plan
**Prompt**: `development-plan.prompt.md`
**Purpose**: Break down requirements into actionable development tasks
**Output**: `Development-Plan.md` with features, tasks, and timelines

**Example Usage**:
```
Run Command: Chat: Run Prompt → development-plan.prompt.md
Input: Reference the generated PRD.md
Process: Answer questions about team, timeline, technical preferences
Output: Structured plan with sprints and task breakdown
```

#### 3. Plan → Architecture
**Prompt**: `solution-architecture.prompt.md`
**Purpose**: Design technical architecture and system components
**Output**: Architecture documentation and diagrams

**Example Usage**:
```
Run Command: Chat: Run Prompt → solution-architecture.prompt.md
Input: Reference PRD and Development Plan
Process: Answer technical constraint and preference questions
Output: System architecture with component diagrams
```

#### 4. Architecture → Prototype
**Prompt**: `start-prototyping.prompt.md`
**Purpose**: Begin implementation with guided prototype development
**Output**: Working prototype code

**Example Usage**:
```
Run Command: Chat: Run Prompt → start-prototyping.prompt.md
Input: Choose prototype type (API, CLI, UI)
Process: Follow guided code generation
Output: Functional prototype following project standards
```

## Prompt File Structure

### Front Matter
Each prompt includes metadata:

```yaml
---
description: "What this prompt accomplishes"
mode: "ask"  # or "agent"
---
```

### Content Structure
1. **Context setting** - What the prompt will help accomplish
2. **Process explanation** - How the conversation will flow
3. **Question categories** - What areas will be explored
4. **Expected deliverables** - What files or outputs will be generated

## Best Practices

### Before Running Prompts
1. **Have context ready** - Know your basic idea or requirements
2. **Prepare details** - Think about users, constraints, preferences
3. **Clear workspace** - Ensure you're in the right project directory
4. **Read prompt description** - Understand what the prompt will accomplish

### During Prompt Execution
1. **Be specific** - Provide detailed answers to questions
2. **Ask for clarification** - If a question isn't clear, ask for examples
3. **Reference existing work** - Point to PRDs, plans, or code when relevant
4. **Iterate** - Run prompts multiple times to refine outputs

### After Prompt Completion
1. **Review outputs** - Check generated files for completeness
2. **Save work** - Commit generated documents to version control
3. **Share with team** - Use outputs for team collaboration
4. **Plan next steps** - Move to the next workflow stage

## Examples

### New Feature Development
```
Scenario: Adding user authentication to existing app

1. Run: new-idea.prompt.md
   Input: "Add OAuth2 authentication with social login"
   Output: PRD.md with auth requirements

2. Run: development-plan.prompt.md
   Input: Reference auth PRD
   Output: Development plan with auth tasks

3. Run: solution-architecture.prompt.md
   Input: Reference PRD and plan
   Output: Auth system architecture

4. Run: start-prototyping.prompt.md
   Input: Provide PRD and choose API prototype type
   Output: Complete auth endpoints and middleware
```

### Code Review Process
```
Scenario: Reviewing a pull request

1. Select code to review
2. Run: code-review.prompt.md
3. Copilot analyzes code against project standards
4. Receive detailed feedback and suggestions
5. Apply recommendations before merging
```

### API Development
```
Scenario: Building new API endpoints

1. Run: start-prototyping.prompt.md
2. Provide PRD or specify requirements (e.g., "Product CRUD API")
3. Answer questions about validation, authentication, technology preferences
4. Receive complete working prototype with:
   - Pydantic models and validation
   - API routers and endpoints
   - Error handling and logging
   - Documentation and tests
```

## Troubleshooting

### Prompt Not Found
- **Check file path** - Ensure prompt file exists in `.github/prompts/`
- **Restart VS Code** - Reload window to refresh prompt cache
- **Check spelling** - Verify prompt filename is correct

### Incomplete Responses
- **Provide more context** - Give detailed answers to questions
- **Break down complex requests** - Use multiple prompts for large projects
- **Reference existing files** - Point to PRDs, plans, or documentation

### Unexpected Outputs
- **Review prompt description** - Ensure prompt matches your needs
- **Check instruction files** - Verify underlying instructions are correct
- **Iterate with refinements** - Run prompt again with clearer inputs

## Customization

### Creating Custom Prompts
1. **Create new `.prompt.md` file** in `.github/prompts/`
2. **Add front matter** with description and mode
3. **Structure conversation flow** with clear questions and expected outputs
4. **Test with various inputs** to ensure robust behavior

### Modifying Existing Prompts
1. **Edit prompt file content** to adjust questions or process
2. **Update front matter** if behavior changes
3. **Test modifications** with sample scenarios
4. **Document changes** for team awareness

### Team-Specific Workflows
- **Customize question sets** for your domain
- **Add company-specific requirements** to prompts
- **Create shortcuts** for frequently used workflows
- **Integrate with existing tools** and processes

This structured approach to prompts enables rapid, consistent development from initial idea through to working prototype, ensuring all team members follow the same proven workflow patterns.
