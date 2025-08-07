---
description: "Create a detailed development plan for a new feature or project."
mode: "ask"
---

# Development Plan Creation Prompt

This prompt will help you create a detailed development plan, breaking down a new feature or project into manageable tasks and timelines.

## 1. **Project Overview**

Please provide a brief overview of the project or feature for which you are creating a development plan.

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
