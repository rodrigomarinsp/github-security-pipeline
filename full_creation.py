import os
import matplotlib.pyplot as plt
import re
from IPython.display import Markdown, display
import requests
from datetime import datetime
import base64
import json

# Ensure output directory exists
output_dir = './output'
os.makedirs(output_dir, exist_ok=True)

# First, let's create the README.md file with enhanced formatting
readme_content = '''# 🛡️ GitHub Security Pipeline

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Maintained](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Security](https://img.shields.io/badge/Security-Enterprise-red.svg)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-Enabled-brightgreen.svg)

> **Enterprise-grade security scanning for GitHub repositories**

<p align="center">
  <img src="https://raw.githubusercontent.com/example/github-security-pipeline/main/docs/images/shield-lock.png" alt="GitHub Security Pipeline" width="180" height="180">
</p>

## 📋 Table of Contents

- [🚀 Quick Start](#-quick-start)
- [✨ Features](#-features)
- [📋 Requirements](#-requirements)
- [🔧 Installation Methods](#-installation-methods)
- [🏗️ Architecture](#-architecture)
- [⚙️ Configuration](#-configuration)
- [🚨 Security Checks](#-security-checks)
- [🔍 Troubleshooting](#-troubleshooting)
- [📝 Contributing](#-contributing)
- [🔄 Changelog](#-changelog)
- [📜 License](#-license)
- [🛟 Support](#-support)

## 🚀 Quick Start

This project provides a comprehensive security pipeline for GitHub repositories that automatically scans for secrets, vulnerabilities, and security issues.

### Single Repository Deployment

```bash
# Clone the repository
git clone https://github.com/yourusername/github-security-pipeline.git
cd github-security-pipeline

# Run the single repository setup
./setup-repository.sh
```

### Organization-Wide Deployment

```bash
# Clone the repository
git clone https://github.com/yourusername/github-security-pipeline.git
cd github-security-pipeline

# Run the organization setup
./setup-organization.sh --org yourgithuborganization
```

### Enterprise Deployment via Terraform

```bash
# Clone the repository
git clone https://github.com/yourusername/github-security-pipeline.git
cd github-security-pipeline/terraform

# Initialize Terraform
terraform init

# Apply the configuration
terraform apply -var="github_token=your_token" -var="organization=your_organization"
```

## ✨ Features

- 🔐 **Comprehensive Security Scanning**
  - Secrets detection (API keys, tokens, passwords)
  - Dependency vulnerability scanning
  - Infrastructure-as-Code security validation
  - Code quality analysis

- 🚫 **Pre-Push Protection**
  - Block commits with secrets
  - Prevent vulnerable dependency introduction
  - Flag insecure code patterns

- 🌐 **Multi-Environment Support**
  - GitHub.com repositories
  - GitHub Enterprise Server
  - GitHub Enterprise Cloud
  - Private GitHub instances

- 🧰 **Enterprise Integration**
  - SIEM integration (Splunk, ELK, etc.)
  - Issue tracker integration (JIRA, ServiceNow)
  - Slack/Teams notifications
  - Email alerts

- 📊 **Compliance Reporting**
  - GDPR compliance checks
  - HIPAA validation
  - SOC2 controls
  - PCI-DSS requirements

## 📋 Requirements

| Component | Minimum | Recommended |
|-----------|---------|------------|
| GitHub | Free Plan | Team/Enterprise |
| GitHub Actions | Free Tier | Business Tier |
| Python | 3.8+ | 3.9+ |
| Git | 2.22+ | 2.30+ |
| GitHub CLI | 2.0+ | 2.15+ |
| Permissions | Repository Admin | Organization Admin |

### Operating System Compatibility

| OS | Version | Support Level |
|----|---------|--------------|
| Ubuntu | 20.04+ | Full Support |
| macOS | 10.15+ | Full Support |
| Windows | 10/11 | Full Support |
| Alpine | 3.14+ | Basic Support |
| CentOS | 8+ | Basic Support |

## 🔧 Installation Methods

### 1. Individual Repository Installation

For single repository protection, our setup script automatically:
- Creates necessary GitHub Actions workflows
- Sets up branch protection rules
- Configures security scanning tools
- Validates the installation

### 2. Organization-Wide Installation

Our organization setup:
- Creates an organization-level `.github` repository
- Sets up workflow templates for all repositories
- Configures organization security settings
- Applies security policies organization-wide
- Sets up automated issue creation for vulnerabilities

### 3. Enterprise Deployment

For enterprise-grade installations:
- Terraform modules for automated deployment
- Integration with enterprise SSO
- Custom security policy enforcement
- Compliance monitoring and reporting
- Audit trail and governance controls

## 🏗️ Architecture

```
                   +---------------------+
                   |                     |
                   |  GitHub Repository  |
                   |                     |
                   +----------+----------+
                              |
                              v
+-------------+   +-----------------------+   +---------------+
|             |   |                       |   |               |
| Pre-Commit  +-->+  GitHub Actions Flow  +-->+ Notifications |
|   Hooks     |   |                       |   |               |
|             |   +-----------+-----------+   +---------------+
+-------------+               |
                              |
              +---------------v---------------+
              |                               |
              |         Security Scans        |
              |                               |
              +-------------------------------+
              |                               |
              | +---------------------------+ |
              | |       Secret Scanning     | |
              | +---------------------------+ |
              |                               |
              | +---------------------------+ |
              | |  Dependency Vulnerability | |
              | +---------------------------+ |
              |                               |
              | +---------------------------+ |
              | |   Static Code Analysis    | |
              | +---------------------------+ |
              |                               |
              | +---------------------------+ |
              | |     Compliance Checks     | |
              | +---------------------------+ |
              |                               |
              +---------------+---------------+
                              |
              +---------------v---------------+
              |                               |
              |       Security Reports        |
              |                               |
              +-------------------------------+
```

## ⚙️ Configuration

### Base Configuration (security-config.yml)

```yaml
# Security Pipeline Configuration
version: 1.0.0
settings:
  notification:
    slack: true
    email: true
    teams: false
  scanning:
    secrets: true
    dependencies: true
    static_analysis: true
    compliance: true
  reporting:
    issue_creation: true
    pull_request_comments: true
    dashboard: true
```

### Secret Scanning Configuration

```yaml
# .gitleaks.yml
rules:
  - id: aws-access-key
    severity: CRITICAL
    regex: 'AKIA[0-9A-Z]{16}'
    tags:
      - aws
      - credentials
  - id: github-pat
    severity: CRITICAL
    regex: 'ghp_[0-9a-zA-Z]{36}'
    tags:
      - github
      - credentials
```

### Dependency Scanning Configuration

```yaml
# dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
    allow:
      - dependency-type: "all"
    open-pull-requests-limit: 10
```

## 🚨 Security Checks

The pipeline performs the following security checks:

1. **Secret Detection**
   - API keys and tokens
   - SSH private keys
   - Database connection strings
   - Authentication credentials
   - Encryption keys

2. **Dependency Security**
   - Vulnerable package detection
   - Outdated dependency alerts
   - License compliance
   - Supply chain attacks

3. **Code Security**
   - Injection vulnerabilities
   - Authentication weaknesses
   - Session management flaws
   - Access control issues
   - Cryptographic failures

4. **IaC Security**
   - Terraform security risks
   - Docker configuration issues
   - Kubernetes misconfigurations
   - Cloud resource exposures

## 🔍 Troubleshooting

### Common Issues

#### GitHub Actions Workflow Not Running

**Problem:** Workflows aren't being triggered on push/PR events.
**Solution:** Verify:
1. Workflow files are in `.github/workflows/`
2. Branch protection settings allow actions
3. Repository actions are enabled in Settings > Actions

#### False Positives in Secret Detection

**Problem:** Legitimate patterns being flagged as secrets
**Solution:** 
1. Add specific patterns to `.gitleaks.toml` allowlist
2. Use [no-secret] marker in comments for approved test keys
3. Configure custom regex patterns in the secret scanning config

#### Performance Issues

**Problem:** Security scans taking too long
**Solution:**
1. Use matrix builds for parallel scanning
2. Implement path filtering to scan only relevant files
3. Adjust scan depth settings in configuration
4. Enable incremental scanning where possible

## 📝 Contributing

We welcome contributions from the community! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for details on:

- Code of conduct
- Contribution process
- Development setup
- Pull request guidelines
- Coding standards
- Testing requirements

## 🔄 Changelog

See [CHANGELOG.md](CHANGELOG.md) for the release history and details of changes in each version.

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🛟 Support

For support, please:

1. Check the [documentation](docs/)
2. Review [troubleshooting](#-troubleshooting) section
3. Open an [issue](https://github.com/yourusername/github-security-pipeline/issues)
4. Join our [community Slack](https://slack.example.com/github-security-pipeline)

For enterprise support, contact: security-pipeline-support@example.com
'''

# Write README.md to the output directory
with open(os.path.join(output_dir, 'README.md'), 'w') as f:
    f.write(readme_content)
    
