---
description: "Design the solution architecture for a new feature or application."
mode: "ask"
---

# Solution Architecture Design Prompt

This prompt will guide you through designing a robust and scalable solution architecture for your new feature or application.

## 1. **High-Level Overview**

Please provide a brief overview of the solution you are designing. What are the key goals and constraints?

## 2. **Component Breakdown**

Identify the main components of your architecture. For each component, describe its responsibilities and how it interacts with other components.

- **Example Components**:
  - **API Gateway**: Manages and routes incoming API requests.
  - **Authentication Service**: Handles user authentication and authorization.
  - **User Service**: Manages user data and profiles.
  - **Product Service**: Manages product information and inventory.
  - **Order Service**: Processes and manages customer orders.
  - **Database**: Stores application data (e.g., PostgreSQL, Redis).
  - **Message Queue**: Enables asynchronous communication between services.

## 3. **Technology Stack**

Specify the technology stack for each component.

- **Backend**: Python (FastAPI), .NET (ASP.NET Core)
- **Frontend**: TypeScript, React
- **Database**: PostgreSQL, Redis
- **Containerization**: Docker
- **Cloud Provider**: AWS, Azure, GCP

## 4. **Data Flow Diagram**

Describe the data flow between the components. How does data move through the system, from the user's initial request to the final response?

## 5. **Scalability and Performance**

How will the architecture scale to handle increasing load? What are the key performance considerations?

- **Strategies**:
  - Load balancing
  - Auto-scaling
  - Caching (e.g., Redis)
  - Database indexing and optimization

## 6. **Security and Compliance**

How will you ensure the security of the application and its data?

- **Measures**:
  - Authentication and authorization (OAuth2, JWT)
  - Input validation
  - Data encryption (at rest and in transit)
  - Compliance with relevant standards (e.g., GDPR, HIPAA)

## 7. **Deployment and CI/CD**

How will the application be deployed and managed?

- **Tools**:
  - Infrastructure as Code (Terraform, ARM)
  - CI/CD pipeline (GitHub Actions)
  - Monitoring and logging (Prometheus, Grafana, ELK stack)

Please provide your input for each section, and I will help you create a comprehensive solution architecture design.
