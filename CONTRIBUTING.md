# Contributing to Tube Downloader Pro

First off, thank you for considering contributing to Tube Downloader Pro! It's people like you that make this tool better for everyone.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Pull Request Process](#pull-request-process)
- [Style Guidelines](#style-guidelines)

## 📜 Code of Conduct

This project and everyone participating in it is governed by our commitment to providing a welcoming and inspiring community for all. Please be respectful and constructive in your communications.

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs actual behavior
- **Screenshots** if applicable
- **Environment details** (OS, Python version, etc.)

### Suggesting Features

Feature suggestions are welcome! Please provide:

- **Clear description** of the feature
- **Use case** - why is this feature needed?
- **Possible implementation** approach (optional)

### Pull Requests

1. Fork the repo and create your branch from `main`
2. Make your changes
3. Test thoroughly
4. Update documentation if needed
5. Submit a pull request

## 🛠️ Development Setup

1. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/tube-downloader-pro.git
   cd tube-downloader-pro
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 🔄 Pull Request Process

1. **Update the README.md** with details of changes if applicable
2. **Follow the code style** guidelines below
3. **Test your changes** thoroughly
4. **Write clear commit messages**
   - Use present tense ("Add feature" not "Added feature")
   - Be descriptive but concise
5. **Reference issues** in your PR description

## 📝 Style Guidelines

### Python Code Style

- Follow [PEP 8](https://pep8.org/) guidelines
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and concise

Example:
```python
def download_video(url, format_id, output_path):
    """
    Download a video from the given URL.
    
    Args:
        url (str): The video URL
        format_id (str): The format identifier
        output_path (str): Where to save the file
        
    Returns:
        bool: True if successful, False otherwise
    """
    # Implementation here
    pass
```

### HTML/CSS/JavaScript

- Use consistent indentation (2 spaces for HTML/CSS/JS)
- Keep CSS organized by component
- Use meaningful class and ID names
- Comment complex UI logic

### Git Commit Messages

Good commit message format:
```
Add support for playlist downloads

- Implement playlist parsing
- Add queue management
- Update UI to show multiple items
- Add tests for playlist functionality

Fixes #123
```

## 🧪 Testing

Before submitting a PR, please test:

- [ ] Application launches without errors
- [ ] Video download works with multiple formats
- [ ] Audio download works correctly
- [ ] Progress tracking updates properly
- [ ] UI is responsive and looks correct
- [ ] No console errors or warnings

## 📌 Priority Areas

We're especially interested in contributions for:

- Playlist download support
- Download queue management
- Additional platform support
- Performance improvements
- UI/UX enhancements
- Better error handling
- Comprehensive testing

## ❓ Questions?

Feel free to:
- Open an issue for discussion
- Reach out to maintainers
- Check existing issues and PRs for context

## 🎉 Recognition

Contributors will be acknowledged in the README and release notes. Thank you for making Tube Downloader Pro better!

---

Happy Contributing! 🚀