# Create the CONTRIBUTING.md file
contributing_content = '''# 📝 Contributing to GitHub Security Pipeline

## Author: Security Pipeline Team

## E-Mail: security-pipeline-maintainers@example.com

## GitHub: github.com/github-security-pipeline

## Website: https://security-pipeline.example.com

Thank you for your interest in contributing to the GitHub Security Pipeline! This document provides guidelines and best practices for contributing to the project.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Improving Documentation](#improving-documentation)
  - [Contributing Code](#contributing-code)
- [Development Environment](#development-environment)
  - [Prerequisites](#prerequisites)
  - [Setup Steps](#setup-steps)
  - [Development Tools](#development-tools)
- [Pull Request Process](#pull-request-process)
  - [Submission Guidelines](#submission-guidelines)
  - [Code Review Process](#code-review-process)
  - [Merge Requirements](#merge-requirements)
- [Coding Standards](#coding-standards)
  - [Style Guides](#style-guides)
  - [Documentation Standards](#documentation-standards)
  - [Testing Requirements](#testing-requirements)
- [Security Considerations](#security-considerations)
- [Additional Resources](#additional-resources)

## Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md) that all participants are expected to follow. By participating, you are expected to uphold this code. Please report unacceptable behavior to security-pipeline-maintainers@example.com.

## How Can I Contribute?

### Reporting Bugs

We use GitHub issues to track bugs. Before creating a bug report:

1. **Check the issue tracker** to see if the bug has already been reported
2. **Use the provided bug report template** when creating a new issue
3. **Provide detailed information** including:
   - Clear, descriptive title
   - Exact steps to reproduce the issue
   - Expected vs. actual behavior
   - Screenshots or logs (redacted of sensitive information)
   - Environment details (OS, GitHub version, etc.)
   - Potential workarounds if known

### Suggesting Features

Feature suggestions are tracked as GitHub issues:

1. **Check existing issues** to avoid duplicates
2. **Use the feature request template** for new suggestions
3. **Be specific about the problem** the feature would solve
4. **Provide mockups or examples** if applicable
5. **Consider scope and compatibility** with the project's goals

### Improving Documentation

Documentation improvements are vital to the project:

1. **Identify gaps or unclear sections** in existing documentation
2. **Follow documentation standards** outlined below
3. **Submit documentation-only PRs** separate from code changes
4. **Include examples and context** for better understanding
5. **Consider multiple audience levels** (beginner, intermediate, advanced)

### Contributing Code

Code contributions are welcome through pull requests:

1. **Start with small contributions** to become familiar with the project
2. **Discuss major changes** in an issue before implementing
3. **Follow the [pull request process](#pull-request-process)**
4. **Adhere to [coding standards](#coding-standards)**
5. **Include tests** for new functionality
6. **Update documentation** to reflect changes

## Development Environment

### Prerequisites

To contribute to this project, you'll need:

- **Git** (2.22.0 or higher)
- **GitHub CLI** (2.0.0 or higher)
- **Python** (3.8 or higher)
- **Docker** (20.10.0 or higher, optional for container testing)
- **Node.js** (14.0.0 or higher, for web components)
- **GitHub account** with two-factor authentication enabled

### Setup Steps

1. **Fork the repository** on GitHub
2. **Clone your fork**:
   ```bash
   git clone https://github.com/YOUR-USERNAME/github-security-pipeline.git
   cd github-security-pipeline
   ```
3. **Set up the upstream remote**:
   ```bash
   git remote add upstream https://github.com/original-org/github-security-pipeline.git
   ```
4. **Install dependencies**:
   ```bash
   python -m pip install -r requirements.txt
   python -m pip install -r requirements-dev.txt
   ```
5. **Set up pre-commit hooks**:
   ```bash
   pre-commit install
   ```

### Development Tools

We recommend the following tools for development:

- **IDE**: Visual Studio Code with Python, YAML, and GitHub Actions extensions
- **Linting**: flake8, pylint, eslint
- **Formatting**: black, prettier
- **Testing**: pytest, github-actions-runner
- **Documentation**: mkdocs, sphinx

## Pull Request Process

### Submission Guidelines

1. **Create a feature branch** from the main branch
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. **Make your changes** following the coding standards
3. **Commit with clear messages** following conventional commits:
   ```
   type(scope): brief description
   
   Longer description explaining the change and its motivation.
   
   Fixes #123
   ```
4. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Submit a pull request** against the main branch

### Code Review Process

1. **Maintainers will review** your pull request
2. **Address review comments** promptly
3. **CI checks must pass** before merging
4. **Update the PR** with requested changes if needed
5. **Squash commits** if requested before merging

### Merge Requirements

- **Approval from at least 2 maintainers**
- **All CI checks passing**
- **Documentation updated**
- **Tests passing**
- **Code meets quality standards**
- **Conflicts resolved**

## Coding Standards

### Style Guides

- **Python Code**: Follow [PEP 8](https://pep8.org/) with a line length of 88 characters
- **Shell Scripts**: Follow [Google's Shell Style Guide](https://google.github.io/styleguide/shellguide.html)
- **YAML**: Use 2-space indentation and follow [YAML Spec 1.2](https://yaml.org/spec/1.2/spec.html)
- **Markdown**: Follow [CommonMark](https://commonmark.org/) specification
- **JavaScript**: Follow [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript)

### Documentation Standards

- **Use clear, concise language**
- **Include examples** for complex features
- **Document function parameters and return values**
- **Add docstrings** to all functions and classes
- **Use type hints** in Python code
- **Keep documentation up-to-date** with code changes
- **Create diagrams** for complex workflows

### Testing Requirements

- **Write unit tests** for all new functionality
- **Maintain minimum 80% code coverage**
- **Include integration tests** for workflow changes
- **Test edge cases** and error conditions
- **Mock external dependencies** in tests
- **Use parameterized tests** where appropriate
- **Verify performance impact** for significant changes

## Security Considerations

When contributing to this security-focused project, please:

- **Never commit secrets** or credentials, even in tests
- **Use strong typing** and input validation
- **Follow the principle of least privilege**
- **Consider security implications** of every change
- **Report security vulnerabilities** via our [security policy](SECURITY.md)
- **Use approved encryption methods** for sensitive data
- **Review dependencies** for security issues before adding

## Additional Resources

- [Project Documentation](https://github-security-pipeline.example.com/docs)
- [Development Roadmap](https://github.com/yourusername/github-security-pipeline/wiki/Roadmap)
- [Security Best Practices](https://github-security-pipeline.example.com/security-guide)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [GitHub Security Features](https://docs.github.com/en/code-security)
'''

# Write CONTRIBUTING.md to the output directory
with open(os.path.join(output_dir, 'CONTRIBUTING.md'), 'w') as f:
    f.write(contributing_content)
    
# Create the CHANGELOG.md file
changelog_content = '''# 📝 Changelog

## Author: Security Pipeline Team

## E-Mail: security-pipeline-maintainers@example.com

## GitHub: github.com/github-security-pipeline

## Website: https://security-pipeline.example.com

All notable changes to the GitHub Security Pipeline project are documented in this file.

This project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html), and the format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- New secret detection patterns for cloud provider credentials
- Enhanced documentation for enterprise deployments
- Support for GitLab integration (experimental)

### Changed
- Improved performance of dependency scanning workflows
- Updated code scanning rules for Python 3.11 compatibility

## [1.0.0] - 2023-06-15

### Added
- Initial release of GitHub Security Pipeline
- Comprehensive security scanning system
  - Secret detection via Gitleaks integration
  - Dependency vulnerability scanning with Dependabot
  - Code quality analysis with CodeQL
  - Infrastructure-as-Code scanning
- Organization-wide deployment capabilities
- Multiple installation methods:
  - Single repository setup
  - Organization-wide setup
  - Enterprise deployment via Terraform
- Extensive documentation and examples
- Pre-commit hooks for local security scanning
- CI/CD integration examples
- Security policy enforcement mechanisms
- Notification systems for various platforms:
  - Slack integration
  - Microsoft Teams integration
  - Email notifications
  - Issue creation

### Security
- Implemented secure secret handling in workflows
- Added sandboxed execution environment for scans
- Encrypted storage for temporary scan artifacts

## [0.9.0] - 2023-05-20

### Added
- Beta release for early adopters
- Core security scanning functionality
- Basic GitHub Actions workflows
- Initial documentation

### Changed
- Refactored workflow structure for better performance
- Enhanced secret detection patterns

### Fixed
- Resolved issues with macOS compatibility
- Fixed Windows path handling in scripts

## [0.8.0] - 2023-04-10

### Added
- Alpha release for internal testing
- Proof-of-concept security scanning workflows
- Basic documentation structure

## Migration Guides

### Migrating from 0.x to 1.0.0

1. **Update Configuration Files**:
   The configuration format has changed in 1.0.0. Use the migration script to update your configuration files:
   ```bash
   ./scripts/migrate_config.sh
   ```

2. **Workflow Updates**:
   Replace your existing workflow files with the new versions:
   ```bash
   cp -r .github/workflows-templates/* .github/workflows/
   ```

3. **New Environment Variables**:
   The following environment variables are now required:
   - `SECURITY_SCAN_LEVEL`: Set to "basic", "standard", or "thorough"
   - `NOTIFICATION_CHANNEL`: Configure notification preferences

4. **Breaking Changes**:
   - The `scan.sh` script has been renamed to `security-scan.sh`
   - Custom rules must now be placed in the `.github/security-rules/` directory
   - Minimum GitHub Actions runner version is now 2.285.0

### Security Update Notes

#### Critical Security Updates in 1.0.0:
- Fixed potential path traversal vulnerability in script execution
- Updated dependencies to patch CVE-2023-28732
- Enhanced permissions model for GitHub Actions

## Compatibility Matrix

| Version | Minimum GitHub Actions | Python Support | GitHub Enterprise | Breaking Changes |
|---------|------------------------|----------------|------------------|-----------------|
| 1.0.0   | 2.285.0+              | 3.8, 3.9, 3.10, 3.11 | 3.4+           | Yes (see migration) |
| 0.9.0   | 2.277.0+              | 3.8, 3.9, 3.10 | 3.2+           | No              |
| 0.8.0   | 2.270.0+              | 3.8, 3.9       | 3.0+           | Initial version |
'''

# Write CHANGELOG.md to the output directory
with open(os.path.join(output_dir, 'CHANGELOG.md'), 'w') as f:
    f.write(changelog_content)
    
    
# Create the requirements.txt file with categorized dependencies
requirements_content = '''# GitHub Security Pipeline - Python Dependencies
# Author: Security Pipeline Team
# E-Mail: security-pipeline-maintainers@example.com
# GitHub: github.com/github-security-pipeline
# Website: https://security-pipeline.example.com

#######################################################
# Core Dependencies - Required for basic functionality #
#######################################################

# YAML parsing for configuration files
pyyaml>=6.0,<7.0            # For parsing configuration files securely

# HTTP client for API interactions
requests>=2.28.0,<3.0.0     # For GitHub API interactions, maintained and secure

# Command-line interface tools
click>=8.1.3,<9.0.0         # For building command-line interfaces
colorama>=0.4.6,<1.0.0      # For colorized terminal output
rich>=12.5.1,<13.0.0        # For rich terminal formatting and output

# Security tools
cryptography>=39.0.0,<40.0.0  # For handling encryption operations securely
gitpython>=3.1.30,<4.0.0      # For Git repository operations

# Progress indicators
tqdm>=4.64.1,<5.0.0         # For progress bars in long-running operations

#################################################
# Security Scanning - For vulnerability scanning #
#################################################

# Secret scanning
detect-secrets>=1.4.0,<2.0.0  # LinkedIn's tool for detecting secrets in code
gitleaks-client>=1.0.0        # Client for Gitleaks secret scanning

# Dependency scanning
safety>=2.3.5,<3.0.0          # For Python dependency vulnerability scanning
bandit>=1.7.4,<2.0.0          # For Python static code security analysis

# Code quality
pylint>=2.15.10,<3.0.0        # Python code linting
flake8>=6.0.0,<7.0.0          # Style enforcement

###########################################################
# Integrations - Optional depending on your configuration #
###########################################################

# GitHub integration
PyGithub>=1.58.0,<2.0.0       # For GitHub API interaction
# Comment the following line if not using GitHub Enterprise:
# github-enterprise>=1.7.0,<2.0.0

# Cloud provider integrations - Uncomment as needed
# boto3>=1.26.0,<2.0.0          # For AWS integration
# google-cloud-storage>=2.7.0   # For Google Cloud integration
# azure-storage-blob>=12.14.0   # For Azure integration

# CI/CD integrations - Uncomment as needed
# jenkins-api-client>=1.0.0     # For Jenkins integration
# circle-client>=0.2.0          # For CircleCI integration

# Notification integrations - Uncomment as needed
slack-sdk>=3.19.0,<4.0.0       # For Slack notifications
# ms-teams-webhook>=1.0.5       # For Microsoft Teams notifications

#####################################################
# Development Dependencies - For contributors only #
#####################################################

# Testing tools - Install with pip install -r requirements-dev.txt
# pytest>=7.2.0,<8.0.0          # For unit testing
# pytest-cov>=4.0.0,<5.0.0      # For test coverage reporting
# pytest-mock>=3.10.0,<4.0.0    # For mocking in tests

# Development tools
# pre-commit>=3.0.0,<4.0.0      # For pre-commit hooks
# black>=23.1.0,<24.0.0         # For code formatting
# mypy>=1.0.0,<2.0.0            # For static type checking
'''

