---
description: "Create a detailed development plan for a new feature or project."
mode: "ask"
model: "Claude Sonnet 4"
---

# Development Plan Creation Prompt

I'll help you create a comprehensive development plan by asking questions about your project and breaking it down into manageable tasks and timelines.

## Planning Approach

When you share your project details, I will:

1. **Ask clarifying questions** about scope, requirements, and constraints
2. **Help define user stories** with clear acceptance criteria
3. **Break down work** into specific, actionable tasks
4. **Estimate effort** and create realistic timelines
5. **Identify dependencies** and potential risks

## Questions I'll Ask

### **Project Context**
- What's the overall goal and scope of this project?
- Who are the stakeholders and what are their expectations?
- What are the key constraints (timeline, resources, technology)?

### **Requirements & Features**
- What are the core features that must be included?
- Are there any existing systems to integrate with?
- What are the performance and scalability requirements?

### **Team & Resources**
- What's your team composition and skill levels?
- What tools and technologies are you already using?
- What's your preferred development methodology (Agile, etc.)?

### **Timeline & Priorities**
- When do you need this delivered?
- What features are highest priority for MVP?
- Are there any critical milestones or dependencies?

## Final Deliverable

After our planning session, I will create a comprehensive **Development-Plan.md** file that includes:

### **Development Plan Structure**
- **Project Overview** - Goals, scope, and success criteria
- **Feature Breakdown** - High-level features organized by priority
- **User Stories** - Detailed user stories with acceptance criteria
- **Task Breakdown** - Each feature broken into specific development tasks
- **Effort Estimation** - Time estimates for each task (hours/story points)
- **Sprint Planning** - Organized sprints with deliverables and timelines
- **Technical Dependencies** - Required integrations and constraints
- **Risk Assessment** - Potential blockers and mitigation strategies
- **Team Assignments** - Who works on what (if team info provided)
- **Definition of Done** - Quality criteria for each deliverable

### **Task Organization**
Features will be broken down into:
- **Frontend Tasks** - UI/UX implementation
- **Backend Tasks** - API and business logic
- **Database Tasks** - Schema design and migrations
- **Integration Tasks** - Third-party services and APIs
- **Testing Tasks** - Unit, integration, and E2E tests
- **DevOps Tasks** - CI/CD, deployment, monitoring

## Let's Start

**Please describe your project or share your PRD, and I'll ask targeted questions to create a detailed development plan with features, tasks, and timelines.**

## 2. **User Stories**

List the user stories that need to be implemented. For each user story, please include:

- A clear description from the user's perspective.
- Acceptance criteria that define when the story is complete.

**Example:**

- **User Story**: As a user, I want to be able to reset my password so that I can access my account if I forget my password.
- **Acceptance Criteria**:
  - User can request a password reset from the login page.
  - User receives an email with a unique, time-limited password reset link.
  - User can set a new password after clicking the link.
  - The new password must meet the defined security requirements.

## 3. **Task Breakdown**

For each user story, break it down into smaller, actionable tasks. Estimate the effort for each task (e.g., in hours or story points).

**Example (for Password Reset story):**

- **Task 1**: Design the database schema for password reset tokens (1 hour).
- **Task 2**: Create the API endpoint to request a password reset (2 hours).
- **Task 3**: Implement the logic to generate and store a secure reset token (2 hours).
- **Task 4**: Integrate with the email service to send the reset link (3 hours).
- **Task 5**: Create the API endpoint to reset the password (2 hours).
- **Task 6**: Implement the frontend form for resetting the password (4 hours).
- **Task 7**: Write unit and integration tests for the password reset flow (4 hours).

## 4. **Timeline and Milestones**

Based on the task breakdown, create a timeline for the project. Define key milestones to track progress.

- **Sprint 1**:
  - Implement user registration and login.
  - Set up the initial database schema.
- **Sprint 2**:
  - Implement password reset functionality.
  - Develop the user profile page.
- **Sprint 3**:
  - Implement the core product features.
  - Set up the CI/CD pipeline.

## 5. **Dependencies and Risks**

Identify any dependencies on other teams or services. What are the potential risks that could impact the project timeline?

- **Dependencies**:
  - Frontend team needs the API endpoints to be ready.
  - Marketing team needs the feature to be launched by a specific date.
- **Risks**:
  - Third-party API may have unexpected downtime.
  - The complexity of a feature may be underestimated.

Please provide your input for each section, and I will help you create a comprehensive development plan.
