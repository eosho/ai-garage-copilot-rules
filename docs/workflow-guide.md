# Workflow Guide

This guide walks you through the complete agentic development process, from initial idea to production-ready implementation.

## Overview

The agentic development workflow consists of four main stages:

1. **💡 Idea Discovery** - Transform concepts into structured requirements
2. **📋 Development Planning** - Break down requirements into actionable tasks
3. **🏗️ Solution Architecture** - Design technical implementation approach
4. **⚡ Rapid Prototyping** - Generate working code following best practices

Each stage builds upon the previous one, creating a systematic approach to solution development.

## Stage 1: Idea Discovery

### Purpose
Transform raw ideas into comprehensive Product Requirements Documents (PRDs) through structured discovery questions.

### Prompt
**File**: `new-idea.prompt.md`
**Mode**: Interactive questioning

### Process
1. **Run the prompt**:
   ```
   Command Palette → Chat: Run Prompt → new-idea.prompt.md
   ```

2. **Provide your initial idea**:
   - Describe your concept in 1-2 sentences
   - Don't worry about being complete - the prompt will guide you

3. **Answer discovery questions** across these areas:
   - **Problem Definition**: What problem are you solving?
   - **Target Users**: Who will use this solution?
   - **Value Proposition**: What makes this valuable?
   - **Scope & Features**: What functionality is needed?
   - **Business Context**: Budget, timeline, constraints
   - **Success Metrics**: How will you measure success?

### Expected Output
**File**: `PRD.md`
**Contents**:
- Executive Summary
- Problem Statement
- Target Users & Personas
- Solution Overview
- Functional Requirements
- Non-Functional Requirements
- User Stories
- Success Metrics
- Timeline & Milestones
- Budget & Resources
- Risk Assessment

### Example
```
Input: "A mobile app to help remote teams stay connected"

Discovery Questions:
- What specific connection problems do remote teams face?
- What team sizes are you targeting?
- What features would provide the most value?
- How is this different from Slack or Teams?
- What's your budget and timeline?

Output: Comprehensive PRD.md with detailed requirements
```

## Stage 2: Development Planning

### Purpose
Convert PRD requirements into detailed development plans with features broken down into specific, actionable tasks.

### Prompt
**File**: `development-plan.prompt.md`
**Mode**: Interactive planning

### Process
1. **Run the prompt**:
   ```
   Command Palette → Chat: Run Prompt → development-plan.prompt.md
   ```

2. **Reference your PRD**:
   - Provide the path to your PRD.md file
   - Highlight key features and requirements

3. **Answer planning questions**:
   - **Team Context**: Team size, skill levels, availability
   - **Technical Preferences**: Technology stack, existing systems
   - **Timeline Constraints**: Deadlines, milestone requirements
   - **Resource Limitations**: Budget, infrastructure, tools

### Expected Output
**File**: `Development-Plan.md`
**Contents**:
- Project Overview
- Feature Breakdown
- Task Lists with estimates
- Sprint Planning
- Team Assignments
- Timeline & Milestones
- Dependencies & Risks
- Definition of Done

### Example
```
Input: PRD for remote team connection app

Planning Questions:
- How many developers on your team?
- Do you prefer React Native or native development?
- What's your target launch date?
- Do you have existing authentication systems?

Output: Detailed plan with 3 sprints, 45 tasks, 12-week timeline
```

## Stage 3: Solution Architecture

### Purpose
Design the technical architecture, system components, and technology stack based on requirements and development plan.

### Prompt
**File**: `solution-architecture.prompt.md`
**Mode**: Technical design consultation

### Process
1. **Run the prompt**:
   ```
   Command Palette → Chat: Run Prompt → solution-architecture.prompt.md
   ```

2. **Provide project context**:
   - Reference PRD.md and Development-Plan.md
   - Highlight technical requirements and constraints

3. **Answer architecture questions**:
   - **System Characteristics**: Scale, performance, availability
   - **Technical Constraints**: Security, compliance, integration
   - **Technology Preferences**: Language, framework, cloud platform
   - **Team Skills**: Existing expertise and learning capacity

### Expected Output
**Files**:
- Architecture documentation
- System diagrams (text-based, can be converted to visual)
- Technology recommendations
- Infrastructure requirements

### Example
```
Input: PRD and plan for team connection app

Architecture Questions:
- Expected number of concurrent users?
- Real-time messaging requirements?
- Data privacy and security needs?
- Preferred cloud provider?

Output: Microservices architecture with React Native, Node.js, PostgreSQL, Redis, AWS deployment
```

## Stage 4: Rapid Prototyping

### Purpose
Generate working prototype code that follows project standards and demonstrates core functionality.

### Prompt
**File**: `start-prototyping.prompt.md`
**Mode**: Implementation guidance

### Process
1. **Run the prompt**:
   ```
   Command Palette → Chat: Run Prompt → start-prototyping.prompt.md
   ```

2. **Choose prototype type**:
   - **API Endpoints** (FastAPI, Express, ASP.NET)
   - **CLI Tool** (Python Click, Node.js Commander)
   - **UI Component** (React, Vue, Angular)
   - **Database Schema** (SQL, NoSQL)

