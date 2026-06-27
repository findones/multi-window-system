# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-06-27

### Added

- **4-Role Window System**: Architect, Engineer, Paper, Repro windows for organized multi-role project management
- **Automated Initialization**: Python script (`init.py`) for quick project setup in 5 minutes
- **Complete Templates**: 9 pre-designed markdown templates for all project types
  - STATUS.md: Cross-window status board
  - method.md: Architecture specification
  - CODE_MAP.md: Code interface guide
  - RESULTS.md: Experiment results tracking
  - WORK_PLAN.md: Work changelog
  - docs/roles/architect.md: Design decisions window
  - docs/roles/engineer.md: Implementation logs window
  - docs/roles/paper.md: Writing & narrative window
  - docs/roles/repro.md: Research & references window
- **Bilingual Support**: Complete English and Chinese documentation
- **Skill Definition**: skill.yaml for Claude Code integration
- **Claude Code Skill**: Ready to be registered as a skill for Claude Code
- **.gitignore**: Properly configured to exclude internal documentation

### Features

- ✅ Zero personal data - fully generic and reusable templates
- ✅ Central synchronization point (STATUS.md) for all cross-window communication
- ✅ Handoff message system for clear task assignment and decision logging
- ✅ Modular role documentation with independent workspace tracking
- ✅ Flexible customization for different team sizes and project types
- ✅ No external dependencies - uses only markdown and Python standard library

### Documentation

- README.md: Complete system overview (English + Chinese)
- README_CN.md: Chinese version with detailed examples
- INSTALL.md: Step-by-step installation guide (bilingual)
- HOW_TO_INSTALL_SKILL.md: Integration guide for Claude Code

### Metadata

- License: MIT
- Author: findones
- Category: Project Management
- Tags: ai-assisted, multi-window, organization, collaboration

## Future Roadmap

### [1.1.0] (Planned)

- [ ] GitHub Actions integration for automatic STATUS.md synchronization
- [ ] Web dashboard for STATUS.md visualization
- [ ] More language translations (Spanish, Japanese, German)
- [ ] Domain-specific templates (Software Engineering, Writing, Product Development)
- [ ] CLI tool for advanced operations

### [1.2.0] (Planned)

- [ ] Slack integration for Handoff message notifications
- [ ] Visual project timeline generation
- [ ] Team collaboration features
- [ ] Export to PDF/HTML

## Known Limitations

- Currently optimized for single-file synchronization (STATUS.md)
- Best used with Claude Code or similar AI-assisted development tools
- Manual file management required (no automatic sync)

## Contributing

Contributions are welcome! Please feel free to:
- Report bugs or suggest improvements via GitHub Issues
- Share your adaptations and use cases
- Contribute translations
- Propose new features

## Support

For installation help, see [INSTALL.md](INSTALL.md)
For usage questions, see [README.md](README.md)
For bug reports and feature requests, open a [GitHub Issue](https://github.com/findones/multi-window-system/issues)
