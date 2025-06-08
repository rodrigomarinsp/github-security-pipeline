# 📝 Changelog

## Author: Author: Rodrigo Marins Piaba (Fanaticos4tech)

## E-Mail: rodrigomarinsp@gmail.com / fanaticos4tech@gmail.com

## GitHub: github.com/rodrigomarinsp/github-security-pipeline

## Website: http://github.com/rodrigomarinsp/github-security-pipeline/index.html

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