3. **Follow specialized prompts**:
   - Comprehensive prototyping with dedicated discovery process
   - Example: `start-prototyping.prompt.md` for any prototype type (APIs, web apps, scripts, etc.)

### Expected Output
**Working code** including:
- Core functionality implementation
- Proper error handling
- Security considerations
- Documentation and tests
- Configuration and deployment setup

### Example
```
Input: Team connection app architecture

Prototype Choice: API Endpoints  
Specialized Prompt: start-prototyping.prompt.md

Questions:
- What resources need CRUD operations? (Users, Teams, Messages)
- Authentication requirements? (OAuth2 with JWT)
- Validation needs? (Email format, team size limits)

Output: Complete FastAPI application with:
- User management endpoints
- Team creation and management
- Message posting and retrieval
- Authentication middleware
- Input validation
- Error handling
- API documentation
```

## Workflow Integration

### Sequential Execution
Each stage builds on the previous one:

```
Idea → PRD → Development Plan → Architecture → Prototype
```

### Iterative Refinement
You can revisit any stage to refine outputs:

```
Prototype feedback → Update Architecture → Revise Plan → Enhance PRD
```

### Parallel Development
Some activities can happen in parallel:

```
Architecture Design ←→ Development Planning
Backend Prototype ←→ Frontend Prototype
```

## Best Practices

### Preparation
1. **Clear workspace** - Start in the right project directory
2. **Gather context** - Have any existing requirements or constraints ready
3. **Time allocation** - Plan adequate time for each stage
4. **Team involvement** - Include relevant stakeholders in discovery

### Execution
1. **Follow the sequence** - Each stage builds on the previous one
2. **Be thorough** - Detailed answers lead to better outputs
3. **Document decisions** - Capture rationale for future reference
4. **Review outputs** - Validate generated documents before proceeding

### Iteration
1. **Start simple** - Begin with core functionality
2. **Build incrementally** - Add features in logical order
3. **Test early** - Validate assumptions with prototypes
4. **Gather feedback** - Use stakeholder input to refine approach

## Common Scenarios

### New Product Development
```
1. Product Manager has idea for customer portal
2. Run new-idea.prompt.md → Comprehensive PRD
3. Run development-plan.prompt.md → 6-month roadmap
4. Run solution-architecture.prompt.md → Cloud-native architecture
5. Run start-prototyping.prompt.md → MVP implementation
```

### Feature Enhancement
```
1. Existing app needs mobile API
2. Run new-idea.prompt.md → Mobile feature PRD
3. Run solution-architecture.prompt.md → API design
4. Run start-prototyping.prompt.md → API implementation
5. Integrate with existing system
```

### Technical Debt Reduction
```
1. Legacy system needs modernization
2. Run new-idea.prompt.md → Modernization PRD
3. Run development-plan.prompt.md → Migration strategy
4. Run solution-architecture.prompt.md → Target architecture
5. Run start-prototyping.prompt.md → Pilot implementation
```

### Bug Fix or Optimization
```
1. Performance issue identified
2. Run new-idea.prompt.md → Performance improvement PRD
3. Run solution-architecture.prompt.md → Optimization approach
4. Run start-prototyping.prompt.md → Performance testing setup
5. Implement and measure improvements
```

## Troubleshooting

### Incomplete Requirements
- **Go back to discovery** - Run new-idea.prompt.md again with more detail
- **Break down complex ideas** - Split large concepts into smaller pieces
- **Involve stakeholders** - Get input from users and business stakeholders

### Technical Challenges
- **Revisit architecture** - Run solution-architecture.prompt.md with new constraints
- **Research alternatives** - Ask Copilot about different technical approaches
- **Start smaller** - Reduce scope to manageable prototype

### Resource Constraints
- **Adjust timeline** - Modify development-plan.prompt.md with realistic constraints
- **Prioritize features** - Focus on core value proposition
- **Consider alternatives** - Explore different technical solutions

### Quality Issues
- **Review instruction files** - Ensure coding standards are properly configured
- **Use code review prompts** - Apply code-review.prompt.md to generated code
- **Iterate on implementation** - Refine prototypes based on testing

## Measuring Success

### Stage Completeness
- ✅ **PRD**: Comprehensive requirements document
- ✅ **Plan**: Actionable task breakdown with estimates
- ✅ **Architecture**: Clear technical design and component overview
- ✅ **Prototype**: Working code demonstrating core functionality

### Quality Indicators
- **Clarity**: Stakeholders understand the plan and approach
- **Feasibility**: Technical approach is realistic and achievable
- **Completeness**: All major requirements and constraints are addressed
- **Actionability**: Team can begin implementation immediately

### Business Value
- **Time to market**: Faster delivery of working solutions
- **Quality**: Higher code quality through consistent standards
- **Alignment**: Better stakeholder alignment through structured requirements
- **Risk reduction**: Early identification of technical and business risks

This systematic workflow ensures that every project starts with a solid foundation and progresses through well-defined stages toward successful implementation.
