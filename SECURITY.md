# Security Policy

## Reporting a Vulnerability

If you discover a security vulnerability in this project, please **do not** open a public GitHub Issue.

Instead, please email your findings to:
- Contact via GitHub profile

Please include:
1. Description of the vulnerability
2. Affected versions
3. Steps to reproduce (if applicable)
4. Suggested fix (if you have one)

We take security seriously and will respond within 48 hours.

## Security Considerations

### What This Project Does

- Creates local markdown files for project management
- Provides templates for organizing work with Claude Code
- Manages no sensitive data by design
- All data stays in your local files

### What This Project Does NOT Do

- ❌ Send data to external servers
- ❌ Store authentication tokens
- ❌ Collect user information
- ❌ Execute arbitrary code

### Best Practices for Users

1. **Keep your local files secure**
   - Don't commit sensitive data to your repositories
   - Use .gitignore for confidential information

2. **Manage your STATUS.md carefully**
   - It contains your project decisions and roadmap
   - Keep it in private repositories if sensitive

3. **Use safely with Claude Code**
   - This system is designed for use with Claude
   - Ensure your Claude Code environment is secure
   - Don't share private project files unintentionally

4. **Token and credential management**
   - Never commit tokens or API keys to git
   - Use environment variables for sensitive data
   - Use .gitignore and .git/info/exclude for protection

## Supported Versions

| Version | Status | Support |
|---------|--------|---------|
| 1.0.0 | Current | ✅ Fully Supported |

## Changelog

For security-related fixes and updates, see [CHANGELOG.md](CHANGELOG.md)

---

**Last updated**: 2025-06-27