# Write requirements.txt to the output directory
with open(os.path.join(output_dir, 'requirements.txt'), 'w') as f:
    f.write(requirements_content)
    
    
# Create the SECURITY.md file
security_content = '''# 🔐 Security Policy

## Author: Security Pipeline Team

## E-Mail: security-pipeline-maintainers@example.com

## GitHub: github.com/github-security-pipeline

## Reporting a Vulnerability

The GitHub Security Pipeline team takes all security vulnerabilities seriously. We appreciate your efforts to disclose your findings responsibly and will make every effort to acknowledge your contributions.

### How to Report a Security Issue

**DO NOT** file a public GitHub issue about security vulnerabilities. 

Please report security vulnerabilities by emailing our security team at:

**security-pipeline-security@example.com**

Please include the following information in your report:

1. Description of the vulnerability
2. Steps to reproduce the issue
3. Potential impact of the vulnerability
4. Suggested mitigation or remediation if available
5. Your name and contact information (for attribution, if desired)

### What to Expect

After receiving your report, our security team will:

1. **Acknowledge** receipt of your vulnerability report within 24 hours
2. **Assess** the impact and severity of the reported issue
3. **Investigate** and work on a fix
4. **Release** an update that addresses the vulnerability
5. **Disclose** the vulnerability after it has been fixed

### Disclosure Policy

- Security vulnerabilities will be addressed with the highest priority
- We aim to release fixes for critical security issues within 7 days
- We will credit security researchers who report valid vulnerabilities if they wish
- Public disclosure will be coordinated with the reporter

## Supported Versions

| Version | Supported          | End of Support |
| ------- | ------------------ | -------------- |
| 1.0.x   | :white_check_mark: | Current        |
| 0.9.x   | :white_check_mark: | 2024-05-20     |
| 0.8.x   | :x:                | 2023-06-15     |
| < 0.8.0 | :x:                | End of life    |

## Security Updates

Security updates are published through:

1. GitHub Security Advisories
2. Release notes in our [CHANGELOG.md](CHANGELOG.md)
3. Security announcements on our [official website](https://security-pipeline.example.com/security)

## Best Practices

We recommend the following security best practices when using GitHub Security Pipeline:

### Authentication Security

- Use fine-grained personal access tokens with minimum required permissions
- Rotate tokens regularly
- Store tokens securely using GitHub Secrets or a secure vault
- Enable 2FA for all GitHub accounts

### Configuration Security

- Review automatically generated security rules before committing
- Store sensitive configuration separately from code
- Use environment variables for runtime configuration
- Validate configuration file permissions

### Integration Security

- Review external services connected to your repositories
- Audit GitHub Apps and OAuth permissions regularly
- Limit webhook endpoints to trusted services
- Verify webhook signatures

## Security Features

The GitHub Security Pipeline includes several security features:

1. **Secret Detection**: Prevents accidental exposure of tokens, passwords, and keys
2. **Dependency Scanning**: Identifies vulnerabilities in dependencies
3. **Code Quality Analysis**: Detects security anti-patterns
4. **Configuration Validation**: Ensures secure configurations
5. **Pull Request Analysis**: Reviews changes for security issues

## Acknowledgments

We would like to thank the following security researchers for their valuable contributions to the security of this project:

- Alex Security ([@alexsec](https://github.com/alexsec)) - Responsible disclosure of token handling vulnerability
- Secure Coder ([@securecoder](https://github.com/securecoder)) - Improvements to secret scanning patterns
- Pentest Pro ([@pentestpro](https://github.com/pentestpro)) - Identifying a permission escalation risk

## Security Development Lifecycle

This project follows a security development lifecycle that includes:

1. Security requirements and threat modeling
2. Security design reviews
3. Static and dynamic code analysis
4. Third-party dependency reviews
5. Penetration testing
6. Security response planning
'''

# Write SECURITY.md to the output directory
with open(os.path.join(output_dir, 'SECURITY.md'), 'w') as f:
    f.write(security_content)
    

# Create the CODE_OF_CONDUCT.md file
code_of_conduct_content = '''# 📜 Code of Conduct

## Author: Security Pipeline Team

## E-Mail: security-pipeline-maintainers@example.com

## GitHub: github.com/github-security-pipeline

# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
conduct@security-pipeline.example.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.
'''

# Write CODE_OF_CONDUCT.md to the output directory
with open(os.path.join(output_dir, 'CODE_OF_CONDUCT.md'), 'w') as f:
    f.write(code_of_conduct_content)
    
    
# Create the SUPPORT.md file
support_content = '''# 🛟 Support

## Author: Security Pipeline Team

## E-Mail: security-pipeline-maintainers@example.com

## GitHub: github.com/github-security-pipeline

## Website: https://security-pipeline.example.com

This document provides information on getting support for the GitHub Security Pipeline.

## 📋 Table of Contents

- [Getting Help](#getting-help)
- [Documentation](#documentation)
- [Troubleshooting](#troubleshooting)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Community Support](#community-support)
- [Enterprise Support](#enterprise-support)
- [Training & Resources](#training--resources)
- [Feedback & Feature Requests](#feedback--feature-requests)

## Getting Help

There are several ways to get help with the GitHub Security Pipeline:

1. **Documentation**: Comprehensive guidance available in our [docs/](docs/) directory
2. **GitHub Issues**: Search existing issues or create new ones for confirmed bugs
3. **Discussion Forum**: Join conversations in our [GitHub Discussions](https://github.com/yourusername/github-security-pipeline/discussions)
4. **Community Slack**: Join our [community Slack](https://security-pipeline-community.slack.com)
5. **Stack Overflow**: Ask questions with the tag `github-security-pipeline`

## Documentation

Our documentation is structured to help users at different experience levels:

- **[Quick Start Guide](docs/quickstart.md)**: Get up and running quickly
- **[User Guide](docs/user-guide.md)**: Comprehensive usage documentation
- **[Administrator Guide](docs/admin-guide.md)**: Setup and management for administrators
- **[API Reference](docs/api-reference.md)**: Integration and automation details
- **[Examples](docs/examples)**: Real-world examples and templates

## Troubleshooting

For common problems and solutions, please refer to our [Troubleshooting Guide](docs/troubleshooting.md).

### Common Issues

1. **Configuration Problems**
   - Check your configuration file syntax
   - Verify permissions on configuration files
   - Ensure all required fields are present

2. **Workflow Failures**
   - Review workflow logs for specific error messages
   - Check GitHub Actions permissions
   - Verify GitHub token scopes

3. **False Positives**
   - Adjust detection rules in your configuration
   - Add specific patterns to allowlists
   - Use comment markers for approved exceptions

## Frequently Asked Questions

### General Questions

**Q: Is this tool compatible with private GitHub repositories?**  
A: Yes, the GitHub Security Pipeline works with all repository types: public, private, and internal.

**Q: Do I need GitHub Enterprise to use all features?**  
A: No, most features work with any GitHub plan. Some organization-wide features are enhanced with GitHub Enterprise.

**Q: How does the pipeline handle false positives?**  
A: We provide configurable allowlists and pattern adjustments to minimize false positives.

### Technical Questions

**Q: Can I customize the security scanning rules?**  
A: Yes, you can add custom rules in the `.github/security-rules/` directory.

**Q: Does this work with monorepos?**  
A: Yes, with path filtering and specialized configuration for monorepo structures.

**Q: How do I handle legitimate test credentials?**  
A: Use [no-secret] comment markers or add specific patterns to your allowlist.

## Community Support

Our community provides support through various channels:

- **GitHub Discussions**: Primary channel for questions and community help
- **Community Calls**: Monthly virtual meetups (announced in our Slack)
- **Knowledge Base**: Community-maintained answers at [docs.security-pipeline.example.com/kb](https://docs.security-pipeline.example.com/kb)
- **Local Meetups**: Check our [community calendar](https://security-pipeline.example.com/community) for events

## Enterprise Support

For organizations requiring dedicated support, we offer:

### Standard Support

- Email support with 48-hour response time
- Access to knowledge base and documentation
- Community forum priority
- Contact: support@security-pipeline.example.com

### Premium Support

- 24/7 email support with 4-hour response for critical issues
- Dedicated support engineer
- Monthly check-in calls
- Implementation consulting
- Custom rules and integration development
- Contact: premium-support@security-pipeline.example.com

## Training & Resources

Improve your skills with these resources:

- **[Official Documentation](https://security-pipeline.example.com/docs)**
- **[Video Tutorials](https://security-pipeline.example.com/videos)**
- **[Webinars](https://security-pipeline.example.com/webinars)** (past recordings available)
- **[Security Blog](https://security-pipeline.example.com/blog)**
- **[GitHub Security Best Practices](https://security-pipeline.example.com/best-practices)**

## Feedback & Feature Requests

We welcome your feedback to improve the project:

- **Feature Requests**: Submit via [GitHub Issues](https://github.com/yourusername/github-security-pipeline/issues/new?template=feature_request.md)
- **Enhancements**: Discuss ideas in our [GitHub Discussions](https://github.com/yourusername/github-security-pipeline/discussions/categories/ideas)
- **Surveys**: Participate in quarterly user surveys (announced in Slack)
- **Direct Feedback**: Send to feedback@security-pipeline.example.com
'''

# Write SUPPORT.md to the output directory
with open(os.path.join(output_dir, 'SUPPORT.md'), 'w') as f:
    f.write(support_content)
    
    
# Create GitHub issue templates directory structure
issue_template_dir = os.path.join(output_dir, '.github', 'ISSUE_TEMPLATE')
os.makedirs(issue_template_dir, exist_ok=True)

