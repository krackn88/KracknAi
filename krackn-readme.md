# Krackn AI Assistant

![Krackn Logo](docs/images/krackn_logo.png)

**Krackn** is an all-in-one AI-powered development assistant that integrates multiple AI services, including Anthropic Claude, OpenAI, Mistral AI, and more, into a powerful pair programming environment. It features FreeLoder technology that chains free tier services to deliver premium-quality results without the premium price tag.

## Key Features

- **Multi-Service AI Integration**: Connect to multiple AI services including Anthropic Claude, OpenAI, Mistral AI, HuggingFace, GitHub Copilot, and CLINE
- **FreeLoder Mode**: Chain free tier services to get high-quality results without paying for premium tiers
- **Advanced Code Editor**: Built-in editor with syntax highlighting, code completion, and more
- **Pair Programming**: AI-assisted pair programming with code completion, explanation, and refactoring
- **Auto-Update System**: Stay up-to-date with the latest AI models and techniques
- **Git/GitHub Integration**: Seamless integration with Git and GitHub repositories
- **Local Model Support**: Run AI models locally for better privacy and offline use
- **Hybrid Architecture**: Rust/Go backend for high performance, Python frontend for easy extensibility

## Installation

### Prerequisites

- Python 3.8 or higher
- Rust 1.60.0 or higher
- Go 1.18 or higher
- Git

### Quick Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/krackn.git
cd krackn

# Run the installer
python scripts/install.py
```

The installer will guide you through the process of setting up Krackn AI Assistant.

### Manual Installation

1. Install the required dependencies:

```bash
# Install Python dependencies
pip install -r requirements.txt

# Build Rust components
cd rust
cargo build --release
cd ..

# Build Go components
cd go
go build -o bin/krackn_service cmd/krackn_service/main.go
cd ..
```

2. Configure API keys:

Create a `config/settings.json` file with your API keys:

```json
{
  "ai_services": {
    "anthropic": {
      "enabled": true,
      "api_key": "YOUR_ANTHROPIC_API_KEY"
    },
    "openai": {
      "enabled": true,
      "api_key": "YOUR_OPENAI_API_KEY"
    },
    "mistral": {
      "enabled": true,
      "api_key": "YOUR_MISTRAL_API_KEY"
    },
    "freeloder": {
      "enabled": true,
      "services": ["anthropic_free", "openai_free", "mistral_free"],
      "rotation_strategy": "sequential"
    }
  }
}
```

## Usage

### Starting Krackn

```bash
# Start Krackn
krackn
```

### Command-Line Options

```bash
# Show help
krackn --help

# Run in command-line mode
krackn --no-gui

# Check for updates
krackn --update

# Enable verbose output
krackn --verbose
```

### GUI Interface

The Krackn AI Assistant GUI provides the following features:

- **Code Editor**: Write and edit code with syntax highlighting and AI-powered code completion
- **AI Chat**: Chat with AI services for code explanations, refactoring, and more
- **Terminal**: Run commands and interact with the system
- **Project Explorer**: Browse and manage your project files
- **FreeLoder Settings**: Configure the FreeLoder mode for maximum efficiency

### FreeLoder Mode

FreeLoder mode allows you to chain free tier services from different AI providers to get high-quality results without paying for premium tiers. Here's how it works:

1. **Service Rotation**: FreeLoder rotates between free tier services to avoid hitting rate limits
2. **Capability-Based Routing**: Tasks are routed to the most capable service for the job
3. **Result Caching**: Results are cached to avoid unnecessary API calls

To configure FreeLoder mode, go to `AI > FreeLoder Settings` in the menu.

## Architecture

Krackn AI Assistant is built with a hybrid architecture:

- **Python Frontend**: PyQt6-based GUI and high-level logic
- **Rust Core**: High-performance core functionality
- **Go Service**: API endpoints and background tasks

This architecture provides the best of all worlds: Python's ease of use, Rust's performance, and Go's concurrency.

## AI Service Integration

Krackn AI Assistant integrates with the following AI services:

- **Anthropic Claude**: High-quality code completion and explanation
- **OpenAI GPT**: Versatile AI capabilities
- **Mistral AI**: Open-source AI models
- **HuggingFace**: Access to thousands of models
- **GitHub Copilot**: Code completion and suggestion
- **CLINE**: Command-line AI tools

## Development

### Project Structure

```
krackn/
├── krackn/                      # Main Python package
│   ├── app.py                   # Application core
│   ├── ui/                      # PyQt6 GUI components
│   ├── core/                    # Core functionality
│   ├── ai/                      # AI services integration
│   └── utils/                   # Utility functions
├── rust/                        # Rust components
│   ├── krackn_core/             # Core Rust library
│   └── krackn_plugins/          # Rust plugins
├── go/                          # Go components
│   ├── cmd/krackn_service/      # Go service entry point
│   └── internal/                # Internal Go packages
├── scripts/                     # Installation and utility scripts
└── docs/                        # Documentation
```

### Building from Source

To build Krackn AI Assistant from source:

```bash
# Clone the repository
git clone https://github.com/yourusername/krackn.git
cd krackn

# Build Rust components
python scripts/build_rust.py

# Build Go components
python scripts/build_go.py

# Build Python package
python setup.py install
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch with your feature or bug fix
3. Write tests for your changes
4. Ensure all tests pass
5. Create a pull request

Please follow the [code of conduct](CODE_OF_CONDUCT.md) and [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Krackn AI Assistant is built upon many open-source projects, including:

- [PyQt](https://riverbankcomputing.com/software/pyqt/)
- [Rust](https://www.rust-lang.org/)
- [Go](https://golang.org/)
- [Anthropic Claude](https://www.anthropic.com/)
- [OpenAI GPT](https://openai.com/)
- [Mistral AI](https://mistral.ai/)
- [HuggingFace](https://huggingface.co/)
- [CLINE](https://github.com/cline-ai/cline)

## Contact

For questions or support, please open an issue on GitHub or contact the maintainers at [email@example.com](mailto:email@example.com).
