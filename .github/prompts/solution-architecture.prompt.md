---
description: "Design the solution architecture for a new feature or application."
mode: 'ask'
model: "Claude Sonnet 4"
---

# Solution Architecture Design Prompt

I'll help you design a robust, scalable solution architecture by asking targeted questions about your requirements and constraints.

## Architecture Design Process

When you share your solution requirements, I will:

1. **Ask clarifying questions** about functional and non-functional requirements
2. **Understand constraints** like scale, performance, security, and compliance needs
3. **Recommend technology stack** based on your team's skills and project needs
4. **Design system components** and their interactions
5. **Address scalability, security, and reliability** concerns
6. **Create architectural diagrams** and documentation

## Key Questions I'll Ask

### **Requirements & Constraints**
- What are the core functional requirements?
- What are your performance, scalability, and availability requirements?
- Are there any security, compliance, or regulatory requirements?
- What's your expected user load and data volume?

### **Technical Context**
- What's your team's technology expertise?
- Are there existing systems you need to integrate with?
- What's your preferred cloud provider or deployment model?
- What's your budget and timeline constraints?

### **System Characteristics**
- Will this be a monolith or microservices architecture?
- Do you need real-time features or is eventual consistency acceptable?
- What are your data consistency and backup requirements?
- How will you handle monitoring, logging, and observability?

## Let's Start

**Please describe your solution requirements, and I'll ask targeted questions to design the optimal architecture for your needs.**

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