# Create bug report issue template
bug_report_template = '''---
name: 🐛 Bug report
about: Create a report to help us improve
title: '[BUG] '
labels: bug, needs-triage
assignees: ''

---

## 🐛 Bug Report

### Prerequisites
- [ ] I have checked the documentation and found no answer
- [ ] I have checked that this issue has not already been reported
- [ ] I have verified the bug exists in the latest version

### Environment
- **GitHub Security Pipeline Version**: <!-- e.g. 1.0.0 -->
- **Operating System**: <!-- e.g. Ubuntu 22.04, Windows 11, macOS 12.4 -->
- **GitHub Version**: <!-- e.g. GitHub Enterprise Cloud, GitHub.com -->
- **Python Version**: <!-- e.g. Python 3.9.10 -->
- **Git Version**: <!-- e.g. Git 2.36.1 -->

### Current Behavior
<!-- A clear and concise description of what the bug is. -->

### Expected Behavior
<!-- A clear and concise description of what you expected to happen. -->

### Steps to Reproduce
1. <!-- First Step -->
2. <!-- Second Step -->
3. <!-- and so on... -->

### Reproduction repository
<!-- If possible, please provide a link to a GitHub repository that can reproduce this issue -->

### Logs/Screenshots
<!-- If applicable, add logs and/or screenshots to help explain your problem. -->
```
// Paste logs here, if applicable
```

### Possible Solution
<!-- If you have suggestions on a fix for the bug, please describe it here. -->

### Additional Context
<!-- Add any other context about the problem here. -->
'''

# Write the bug report template
with open(os.path.join(issue_template_dir, 'bug_report.md'), 'w') as f:
    f.write(bug_report_template)

# Create feature request issue template
feature_request_template = '''---
name: 💡 Feature request
about: Suggest an idea for this project
title: '[FEATURE] '
labels: enhancement, needs-triage
assignees: ''

---

## 💡 Feature Request

### Is your feature request related to a problem? Please describe.
<!-- A clear and concise description of what the problem is. Ex. I'm always frustrated when [...] -->

### Describe the solution you'd like
<!-- A clear and concise description of what you want to happen. -->

### Describe alternatives you've considered
<!-- A clear and concise description of any alternative solutions or features you've considered. -->

### User Impact
<!-- Who would use this feature and how would it benefit them in their workflow? -->

### Proposed Implementation
<!-- If you have ideas about how this might be implemented, please share them here. -->

### Additional Context
<!-- Add any other context, screenshots, or mock-ups about the feature request here. -->
'''

# Write the feature request template
with open(os.path.join(issue_template_dir, 'feature_request.md'), 'w') as f:
    f.write(feature_request_template)

# Create security vulnerability issue template
security_vulnerability_template = '''---
name: 🔒 Security Vulnerability
about: Report a security vulnerability (PLEASE DO NOT DISCLOSE SENSITIVE DETAILS HERE)
title: "[SECURITY] "
labels: security, confidential
assignees: security-team

---

## 🚨 SECURITY ISSUE - HANDLE WITH CARE

### ⚠️ IMPORTANT - DO NOT DISCLOSE VULNERABILITY DETAILS IN THIS ISSUE ⚠️

**Please DO NOT disclose specific details about the vulnerability in this GitHub issue.**

Instead, please send details privately to:
**security-pipeline-security@example.com**

In your email, please include:

1. Description of the type of vulnerability (without specific exploit details)
2. Affected versions/components
3. Your contact information for follow-up

### For tracking purposes only, please provide:

**General type of issue**: <!-- e.g., Cross-Site Scripting, Authentication Bypass, etc. -->

**Affected component**: <!-- e.g., Web UI, API, CLI tool, GitHub Actions workflow -->

**Severity estimate**: <!-- High/Medium/Low based on your assessment -->

---

Thank you for responsibly reporting security issues.
We will respond to your email within 24 hours.

Please note: Public disclosure of security vulnerabilities without coordination puts all users at risk. We kindly request that you follow responsible disclosure practices.
'''

# Write the security vulnerability template
with open(os.path.join(issue_template_dir, 'security_vulnerability.md'), 'w') as f:
    f.write(security_vulnerability_template)

# Create documentation issue template
documentation_template = '''---
name: 📚 Documentation Issue
about: Report issues with the documentation or suggest improvements
title: '[DOCS] '
labels: documentation
assignees: ''

---

## 📚 Documentation Issue

### Current Documentation
<!-- Link to the documentation page or section that has issues -->

### Issue Type
- [ ] Missing information
- [ ] Incorrect information
- [ ] Unclear explanation
- [ ] Outdated content
- [ ] Formatting/structure issue
- [ ] Other

### Description
<!-- A clear and concise description of the issue with the documentation -->

### Suggested Improvement
<!-- How would you like to see the documentation improved? -->

### Additional Context
<!-- Add any other context about the documentation issue here -->

### Are you willing to help with this improvement?
<!-- Let us know if you'd like to contribute a fix for this docs issue -->
'''

# Write the documentation template
with open(os.path.join(issue_template_dir, 'documentation.md'), 'w') as f:
    f.write(documentation_template)

# Create config.yml for issue templates
config_yml = '''blank_issues_enabled: false
contact_links:
  - name: GitHub Security Pipeline Community Support
    url: https://github.com/yourusername/github-security-pipeline/discussions
    about: Please ask and answer questions here.
  - name: GitHub Security Pipeline Security Issues
    url: https://security-pipeline.example.com/security
    about: Please report security vulnerabilities here.
'''

# Write the config.yml file
with open(os.path.join(issue_template_dir, 'config.yml'), 'w') as f:
    f.write(config_yml)
    
# Create GitHub pull request template directory and file
pr_template_dir = os.path.join(output_dir, '.github')
os.makedirs(pr_template_dir, exist_ok=True)

# Create pull request template
pr_template = '''# 🚀 Pull Request

## 📝 Description
<!-- Provide a clear and concise description of what this PR does -->

## 🔄 Related Issue
<!-- Link to the issue this PR resolves -->
Closes #<!-- issue number -->

## 📋 Type of change
<!-- Mark the relevant option with an [x] -->

- [ ] 🐛 Bug fix (non-breaking change which fixes an issue)
- [ ] ✨ New feature (non-breaking change which adds functionality)
- [ ] 💥 Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] 📚 Documentation update
- [ ] 🧹 Code refactoring (no functional changes)
- [ ] 🛠️ Build/CI improvement
- [ ] ⚡ Performance improvement
- [ ] 🔒 Security enhancement

## 🧪 Testing
<!-- Describe the tests you've added for this change -->

- [ ] I have added unit tests that prove my fix is effective or that my feature works
- [ ] I have added integration tests (if appropriate)
- [ ] All new and existing tests passed

## 📸 Screenshots
<!-- If applicable, add screenshots to help explain your changes -->

## 📋 Checklist
<!-- Make sure your PR meets all expectations -->

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules
- [ ] I have checked my code and corrected any misspellings
- [ ] I have updated the CHANGELOG.md (if necessary)

## 🛡️ Security Considerations
<!-- If your changes involve security implications, please detail them here -->

## 🔍 Additional Context
<!-- Add any other context or information about the PR here -->
'''

# Write the pull request template
with open(os.path.join(pr_template_dir, 'PULL_REQUEST_TEMPLATE.md'), 'w') as f:
    f.write(pr_template)
    
# Create GitHub Actions workflow directory
workflows_dir = os.path.join(output_dir, '.github', 'workflows')
os.makedirs(workflows_dir, exist_ok=True)

# Create security scanning workflow
security_scan_workflow = '''name: 🛡️ Security Scanning

on:
  push:
    branches: [ main, master, develop ]
  pull_request:
    branches: [ main, master, develop ]
  schedule:
    - cron: '0 7 * * *'  # Run every day at 7 AM UTC
  workflow_dispatch:  # Allow manual triggering

jobs:
  security-scan:
    name: 🔍 Comprehensive Security Scan
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        include:
          - os: ubuntu-latest
            scan-depth: thorough
          - os: windows-latest
            scan-depth: standard
          - os: macos-latest
            scan-depth: standard
    
    steps:
      - name: ⬇️ Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0  # Full history for better secret detection
      
      - name: 🏗️ Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          cache: 'pip'
      
      - name: 📦 Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install gitleaks detect-secrets
      
      - name: 🔒 Run secret detection
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITLEAKS_CONFIG: .gitleaks.toml
          GITLEAKS_REPORT: gitleaks-report.json
      
      - name: 📊 Generate secret scanning report
        if: always()
        run: |
          python scripts/generate_security_report.py --input gitleaks-report.json --output security-report.md
      
      - name: 🧪 Run dependency vulnerability scan
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          format: 'sarif'
          output: 'dependency-report.sarif'
          severity: 'CRITICAL,HIGH'
      
      - name: 📤 Upload security analysis results
        uses: github/codeql-action/upload-sarif@v2
        if: always()
        with:
          sarif_file: dependency-report.sarif
      
      - name: 🏷️ Create GitHub issues for vulnerabilities
        if: github.event_name != 'pull_request' && matrix.os == 'ubuntu-latest'
        uses: actions/github-script@v6
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            const fs = require('fs');
            try {
              const reportPath = 'security-report.md';
              if (fs.existsSync(reportPath)) {
                const reportContent = fs.readFileSync(reportPath, 'utf8');
                if (reportContent.includes('CRITICAL') || reportContent.includes('HIGH')) {
                  await github.rest.issues.create({
                    owner: context.repo.owner,
                    repo: context.repo.repo,
                    title: '🚨 Security vulnerabilities detected',
                    body: reportContent,
                    labels: ['security', 'vulnerability', 'automated'],
                  });
                }
              }
            } catch (error) {
              console.error('Error creating issue:', error);
            }
      
      - name: 📝 Publish scan summary
        if: always()
        run: |
          echo "### 🛡️ Security Scan Results - ${{ matrix.os }}" >> $GITHUB_STEP_SUMMARY
          echo "Security scan completed with scan depth: ${{ matrix.scan-depth }}" >> $GITHUB_STEP_SUMMARY
          echo "| Check Type | Status | Details |" >> $GITHUB_STEP_SUMMARY
          echo "| --- | --- | --- |" >> $GITHUB_STEP_SUMMARY
          
          # Add secret scan results
          SECRET_COUNT=$(grep -c "CRITICAL\\|HIGH" gitleaks-report.json || echo "0")
          if [ "$SECRET_COUNT" -gt "0" ]; then
            echo "| Secret Detection | ❌ Failed | $SECRET_COUNT issues found |" >> $GITHUB_STEP_SUMMARY
          else
            echo "| Secret Detection | ✅ Passed | No critical issues |" >> $GITHUB_STEP_SUMMARY
          fi
          
          # Add dependency scan results
          DEP_COUNT=$(grep -c "CRITICAL\\|HIGH" dependency-report.sarif || echo "0")
          if [ "$DEP_COUNT" -gt "0" ]; then
            echo "| Dependency Check | ❌ Failed | $DEP_COUNT vulnerabilities |" >> $GITHUB_STEP_SUMMARY
          else
            echo "| Dependency Check | ✅ Passed | No critical vulnerabilities |" >> $GITHUB_STEP_SUMMARY
          fi
        shell: bash

  code-quality:
    name: 👨‍💻 Code Quality Analysis
    runs-on: ubuntu-latest
    needs: security-scan
    permissions:
      security-events: write
      
    steps:
      - name: ⬇️ Checkout code
        uses: actions/checkout@v3
        
      - name: 🔎 Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: javascript, python, go, java, ruby
          queries: security-and-quality
          config-file: ./.github/codeql.yml
      
      - name: 🧪 Autobuild
        uses: github/codeql-action/autobuild@v2
      
      - name: 🔍 Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v2
        with:
          category: "/language:${{matrix.language}}"

  notify:
    name: 📢 Notification
    runs-on: ubuntu-latest
    needs: [security-scan, code-quality]
    if: always()
    steps:
      - name: 📧 Send Notification
        uses: slackapi/slack-github-action@v1.23.0
        with:
          payload: |
            {
              "text": "🛡️ Security Scan Results: ${{ job.status == 'success' && '✅ Passed' || '❌ Failed' }}",
              "blocks": [
                {
                  "type": "header",
                  "text": {
                    "type": "plain_text",
                    "text": "🛡️ Security Scan Results for ${{ github.repository }}",
                    "emoji": true
                  }
                },
                {
                  "type": "section",
                  "fields": [
                    {
                      "type": "mrkdwn",
                      "text": "*Status:* ${{ needs.security-scan.result == 'success' && '✅ Passed' || '❌ Failed' }}"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Branch:* ${{ github.ref_name }}"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Triggered by:* ${{ github.event_name }}"
                    },
                    {
                      "type": "mrkdwn",
                      "text": "*Run:* <${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}|View Details>"
                    }
                  ]
                }
              ]
            }
        env:
          SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK_URL }}
          SLACK_WEBHOOK_TYPE: INCOMING_WEBHOOK
'''

