# AI Garage Copilot Instructions

This file contains general coding practices, preferred technologies, and project requirements for rapid, production-grade solution development.

## Core Development Principles

**Security First**: All code must be developed with security as the primary consideration. Apply defense-in-depth principles and validate all inputs.

**Production Ready**: Code should be deployment-ready with proper error handling, logging, monitoring, and documentation.

**Customer Adaptable**: Solutions should be flexible and configurable to meet diverse customer requirements without major architectural changes.

**Documentation Driven**: All code must be thoroughly documented with clear explanations, examples, and architectural diagrams.

## Technology Stack Preferences

### Backend Development

- **Python**: FastAPI for APIs, Pydantic for data validation, SQLAlchemy for ORM
- **.NET**: ASP.NET Core for APIs, Entity Framework Core for ORM, Clean Architecture patterns
- **Databases**: PostgreSQL for relational data, Redis for caching
- **Authentication**: OAuth2/OpenID Connect, JWT tokens with proper validation

### Frontend Development

- **TypeScript**: Strict type checking enabled
- **React**: Functional components with hooks, proper state management
- **UI Libraries**: Tailwind CSS, shadcn/ui, or Material-UI
- **Testing**: Jest, React Testing Library, Playwright for E2E

### DevOps & Infrastructure

- **Containerization**: Docker with multi-stage builds, non-root users
- **Cloud Agnostic**: Support for AWS, Azure, GCP deployment patterns
- **CI/CD**: GitHub Actions with security scanning and automated testing
- **Monitoring**: Structured logging with correlation IDs, health checks

## Code Quality Standards

### General Guidelines

- Use meaningful names for variables, functions, and classes
- Keep functions small and focused (single responsibility)
- Write self-documenting code with clear intent
- Implement comprehensive error handling
- Include unit tests with >80% coverage

### Performance Requirements

- All APIs must respond within 200ms for 95% of requests
- Database queries must be optimized with proper indexing
- Implement caching strategies for frequently accessed data
- Use async/await patterns for I/O operations

### Security Requirements

- Input validation on all external data
- Parameterized queries to prevent SQL injection
- Proper authentication and authorization on all endpoints
- Sensitive data encryption at rest and in transit
- Regular dependency vulnerability scanning

## Documentation Requirements

### Code Documentation

- All public APIs must have comprehensive docstrings
- Include parameter types, return values, and exceptions
- Provide usage examples for complex functions
- Document business logic and architectural decisions

### API Documentation

- OpenAPI/Swagger specifications for all REST APIs
- Request/response examples with status codes
- Authentication requirements clearly documented
- Rate limiting and error handling documented

### Architecture Documentation

- System architecture diagrams using Mermaid or PlantUML
- Database schema documentation with relationships
- Deployment architecture and environment configurations
- Security architecture and data flow diagrams

## Testing Strategy

### Unit Testing

- Test all business logic with comprehensive coverage
- Use dependency injection for testable code
- Mock external dependencies and services
- Include edge cases and error scenarios

### Integration Testing

- Test API endpoints with realistic data
- Test database operations and transactions
- Test authentication and authorization flows
- Test external service integrations

### Security Testing

- Input validation testing with malicious payloads
- Authentication and authorization testing
- SQL injection and XSS prevention testing
- Dependency vulnerability scanning

## Deployment Patterns

### Containerization

- Multi-stage Docker builds for optimized images
- Non-root user execution for security
- Health check endpoints for container orchestration
- Environment-specific configuration management

### Cloud Deployment

- Infrastructure as Code (Terraform/ARM/CloudFormation)
- Auto-scaling and load balancing configuration
- Backup and disaster recovery procedures
- Monitoring and alerting setup

### CI/CD Pipeline

- Automated testing on all pull requests
- Security scanning in the build pipeline
- Automated deployment to staging environments
- Manual approval for production deployments

## Customer Adaptability

### Configuration Management

- Environment variables for all configurable settings
- Customer-specific configuration files
- Feature flags for optional functionality
- Database schema migration strategies

### Multi-tenancy Support

- Tenant isolation at the application and data level
- Configurable branding and theming
- Customer-specific business rules
- Scalable architecture for varying loads

### Integration Capabilities

- RESTful APIs with standard HTTP methods
- Webhook support for event notifications
- Standard authentication mechanisms
- Data export/import capabilities

## AI Development Guidelines

### Prompt Engineering

- Use clear, specific instructions in prompts
- Provide context and examples for complex tasks
- Iteratively refine prompts based on results
- Document successful prompt patterns

### Code Generation

- Review all AI-generated code for security vulnerabilities
- Ensure generated code follows project standards
- Test AI-generated code thoroughly
- Maintain human oversight for critical components

### Quality Assurance

- AI-generated code must pass all quality gates
- Security scanning required for all generated code
- Performance testing for AI-generated components
- Documentation required for AI-assisted development

---

These instructions apply to all code generation tasks and should be followed consistently across all projects and technologies.

---
## Referenced Instructions

### Python
- [Classes](./instructions/python/classes.instructions.md)
- [Configuration](./instructions/python/configuration.instructions.md)
- [Documentation](./instructions/python/documentation.instructions.md)
- [Error Handling](./instructions/python/error-handling.instructions.md)
- [Functions](./instructions/python/functions.instructions.md)
- [General](./instructions/python/general.instructions.md)
- [Imports](./instructions/python/imports.instructions.md)
- [Logging](./instructions/python/logging.instructions.md)
- [Performance](./instructions/python/performance.instructions.md)
- [Testing](./instructions/python/testing.instructions.md)
- [Typing](./instructions/python/typing.instructions.md)
