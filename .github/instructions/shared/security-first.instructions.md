---
applyTo: "**"
---

# Security-First Development Instructions

**Keywords**: #security #security-first #owasp #secure-coding #best-practices

---

## 🔐 Security Rule Directives

### Core Security Principles

```
@security Rule - Security by Design: Security considerations must be integrated from the initial design phase, not added as an afterthought.
```

```
@security Rule - Defense in Depth: Implement multiple layers of security controls rather than relying on a single security measure.
```

```
@security Rule - Principle of Least Privilege: Grant only the minimum permissions necessary for functionality.
```

```
@security Rule - Fail Securely: When security controls fail, the system should fail to a secure state.
```

### Input Validation and Sanitization

```
@security Rule - Validate All Input: Always validate and sanitize all input from external sources including user input, file uploads, API calls, and database queries.
```

```
@security Rule - Input Validation: Use allowlist validation (what is allowed) rather than blocklist (what is forbidden).
```

```
@security Rule - SQL Injection Prevention: Always use parameterized queries, prepared statements, or ORMs instead of string concatenation for database operations.
```

```
@security Rule - XSS Prevention: Encode all output and use Content Security Policy (CSP) headers to prevent cross-site scripting attacks.
```

### Authentication and Authorization

```
@security Rule - Strong Authentication: Implement multi-factor authentication and strong password policies.
```

```
@security Rule - Session Management: Use secure session management with proper timeout, regeneration, and invalidation.
```

```
@security Rule - Authorization Checks: Perform authorization checks on every request, not just authentication.
```

```
@security Rule - JWT Security: If using JWT tokens, use strong signing algorithms, validate all claims, and implement proper expiration.
```

### Data Protection

```
@security Rule - Encryption at Rest: Encrypt sensitive data when stored in databases, files, or other storage systems.
```

```
@security Rule - Encryption in Transit: Use TLS/HTTPS for all communications, especially when transmitting sensitive data.
```

```
@security Rule - Password Hashing: Use strong, salted hashing algorithms (bcrypt, scrypt, or Argon2) for password storage.
```

```
@security Rule - Sensitive Data Handling: Never log, cache, or store sensitive information (passwords, keys, tokens) in plain text.
```

### API Security

```
@security Rule - API Rate Limiting: Implement rate limiting to prevent abuse and denial-of-service attacks.
```

```
@security Rule - API Authentication: Secure all API endpoints with proper authentication mechanisms.
```

```
@security Rule - API Versioning: Maintain API versioning and deprecate insecure endpoints properly.
```

```
@security Rule - CORS Configuration: Configure CORS headers restrictively, only allowing necessary origins.
```

### Error Handling and Logging

```
@security Rule - Secure Error Messages: Never expose sensitive information, stack traces, or system details in error messages.
```

```
@security Rule - Security Logging: Log all security-relevant events (authentication attempts, authorization failures, input validation failures).
```

```
@security Rule - Log Protection: Protect log files from unauthorized access and tampering.
```

### Dependencies and Infrastructure

```
@security Rule - Dependency Security: Regularly update dependencies and scan for known vulnerabilities.
```

```
@security Rule - Environment Variables: Use environment variables or secure vaults for configuration secrets, never hardcode them.
```

```
@security Rule - Container Security: Follow container security best practices including non-root users and minimal base images.
```

```
@security Rule - Network Security: Implement proper network segmentation and firewall rules.
```

## 🛡️ OWASP Top 10 Mitigations

### A01 - Broken Access Control
- Implement proper authorization checks at the application level
- Use centralized access control mechanisms
- Validate permissions for every request

### A02 - Cryptographic Failures
- Use strong, up-to-date cryptographic algorithms
- Implement proper key management
- Never use deprecated or weak encryption methods

### A03 - Injection
- Use parameterized queries and prepared statements
- Validate and sanitize all inputs
- Use allowlist input validation

### A04 - Insecure Design
- Integrate security into the design phase
- Use threat modeling
- Implement security patterns and libraries

### A05 - Security Misconfiguration
- Secure default configurations
- Regular security updates
- Remove unnecessary features and services

### A06 - Vulnerable Components
- Maintain an inventory of components
- Regular vulnerability scanning
- Keep dependencies updated

### A07 - Authentication Failures
- Implement multi-factor authentication
- Strong password policies
- Secure session management

### A08 - Software Data Integrity Failures
- Use digital signatures for software updates
- Implement integrity checks
- Secure CI/CD pipelines

### A09 - Logging and Monitoring Failures
- Comprehensive security logging
- Real-time monitoring and alerting
- Incident response procedures

### A10 - Server-Side Request Forgery
- Validate and sanitize URLs
- Use allowlists for remote resources
- Network layer controls

## 🔍 Security Testing Requirements

- **Static Application Security Testing (SAST)**: Integrate automated code analysis
- **Dynamic Application Security Testing (DAST)**: Test running applications
- **Interactive Application Security Testing (IAST)**: Real-time security testing
- **Software Composition Analysis (SCA)**: Scan dependencies for vulnerabilities
- **Penetration Testing**: Regular security assessments by qualified professionals

## 📋 Security Checklist

### Pre-Development
- [ ] Threat modeling completed
- [ ] Security requirements defined
- [ ] Secure architecture design reviewed

### During Development
- [ ] Input validation implemented
- [ ] Authentication and authorization in place
- [ ] Sensitive data encrypted
- [ ] Security testing integrated

### Pre-Deployment
- [ ] Security configuration review
- [ ] Vulnerability scanning completed
- [ ] Penetration testing performed
- [ ] Security documentation updated

### Post-Deployment
- [ ] Security monitoring enabled
- [ ] Incident response plan in place
- [ ] Regular security updates scheduled
- [ ] Security training completed

---

**Note**: These security guidelines should be applied consistently across all technologies and platforms. Security is not optional—it's a fundamental requirement for all production systems.