# Write the security scan workflow
with open(os.path.join(workflows_dir, 'security-scan.yml'), 'w') as f:
    f.write(security_scan_workflow)

# Create dependency check workflow
dependency_check_workflow = '''name: 📦 Dependency Vulnerability Scan

on:
  push:
    branches: [ main, master, develop ]
    paths:
      - '**/*.json'
      - '**/*.xml'
      - '**/*.gradle'
      - '**/requirements*.txt'
      - '**/go.mod'
      - '**/go.sum'
      - '**/Gemfile'
      - '**/Gemfile.lock'
      - '**/pom.xml'
      - '**/package.json'
      - '**/package-lock.json'
      - '**/yarn.lock'
  pull_request:
    branches: [ main, master, develop ]
    paths:
      - '**/*.json'
      - '**/*.xml'
      - '**/*.gradle'
      - '**/requirements*.txt'
      - '**/go.mod'
      - '**/go.sum'
      - '**/Gemfile'
      - '**/Gemfile.lock'
      - '**/pom.xml'
      - '**/package.json'
      - '**/package-lock.json'
      - '**/yarn.lock'
  schedule:
    - cron: '0 4 * * 1' # Run every Monday at 4 AM UTC
  workflow_dispatch:  # Allow manual triggering

jobs:
  dependency-check:
    name: 🔍 Dependency Vulnerability Check
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
      pull-requests: write
    
    strategy:
      fail-fast: false
      matrix:
        language: [javascript, python, java, ruby, go]
        include:
          - language: javascript
            patterns: "package*.json"
            tool: npm
          - language: python
            patterns: "requirements*.txt,setup.py"
            tool: pip
          - language: java
            patterns: "pom.xml,build.gradle"
            tool: maven
          - language: ruby
            patterns: "Gemfile,Gemfile.lock"
            tool: bundler
          - language: go
            patterns: "go.mod,go.sum"
            tool: gomod
    
    steps:
      - name: ⬇️ Checkout code
        uses: actions/checkout@v3
        
      - name: 🔍 Look for dependency files
        id: check_files
        run: |
          IFS=',' read -ra PATTERNS <<< "${{ matrix.patterns }}"
          for PATTERN in "${PATTERNS[@]}"; do
            if compgen -G "$PATTERN" > /dev/null; then
              echo "FOUND_FILES=true" >> $GITHUB_OUTPUT
              break
            fi
          done
          
      - name: 📋 Setup Dependency Check
        if: steps.check_files.outputs.FOUND_FILES == 'true'
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'
        
      - name: 🧪 Run OWASP Dependency Check
        if: steps.check_files.outputs.FOUND_FILES == 'true'
        uses: dependency-check/Dependency-Check_Action@main
        id: dependency-check
        with:
          project: '${{ github.repository }}'
          path: '.'
          format: 'SARIF'
          out: '${{ github.workspace }}/reports' 
          args: >
            --enableExperimental
            --exclude "**/*-test.jar"
            --suppression .github/dependency-check-suppressions.xml
            --failOnCVSS 7
            --enableRetired
      
      - name: 📤 Upload Dependency Check results
        if: steps.check_files.outputs.FOUND_FILES == 'true' && always()
        uses: github/codeql-action/upload-sarif@v2
        with:
          sarif_file: ${{ github.workspace }}/reports/dependency-check-report.sarif
          
      - name: 🔄 Upload Dependency Check Report
        if: steps.check_files.outputs.FOUND_FILES == 'true' && always()
        uses: actions/upload-artifact@v3
        with:
          name: Dependency-Check-Report-${{ matrix.language }}
          path: ${{ github.workspace }}/reports
          
      - name: 🚨 Comment PR with Vulnerability Summary
        if: steps.check_files.outputs.FOUND_FILES == 'true' && github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            const fs = require('fs');
            try {
              // Basic parsing of the report to extract vulnerability counts
              const reportPath = '${{ github.workspace }}/reports/dependency-check-report.json';
              if (fs.existsSync(reportPath)) {
                const report = JSON.parse(fs.readFileSync(reportPath, 'utf8'));
                const dependencies = report.dependencies || [];
                
                // Count vulnerabilities by severity
                const vulnCount = { critical: 0, high: 0, medium: 0, low: 0 };
                dependencies.forEach(dep => {
                  const vulns = dep.vulnerabilities || [];
                  vulns.forEach(vuln => {
                    const cvssScore = vuln.cvssv3 ? vuln.cvssv3.baseScore : (vuln.cvssv2 ? vuln.cvssv2.score : 0);
                    if (cvssScore >= 9.0) vulnCount.critical++;
                    else if (cvssScore >= 7.0) vulnCount.high++;
                    else if (cvssScore >= 4.0) vulnCount.medium++;
                    else if (cvssScore > 0) vulnCount.low++;
                  });
                });
                
                // Create comment body
                let commentBody = `## 📦 Dependency Vulnerability Scan Results for ${{ matrix.language }}
                
| Severity | Count | Threshold |
|----------|-------|-----------|
| 🔴 Critical | ${vulnCount.critical} | Must fix |
| 🟠 High | ${vulnCount.high} | Should fix |
| 🟡 Medium | ${vulnCount.medium} | Consider fixing |
| 🟢 Low | ${vulnCount.low} | Be aware |

`;
                
                // Add recommendations based on findings
                if (vulnCount.critical > 0 || vulnCount.high > 0) {
                  commentBody += `### ⚠️ Action Required
This PR introduces dependencies with Critical or High vulnerabilities that should be addressed before merging.`;
                } else if (vulnCount.medium > 0) {
                  commentBody += `### ℹ️ Attention
This PR introduces dependencies with Medium vulnerabilities that should be reviewed.`;
                } else {
                  commentBody += `### ✅ All Good
No significant vulnerabilities detected in dependencies.`;
                }
                
                // Post comment on PR
                const { data: comments } = await github.rest.issues.listComments({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: context.issue.number,
                });
                
                const botComment = comments.find(comment => {
                  return comment.user.login === 'github-actions[bot]' && 
                         comment.body.includes('Dependency Vulnerability Scan Results for ${{ matrix.language }}');
                });
                
                if (botComment) {
                  await github.rest.issues.updateComment({
                    owner: context.repo.owner,
                    repo: context.repo.repo,
                    comment_id: botComment.id,
                    body: commentBody
                  });
                } else {
                  await github.rest.issues.createComment({
                    owner: context.repo.owner,
                    repo: context.repo.repo,
                    issue_number: context.issue.number,
                    body: commentBody
                  });
                }
              }
            } catch (error) {
              console.error('Error posting comment:', error);
            }

      - name: 📝 Publish scan summary
        if: steps.check_files.outputs.FOUND_FILES == 'true' && always()
        run: |
          echo "### 📦 Dependency Check Results - ${{ matrix.language }}" >> $GITHUB_STEP_SUMMARY
          echo "Dependency check completed using ${{ matrix.tool }}" >> $GITHUB_STEP_SUMMARY
          
          if [ -f "${{ github.workspace }}/reports/dependency-check-report.json" ]; then
            # Extract and display basic statistics from the report
            CRITICAL=$(jq -r '.dependencies | map(.vulnerabilities // []) | flatten | map(select(.cvssv3.baseScore >= 9.0)) | length' ${{ github.workspace }}/reports/dependency-check-report.json)
            HIGH=$(jq -r '.dependencies | map(.vulnerabilities // []) | flatten | map(select(.cvssv3.baseScore >= 7.0 and .cvssv3.baseScore < 9.0)) | length' ${{ github.workspace }}/reports/dependency-check-report.json)
            MEDIUM=$(jq -r '.dependencies | map(.vulnerabilities // []) | flatten | map(select(.cvssv3.baseScore >= 4.0 and .cvssv3.baseScore < 7.0)) | length' ${{ github.workspace }}/reports/dependency-check-report.json)
            LOW=$(jq -r '.dependencies | map(.vulnerabilities // []) | flatten | map(select(.cvssv3.baseScore > 0 and .cvssv3.baseScore < 4.0)) | length' ${{ github.workspace }}/reports/dependency-check-report.json)
            
            echo "| Severity | Count |" >> $GITHUB_STEP_SUMMARY
            echo "| --- | --- |" >> $GITHUB_STEP_SUMMARY
            echo "| 🔴 Critical | $CRITICAL |" >> $GITHUB_STEP_SUMMARY
            echo "| 🟠 High | $HIGH |" >> $GITHUB_STEP_SUMMARY
            echo "| 🟡 Medium | $MEDIUM |" >> $GITHUB_STEP_SUMMARY
            echo "| 🟢 Low | $LOW |" >> $GITHUB_STEP_SUMMARY
            
            if [ "$CRITICAL" -gt 0 ] || [ "$HIGH" -gt 0 ]; then
              echo "⚠️ **Critical or High vulnerabilities detected!** Please review the full report." >> $GITHUB_STEP_SUMMARY
            fi
          else
            echo "No dependency report generated or no vulnerabilities found." >> $GITHUB_STEP_SUMMARY
          fi
        shell: bash
'''

# Write the dependency check workflow
with open(os.path.join(workflows_dir, 'dependency-check.yml'), 'w') as f:
    f.write(dependency_check_workflow)
    
    
# Create secret scanning workflow
secret_scan_workflow = '''name: 🔒 Secret Detection

on:
  push:
    branches: [ '*' ]
  pull_request:
    types: [opened, synchronize]
  schedule:
    - cron: '0 1 * * *'  # Run every day at 1 AM UTC
  workflow_dispatch:  # Allow manual triggering

jobs:
  detect-secrets:
    name: 🔍 Detect Secrets
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pull-requests: write
      security-events: write
    
    steps:
      - name: ⬇️ Checkout repository
        uses: actions/checkout@v3
        with:
          fetch-depth: 0  # Fetch all history for all branches and tags
          
      - name: 🔎 Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          
      - name: 🛠️ Install Gitleaks
        run: |
          wget -q https://github.com/gitleaks/gitleaks/releases/download/v8.16.1/gitleaks_8.16.1_linux_x64.tar.gz
          tar -xzf gitleaks_8.16.1_linux_x64.tar.gz
          chmod +x gitleaks
          sudo mv gitleaks /usr/local/bin/
          
      - name: 📦 Install detect-secrets
        run: |
          python -m pip install --upgrade pip
          pip install detect-secrets
          
      - name: 🧪 Run Gitleaks
        id: gitleaks
        run: |
          mkdir -p reports
          if [ "${{ github.event_name }}" == "pull_request" ]; then
            # For PR events, only scan new/modified content
            gitleaks detect --source="." --report-path=reports/gitleaks-report.json \
              --report-format=json --no-git --verbose --redact \
              --config=.gitleaks.toml || true
          else
            # For other events, scan entire repository history
            gitleaks detect --source="." --report-path=reports/gitleaks-report.json \
              --report-format=json --verbose --redact \
              --config=.gitleaks.toml || true
          fi
          
          if [ -s reports/gitleaks-report.json ]; then
            echo "Found potential secrets, see report for details."
            echo "SECRETS_FOUND=true" >> $GITHUB_OUTPUT
          else
            echo "No secrets found."
            echo "SECRETS_FOUND=false" >> $GITHUB_OUTPUT
          fi

      - name: 🧪 Run detect-secrets
        id: detect_secrets
        run: |
          # Run detect-secrets and save results
          detect-secrets scan --all-files --exclude-files '\.github/workflows/.*' > reports/detect-secrets-report.json
          
          # Check if any secrets were found (non-empty results)
          if [ "$(jq 'has("results")' reports/detect-secrets-report.json)" = "true" ] && \
             [ "$(jq '.results | length > 0' reports/detect-secrets-report.json)" = "true" ]; then
            echo "Found potential secrets with detect-secrets."
            echo "SECRETS_FOUND=true" >> $GITHUB_OUTPUT
          else
            echo "No secrets found with detect-secrets."
            echo "SECRETS_FOUND=false" >> $GITHUB_OUTPUT
          fi

      - name: 🔍 Analyze custom patterns
        id: custom_patterns
        run: |
          # Check for custom security patterns like API keys, tokens, etc.
          # using more targeted regex for higher precision
          
          mkdir -p reports
          
          # Define patterns to search for
          cat > patterns.txt <<EOF
          # AWS Keys
          (A3T[A-Z0-9]|AKIA|AGPA|AIDA|AROA|AIPA|ANPA|ANVA|ASIA)[A-Z0-9]{16}
          
          # GitHub Personal Access Token
          ghp_[a-zA-Z0-9]{36}
          github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}
          
          # Database Connection Strings
          jdbc:[a-z]+://[a-zA-Z0-9\.\-_:]+/[a-zA-Z0-9\.\-_]+(\?user=[a-zA-Z0-9\.\-_]+&password=[^&\s]+)
          
          # Generic API Keys
          api[_-]?key[_-]?([a-zA-Z0-9]{32,45})
          
          # Authentication tokens
          bearer [a-zA-Z0-9_\-\.=]+
          authorization: basic [a-zA-Z0-9_\-\.=]+
          authorization: token [a-zA-Z0-9_\-\.=]+
          
          # SSH Private Keys
          -----BEGIN RSA PRIVATE KEY-----
          -----BEGIN DSA PRIVATE KEY-----
          -----BEGIN EC PRIVATE KEY-----
          -----BEGIN OPENSSH PRIVATE KEY-----
          
          # Certificate files
          -----BEGIN CERTIFICATE-----
          
          # Encryption keys
          -----BEGIN PGP PRIVATE KEY BLOCK-----
          EOF
          
          # Count matches, excluding false positives and test fixtures
          FOUND_COUNT=0
          while IFS= read -r line; do
            # Skip comments and empty lines
            [[ "$line" =~ ^#.*$ ]] && continue
            [[ -z "$line" ]] && continue
            
            MATCHES=$(find . -type f \
              -not -path "*/node_modules/*" \
              -not -path "*/vendor/*" \
              -not -path "*/.git/*" \
              -not -path "*/test/fixtures/*" \
              -not -path "*/tests/data/*" \
              -exec grep -l -E "$line" {} \; | wc -l)
            
            FOUND_COUNT=$((FOUND_COUNT + MATCHES))
          done < patterns.txt
          
          if [ "$FOUND_COUNT" -gt 0 ]; then
            echo "Found $FOUND_COUNT potential security issues with custom patterns."
            echo "SECRETS_FOUND=true" >> $GITHUB_OUTPUT
          else
            echo "No issues found with custom patterns."
            echo "SECRETS_FOUND=false" >> $GITHUB_OUTPUT
          fi

      - name: 📄 Generate Final Report
        if: steps.gitleaks.outputs.SECRETS_FOUND == 'true' || steps.detect_secrets.outputs.SECRETS_FOUND == 'true' || steps.custom_patterns.outputs.SECRETS_FOUND == 'true'
        run: |
          cat > reports/secret-scan-summary.md << EOF
          # 🔒 Secret Detection Report
          
          ## Summary
          
          The automated secret scanning tools have identified potential secrets or sensitive data in this repository.
          
          | Tool | Secrets Found | Risk Level |
          | ---- | ------------ | ---------- |
          | Gitleaks | ${{ steps.gitleaks.outputs.SECRETS_FOUND == 'true' && '⚠️ Yes' || '✅ No' }} | ${{ steps.gitleaks.outputs.SECRETS_FOUND == 'true' && '🔴 High' || '🟢 None' }} |
          | detect-secrets | ${{ steps.detect_secrets.outputs.SECRETS_FOUND == 'true' && '⚠️ Yes' || '✅ No' }} | ${{ steps.detect_secrets.outputs.SECRETS_FOUND == 'true' && '🔴 High' || '🟢 None' }} |
          | Custom Patterns | ${{ steps.custom_patterns.outputs.SECRETS_FOUND == 'true' && '⚠️ Yes' || '✅ No' }} | ${{ steps.custom_patterns.outputs.SECRETS_FOUND == 'true' && '🔴 High' || '🟢 None' }} |
          
          ## 🚨 Action Required
          
          Potential secrets have been detected in this repository. This is a security risk that needs immediate attention.
          
          ### Next Steps
          
          1. **Review the detected secrets** in the reports
          2. **Revoke any exposed credentials** immediately
          3. **Remove the secrets** from the repository
          4. **Use secure methods** to store secrets:
             - GitHub Secrets
             - Environment variables
             - Secret management services
          5. **Add false positives** to the `.gitleaks.allow` file
          
          ## Resources
          
          - [GitHub Secret Scanning](https://docs.github.com/en/code-security/secret-scanning)
          - [Secret Management Best Practices](https://security-pipeline.example.com/docs/secrets)
          - [How to Properly Rotate Credentials](https://security-pipeline.example.com/guides/credential-rotation)
          EOF

      - name: 🚨 Block PR if secrets are found
        if: github.event_name == 'pull_request' && (steps.gitleaks.outputs.SECRETS_FOUND == 'true' || steps.detect_secrets.outputs.SECRETS_FOUND == 'true' || steps.custom_patterns.outputs.SECRETS_FOUND == 'true')
        uses: actions/github-script@v6
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            const fs = require('fs');
            
            // Read the summary report
            const reportContent = fs.readFileSync('reports/secret-scan-summary.md', 'utf8');
            
            // Create or update comment on PR
            const { data: comments } = await github.rest.issues.listComments({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number
            });
            
            const botComment = comments.find(comment => {
              return comment.user.login === 'github-actions[bot]' && 
                    comment.body.includes('Secret Detection Report');
            });
            
            if (botComment) {
              await github.rest.issues.updateComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                comment_id: botComment.id,
                body: reportContent
              });
            } else {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.issue.number,
                body: reportContent
              });
            }
            
            // Block the PR by creating a review
            await github.rest.pulls.createReview({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number,
              event: 'REQUEST_CHANGES',
              body: '🚫 **This PR is blocked due to detected secrets**\n\nPlease review the security scan results and remove any secrets or credentials from this PR. Once removed, request a re-review.'
            });
            
            core.setFailed('Pull request blocked due to potential secrets detected.');

      - name: 📊 Upload scan results as artifact
        if: always()
        uses: actions/upload-artifact@v3
        with:
          name: secret-scan-results
          path: reports/
          retention-days: 5

      - name: 📝 Publish scan summary
        if: always()
        run: |
          echo "### 🔒 Secret Detection Results" >> $GITHUB_STEP_SUMMARY
          
          echo "| Tool | Status | Details |" >> $GITHUB_STEP_SUMMARY
          echo "| --- | --- | --- |" >> $GITHUB_STEP_SUMMARY
          
          # Gitleaks results
          if [ "${{ steps.gitleaks.outputs.SECRETS_FOUND }}" == "true" ]; then
            echo "| Gitleaks | ❌ Failed | Secrets detected |" >> $GITHUB_STEP_SUMMARY
          else
            echo "| Gitleaks | ✅ Passed | No secrets found |" >> $GITHUB_STEP_SUMMARY
          fi
          
          # detect-secrets results
          if [ "${{ steps.detect_secrets.outputs.SECRETS_FOUND }}" == "true" ]; then
            echo "| detect-secrets | ❌ Failed | Secrets detected |" >> $GITHUB_STEP_SUMMARY
          else
            echo "| detect-secrets | ✅ Passed | No secrets found |" >> $GITHUB_STEP_SUMMARY
          fi
          
          # Custom patterns results
          if [ "${{ steps.custom_patterns.outputs.SECRETS_FOUND }}" == "true" ]; then
            echo "| Custom Patterns | ❌ Failed | Sensitive data detected |" >> $GITHUB_STEP_SUMMARY
          else
            echo "| Custom Patterns | ✅ Passed | No sensitive data found |" >> $GITHUB_STEP_SUMMARY
          fi
          
          # Overall status
          if [ "${{ steps.gitleaks.outputs.SECRETS_FOUND }}" == "true" ] || [ "${{ steps.detect_secrets.outputs.SECRETS_FOUND }}" == "true" ] || [ "${{ steps.custom_patterns.outputs.SECRETS_FOUND }}" == "true" ]; then
            echo "### ⚠️ Action Required" >> $GITHUB_STEP_SUMMARY
            echo "Potential secrets detected. See the detailed report in the workflow artifacts." >> $GITHUB_STEP_SUMMARY
          else
            echo "### ✅ All Clear" >> $GITHUB_STEP_SUMMARY
            echo "No secrets or sensitive data detected in this scan." >> $GITHUB_STEP_SUMMARY
          fi
'''

# Write the secret scan workflow
with open(os.path.join(workflows_dir, 'secret-scan.yml'), 'w') as f:
    f.write(secret_scan_workflow)
    
    
# Create code quality workflow
code_quality_workflow = '''name: 🧹 Code Quality

on:
  push:
    branches: [ main, master, develop ]
  pull_request:
    branches: [ main, master, develop ]
  schedule:
    - cron: '0 3 * * *'  # Run every day at 3 AM UTC
  workflow_dispatch:  # Allow manual triggering

jobs:
  code-quality:
    name: 📊 Static Code Analysis
    runs-on: ${{ matrix.os }}
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest]
        language: [python, javascript, go, java]
        include:
          - language: python
            extensions: '**/*.py'
            linter: pylint
          - language: javascript
            extensions: '**/*.js,**/*.jsx,**/*.ts,**/*.tsx'
            linter: eslint
          - language: go
            extensions: '**/*.go'
            linter: golangci-lint
          - language: java
            extensions: '**/*.java'
            linter: checkstyle
            
    steps:
      - name: ⬇️ Checkout code
        uses: actions/checkout@v3
        
      - name: 🔍 Find files of language type
        id: find-files
        run: |
          # Check if files of the current language type exist in the repository
          IFS=',' read -ra PATTERNS <<< "${{ matrix.extensions }}"
          FILES_FOUND=false
          
          for PATTERN in "${PATTERNS[@]}"; do
            if compgen -G "$PATTERN" > /dev/null 2>&1; then
              FILES_FOUND=true
              break
            fi
          done
          
          echo "FILES_FOUND=$FILES_FOUND" >> $GITHUB_OUTPUT
        shell: bash

      # Setup for Python analysis
      - name: 🐍 Set up Python
        if: matrix.language == 'python' && steps.find-files.outputs.FILES_FOUND == 'true'
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          cache: 'pip'
          
      - name: 📦 Install Python dependencies
        if: matrix.language == 'python' && steps.find-files.outputs.FILES_FOUND == 'true'
        run: |
          python -m pip install --upgrade pip
          pip install pylint flake8 black mypy bandit
          pip install -r requirements.txt || echo "No requirements.txt found"
          
      - name: 🧪 Run Python analysis
        if: matrix.language == 'python' && steps.find-files.outputs.FILES_FOUND == 'true'
        run: |
          mkdir -p reports
          
          echo "Running Pylint..."
          pylint --output-format=json --reports=y $(git ls-files '*.py') > reports/pylint-report.json || true
          
          echo "Running Flake8..."
          flake8 --format=pylint --output-file=reports/flake8-report.txt $(git ls-files '*.py') || true
          
          echo "Running Black in check mode..."
          black --check $(git ls-files '*.py') > reports/black-report.txt || true
          
          echo "Running MyPy for type checking..."
          mypy --ignore-missing-imports --show-error-codes $(git ls-files '*.py') > reports/mypy-report.txt || true
          
          echo "Running Bandit security checks..."
          bandit -r . -f json -o reports/bandit-report.json || true
      
      # Setup for JavaScript analysis
      - name: 📄 Set up Node.js
        if: matrix.language == 'javascript' && steps.find-files.outputs.FILES_FOUND == 'true'
        uses: actions/setup-node@v3
        with:
          node-version: '16'
          cache: 'npm'
          
      - name: 📦 Install JavaScript dependencies
        if: matrix.language == 'javascript' && steps.find-files.outputs.FILES_FOUND == 'true'
        run: |
          if [ -f package.json ]; then
            npm ci
          else
            npm init -y
            npm install --save-dev eslint prettier eslint-config-prettier eslint-plugin-security
          fi
          
      - name: 🧪 Run JavaScript analysis
        if: matrix.language == 'javascript' && steps.find-files.outputs.FILES_FOUND == 'true'
        run: |
          mkdir -p reports
          
          # Create basic eslint config if it doesn't exist
          if [ ! -f .eslintrc.json ]; then
            echo '{
              "env": {
                "browser": true,
                "es2021": true,
                "node": true
              },
              "extends": [
                "eslint:recommended",
                "plugin:security/recommended"
              ],
              "plugins": [
                "security"
              ],
              "parserOptions": {
                "ecmaVersion": "latest",
                "sourceType": "module"
              }
            }' > .eslintrc.json
          fi
          
          # Run ESLint
          npx eslint --output-file reports/eslint-report.json --format json $(git ls-files '*.js' '*.jsx' '*.ts' '*.tsx') || true
          
          # Run Prettier in check mode
          npx prettier --check $(git ls-files '*.js' '*.jsx' '*.ts' '*.tsx') > reports/prettier-report.txt || true
          
      # Setup for Go analysis
      - name: 📑 Set up Go
        if: matrix.language == 'go' && steps.find-files.outputs.FILES_FOUND == 'true'
        uses: actions/setup-go@v3
        with:
          go-version: '1.19'
          
      - name: 📦 Install Go dependencies
        if: matrix.language == 'go' && steps.find-files.outputs.FILES_FOUND == 'true'
        run: |
          go mod download || echo "No go.mod found"
          curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/master/install.sh | sh -s -- -b $(go env GOPATH)/bin v1.50.1
          
      - name: 🧪 Run Go analysis
        if: matrix.language == 'go' && steps.find-files.outputs.FILES_FOUND == 'true'
        run: |
          mkdir -p reports
          
          # Run Go vet
          go vet ./... > reports/govet-report.txt || true
          
          # Run golangci-lint 
          golangci-lint run --out-format json > reports/golangci-lint-report.json || true
      
      # Setup for Java analysis
      - name: ☕ Set up Java
        if: matrix.language == 'java' && steps.find-files.outputs.FILES_FOUND == 'true'
        uses: actions/setup-java@v3
        with:
          distribution: 'temurin'
          java-version: '17'
          
      - name: 📦 Install Java dependencies
        if: matrix.language == 'java' && steps.find-files.outputs.FILES_FOUND == 'true'
        run: |
          wget -q https://github.com/checkstyle/checkstyle/releases/download/checkstyle-10.3.3/checkstyle-10.3.3-all.jar
          
      - name: 🧪 Run Java analysis
        if: matrix.language == 'java' && steps.find-files.outputs.FILES_FOUND == 'true'
        run: |
          mkdir -p reports
          
          # Run checkstyle
          java -jar checkstyle-10.3.3-all.jar -c /google_checks.xml $(git ls-files '*.java') > reports/checkstyle-report.txt || true

      # Generate combined report      
      - name: 📊 Generate combined code quality report
        if: steps.find-files.outputs.FILES_FOUND == 'true'
        run: |
          echo "# Code Quality Report for ${{ matrix.language }}" > reports/combined-report.md
          echo "" >> reports/combined-report.md
          echo "## Summary" >> reports/combined-report.md
          echo "" >> reports/combined-report.md
          
          case "${{ matrix.language }}" in
            python)
              # Process Python reports
              echo "### Pylint Summary" >> reports/combined-report.md
              if [ -f reports/pylint-report.json ]; then
                # Extract statistics from Pylint JSON output (simplified)
                echo "Pylint output available in artifacts" >> reports/combined-report.md
              else
                echo "No Pylint report generated" >> reports/combined-report.md
              fi
              
              echo "" >> reports/combined-report.md
              echo "### Bandit Security Summary" >> reports/combined-report.md
              if [ -f reports/bandit-report.json ]; then
                # Count security issues by severity
                HIGH=$(grep -c "HIGH" reports/bandit-report.json || echo "0")
                MEDIUM=$(grep -c "MEDIUM" reports/bandit-report.json || echo "0")
                LOW=$(grep -c "LOW" reports/bandit-report.json || echo "0")
                echo "- High severity issues: $HIGH" >> reports/combined-report.md
                echo "- Medium severity issues: $MEDIUM" >> reports/combined-report.md
                echo "- Low severity issues: $LOW" >> reports/combined-report.md
              else
                echo "No Bandit report generated" >> reports/combined-report.md
              fi
              ;;
              
            javascript)
              # Process JavaScript reports
              echo "### ESLint Summary" >> reports/combined-report.md
              if [ -f reports/eslint-report.json ]; then
                ERRORS=$(grep -c "\"severity\":2" reports/eslint-report.json || echo "0")
                WARNINGS=$(grep -c "\"severity\":1" reports/eslint-report.json || echo "0")
                echo "- Errors: $ERRORS" >> reports/combined-report.md
                echo "- Warnings: $WARNINGS" >> reports/combined-report.md
              else
                echo "No ESLint report generated" >> reports/combined-report.md
              fi
              ;;
              
            go)
              # Process Go reports
              echo "### Go Analysis Summary" >> reports/combined-report.md
              if [ -f reports/golangci-lint-report.json ]; then
                ISSUES=$(grep -c "\"Text\":" reports/golangci-lint-report.json || echo "0")
                echo "- Issues found: $ISSUES" >> reports/combined-report.md
              else
                echo "No golangci-lint report generated" >> reports/combined-report.md
              fi
              ;;
              
            java)
              # Process Java reports
              echo "### Checkstyle Summary" >> reports/combined-report.md
              if [ -f reports/checkstyle-report.txt ]; then
                ERRORS=$(grep -c "ERROR" reports/checkstyle-report.txt || echo "0")
                WARNINGS=$(grep -c "WARNING" reports/checkstyle-report.txt || echo "0")
                echo "- Errors: $ERRORS" >> reports/combined-report.md
                echo "- Warnings: $WARNINGS" >> reports/combined-report.md
              else
                echo "No Checkstyle report generated" >> reports/combined-report.md
              fi
              ;;
          esac
          
          echo "" >> reports/combined-report.md
          echo "## Recommendations" >> reports/combined-report.md
          echo "" >> reports/combined-report.md
          echo "Please review the detailed reports in the workflow artifacts for specific issues and recommendations." >> reports/combined-report.md
          
      - name: 📂 Upload analysis results
        if: steps.find-files.outputs.FILES_FOUND == 'true'
        uses: actions/upload-artifact@v3
        with:
          name: code-quality-${{ matrix.language }}-report
          path: reports/
          retention-days: 7

      - name: 🔍 Extract results for PR comment
        if: github.event_name == 'pull_request' && steps.find-files.outputs.FILES_FOUND == 'true'
        id: results
        run: |
          # Calculate a simple quality score
          SCORE=100  # Start with perfect score
          
          case "${{ matrix.language }}" in
            python)
              if [ -f reports/pylint-report.json ] && grep -q "error" reports/pylint-report.json; then
                ERROR_COUNT=$(grep -c "error" reports/pylint-report.json)
                SCORE=$((SCORE - ERROR_COUNT * 5))  # Deduct 5 points per error
              fi
              
              if [ -f reports/bandit-report.json ]; then
                HIGH=$(grep -c "HIGH" reports/bandit-report.json || echo "0")
                MEDIUM=$(grep -c "MEDIUM" reports/bandit-report.json || echo "0")
                SCORE=$((SCORE - HIGH * 10 - MEDIUM * 5))  # Deduct 10 points per high issue, 5 per medium
              fi
              ;;
              
            javascript)
              if [ -f reports/eslint-report.json ]; then
                ERRORS=$(grep -c "\"severity\":2" reports/eslint-report.json || echo "0")
                WARNINGS=$(grep -c "\"severity\":1" reports/eslint-report.json || echo "0")
                SCORE=$((SCORE - ERRORS * 5 - WARNINGS * 2))  # Deduct 5 per error, 2 per warning
              fi
              ;;
              
            go)
              if [ -f reports/golangci-lint-report.json ]; then
                ISSUES=$(grep -c "\"Text\":" reports/golangci-lint-report.json || echo "0")
                SCORE=$((SCORE - ISSUES * 3))  # Deduct 3 points per issue
              fi
              ;;
              
            java)
              if [ -f reports/checkstyle-report.txt ]; then
                ERRORS=$(grep -c "ERROR" reports/checkstyle-report.txt || echo "0")
                WARNINGS=$(grep -c "WARNING" reports/checkstyle-report.txt || echo "0")
                SCORE=$((SCORE - ERRORS * 5 - WARNINGS * 2))  # Deduct 5 per error, 2 per warning
              fi
              ;;
          esac
          
          # Ensure score doesn't go below 0
          if [ $SCORE -lt 0 ]; then
            SCORE=0
          fi
          
          # Set output for next step
          echo "QUALITY_SCORE=$SCORE" >> $GITHUB_OUTPUT
          
      - name: 💬 Comment on PR
        if: github.event_name == 'pull_request' && steps.find-files.outputs.FILES_FOUND == 'true'
        uses: actions/github-script@v6
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            const fs = require('fs');
            const score = Number('${{ steps.results.outputs.QUALITY_SCORE }}');
            let scoreColor, recommendation;
            
            // Determine score color and recommendation based on score
            if (score >= 90) {
              scoreColor = '🟢';
              recommendation = 'Excellent code quality! Keep up the good work.';
            } else if (score >= 70) {
              scoreColor = '🟡';
              recommendation = 'Good code quality, but there\'s room for improvement. Please address the issues found.';
            } else if (score >= 50) {
              scoreColor = '🟠';
              recommendation = 'Mediocre code quality. Several issues should be fixed before merging.';
            } else {
              scoreColor = '🔴';
              recommendation = 'Poor code quality. Please fix the identified issues before this PR can be merged.';
            }
            
            // Read the combined report
            let reportContent;
            try {
              reportContent = fs.readFileSync('reports/combined-report.md', 'utf8');
            } catch (error) {
              reportContent = 'No detailed report available.';
            }
            
            // Create comment body
            const body = `## 🧹 Code Quality Analysis: ${scoreColor} ${score}/100
            
            ${recommendation}
            
            ### Details for ${{ matrix.language }}
            
            ${reportContent}
            
            [View full report in workflow artifacts](${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }})`;
            
            // Look for existing comment
            const { data: comments } = await github.rest.issues.listComments({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number
            });
            
            const commentMarker = '## 🧹 Code Quality Analysis:';
            const existingComment = comments.find(comment => 
              comment.user.login === 'github-actions[bot]' && 
              comment.body.includes(commentMarker) &&
              comment.body.includes(`Details for ${{ matrix.language }}`)
            );
            
            // Update or create comment
            if (existingComment) {
              await github.rest.issues.updateComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                comment_id: existingComment.id,
                body
              });
            } else {
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.issue.number,
                body
              });
            }

      - name: 📝 Publish scan summary
        if: steps.find-files.outputs.FILES_FOUND == 'true'
        run: |
          echo "### 🧹 Code Quality Results - ${{ matrix.language }}" >> $GITHUB_STEP_SUMMARY
          
          QUALITY_SCORE="${{ steps.results.outputs.QUALITY_SCORE }}"
          if [ -z "$QUALITY_SCORE" ]; then
            QUALITY_SCORE="N/A"
          fi
          
          echo "| Metric | Value |" >> $GITHUB_STEP_SUMMARY
          echo "| --- | --- |" >> $GITHUB_STEP_SUMMARY
          echo "| Language | ${{ matrix.language }} |" >> $GITHUB_STEP_SUMMARY
          echo "| Quality Score | $QUALITY_SCORE/100 |" >> $GITHUB_STEP_SUMMARY
          
          case "${{ matrix.language }}" in
            python)
              if [ -f reports/pylint-report.json ]; then
                ERRORS=$(grep -c "error" reports/pylint-report.json || echo "0")
                WARNINGS=$(grep -c "warning" reports/pylint-report.json || echo "0")
                echo "| Pylint Errors | $ERRORS |" >> $GITHUB_STEP_SUMMARY
                echo "| Pylint Warnings | $WARNINGS |" >> $GITHUB_STEP_SUMMARY
              fi
              
              if [ -f reports/bandit-report.json ]; then
                HIGH=$(grep -c "HIGH" reports/bandit-report.json || echo "0")
                MEDIUM=$(grep -c "MEDIUM" reports/bandit-report.json || echo "0")
                echo "| Security High | $HIGH |" >> $GITHUB_STEP_SUMMARY
                echo "| Security Medium | $MEDIUM |" >> $GITHUB_STEP_SUMMARY
              fi
              ;;
              
            javascript)
              if [ -f reports/eslint-report.json ]; then
                ERRORS=$(grep -c "\"severity\":2" reports/eslint-report.json || echo "0")
                WARNINGS=$(grep -c "\"severity\":1" reports/eslint-report.json || echo "0")
                echo "| ESLint Errors | $ERRORS |" >> $GITHUB_STEP_SUMMARY
                echo "| ESLint Warnings | $WARNINGS |" >> $GITHUB_STEP_SUMMARY
              fi
              ;;
              
            go)
              if [ -f reports/golangci-lint-report.json ]; then
                ISSUES=$(grep -c "\"Text\":" reports/golangci-lint-report.json || echo "0")
                echo "| Go Issues | $ISSUES |" >> $GITHUB_STEP_SUMMARY
              fi
              ;;
              
            java)
              if [ -f reports/checkstyle-report.txt ]; then
                ERRORS=$(grep -c "ERROR" reports/checkstyle-report.txt || echo "0")
                WARNINGS=$(grep -c "WARNING" reports/checkstyle-report.txt || echo "0")
                echo "| Checkstyle Errors | $ERRORS |" >> $GITHUB_STEP_SUMMARY
                echo "| Checkstyle Warnings | $WARNINGS |" >> $GITHUB_STEP_SUMMARY
              fi
              ;;
          esac
        shell: bash

  codeql-analysis:
    name: 🔬 CodeQL Analysis
    runs-on: ubuntu-latest
    permissions:
      actions: read
      contents: read
      security-events: write
    needs: code-quality
      
    strategy:
      fail-fast: false
      matrix:
        language: ['javascript', 'python', 'java', 'go', 'ruby', 'cpp']
        
    steps:
      - name: ⬇️ Checkout repository
        uses: actions/checkout@v3
        
      - name: 🔍 Check for language files
        id: check_files
        run: |
          case "${{ matrix.language }}" in
            javascript)
              EXTENSIONS=("js" "jsx" "ts" "tsx")
              ;;
            python)
              EXTENSIONS=("py")
              ;;
            java)
              EXTENSIONS=("java")
              ;;
            go)
              EXTENSIONS=("go")
              ;;
            ruby)
              EXTENSIONS=("rb")
              ;;
            cpp)
              EXTENSIONS=("cpp" "cc" "cxx" "c" "h" "hpp")
              ;;
            *)
              echo "Unknown language: ${{ matrix.language }}"
              exit 1
              ;;
          esac
          
          FILES_FOUND=false
          for EXT in "${EXTENSIONS[@]}"; do
            if compgen -G "**/*.$EXT" > /dev/null 2>&1; then
              FILES_FOUND=true
              break
            fi
          done
          
          echo "FILES_FOUND=$FILES_FOUND" >> $GITHUB_OUTPUT
        shell: bash
      
      - name: 🛠️ Initialize CodeQL
        if: steps.check_files.outputs.FILES_FOUND == 'true'
        uses: github/codeql-action/init@v2
        with:
          languages: ${{ matrix.language }}
          queries: +security-and-quality
          
      - name: 🔨 Autobuild
        if: steps.check_files.outputs.FILES_FOUND == 'true'
        uses: github/codeql-action/autobuild@v2
        
      - name: 🔎 Perform CodeQL Analysis
        if: steps.check_files.outputs.FILES_FOUND == 'true'
        uses: github/codeql-action/analyze@v2
        with:
          category: "/language:${{ matrix.language }}"
'''

# Write the code quality workflow
with open(os.path.join(workflows_dir, 'code-quality.yml'), 'w') as f:
    f.write(code_quality_workflow)
    
    
