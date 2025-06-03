**User:**

<task>
Write a good rules.md for Roocode and put it into the .roo folder.
</task>
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs


# Current Time
1.6.2025, 11:09:43 PM (Europe/Berlin, UTC+2:00)

# Current Context Size (Tokens)
(Not available)

# Current Cost
$0.00

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
<model>anthropic/claude-sonnet-4-20250514</model>


# Current Workspace Directory (/Users/the/Developer/thetom42/github/perplexica-mcp) Files
.gitignore
.sample.env
CHANGELOG.md
CLAUDE.md
LICENSE
perplexica_mcp_tool.py
pyproject.toml
README.md
</environment_details>

---

**Assistant:**

<thinking>
I need to write a good rules.md file for Roocode and put it into the .roo folder. Let me first understand what this project is about by looking at the current files and structure.

From the environment details, I can see this is a perplexica-mcp project with Python files. I should first check if the .roo folder exists, and if not, create it. Then I need to write a comprehensive rules.md file that would be appropriate for a Roocode project.

Let me start by checking if the .roo folder exists and understanding the project structure better.
</thinking>

I'll help you create a comprehensive rules.md file for Roocode in the .roo folder. Let me first check the current project structure and then create the appropriate rules file.

<list_files>
<path>.</path>
<recursive>true</recursive>
</list_files>

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of the message.]

---

**User:**

[list_files for '.'] Result:
.gitignore
.sample.env
CHANGELOG.md
CLAUDE.md
LICENSE
perplexica_mcp_tool.py
pyproject.toml
README.md
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs


# Current Time
1.6.2025, 11:09:49 PM (Europe/Berlin, UTC+2:00)

# Current Context Size (Tokens)
43.406 (22%)

# Current Cost
$0.08

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
<model>anthropic/claude-sonnet-4-20250514</model>
</environment_details>

---

**Assistant:**

Now let me check if the .roo folder exists and read some key files to understand the project better:

<read_file>
<args>
  <file>
    <path>README.md</path>
  </file>
</args>
</read_file>

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of the message.]

---

**User:**

[read_file for 'README.md'. Reading multiple files at once is more efficient for the LLM. If other files are relevant to your current task, please read them simultaneously.] Result:
<files>
<file><path>README.md</path>
<content lines="1-101">
  1 | # Perplexica MCP Server
  2 | 
  3 | Perplexica MCP Server is a Model Context Protocol (MCP) server that acts as a proxy to provide LLM access to Perplexica's AI-powered search engine. This server enables AI assistants and other MCP clients to perform searches through the Perplexica API.
  4 | 
  5 | ## What This MCP Server Provides
  6 | 
  7 | - **Single Search Tool**: Exposes Perplexica's search functionality as an MCP tool
  8 | - **API Proxy**: Acts as a bridge between MCP clients and the Perplexica search endpoint
  9 | - **Parameter Passthrough**: Forwards all search parameters (focus modes, models, etc.) to the Perplexica API
 10 | - **MCP Protocol Compliance**: Implements the Model Context Protocol for seamless integration with AI assistants
 11 | 
 12 | ## Installation
 13 | 
 14 | To use the Perplexica MCP Server, you'll need to have Python 3.12 or later installed on your system.
 15 | 
 16 | 1. Clone this repository:
 17 | 
 18 |   ```bash
 19 |   git clone https://github.com/yourusername/perplexica-mcp.git
 20 |   cd perplexica-mcp
 21 |   ```
 22 | 
 23 | 2. Install the required dependencies:
 24 | 
 25 |   ```bash
 26 |   pip install -e .
 27 |   ```
 28 | 
 29 | ## MCP Server Configuration
 30 | 
 31 | This server is designed to be used with MCP-compatible clients. Add the following configuration to your MCP client:
 32 | 
 33 | ```json
 34 | {
 35 |   "mcpServers": {
 36 |     "perplexica": {
 37 |       "command": "uv",
 38 |       "args": ["run", "/path/to/perplexica-mcp/perplexica_mcp_tool.py"],
 39 |       "env": {
 40 |         "PERPLEXICA_BACKEND_URL": "http://localhost:3000/api/search"
 41 |       }
 42 |     }
 43 |   }
 44 | }
 45 | ```
 46 | 
 47 | ## Backend URL Configuration
 48 | 
 49 | The Perplexica MCP Server uses an environment variable to configure the backend URL. To set this up:
 50 | 
 51 | 1. Create a `.env` file in the root of the project (if it doesn't already exist)
 52 | 2. Add the `PERPLEXICA_BACKEND_URL` variable with your desired backend URL:
 53 | 
 54 | ```ini
 55 | PERPLEXICA_BACKEND_URL=http://localhost:3000/api/search
 56 | ```
 57 | 
 58 | The server will use this URL to communicate with the Perplexica backend. If the environment variable is not set, it will default to `http://localhost:3000/api/search`.
 59 | 
 60 | ## Usage
 61 | 
 62 | This MCP server provides a `search` tool that can be used by MCP clients to perform searches through Perplexica. The tool accepts the following parameters:
 63 | 
 64 | ### Search Tool Parameters
 65 | 
 66 | - `query` (required): The search query string
 67 | - `focus_mode` (required): The search focus mode
 68 | - `chat_model` (optional): Chat model configuration
 69 | - `embedding_model` (optional): Embedding model configuration
 70 | - `optimization_mode` (optional): Performance optimization setting
 71 | - `history` (optional): Conversation history
 72 | - `system_instructions` (optional): Custom AI guidance
 73 | - `stream` (optional): Whether to stream responses
 74 | 
 75 | ### Example Usage via MCP Client
 76 | 
 77 | When connected to an MCP client, you can use the search tool like this:
 78 | 
 79 | ```none
 80 | Search for "Python programming best practices" using webSearch focus mode
 81 | ```
 82 | 
 83 | The MCP client will automatically invoke the search tool with the appropriate parameters.
 84 | 
 85 | ## Perplexica Integration
 86 | 
 87 | This MCP server acts as a proxy to the Perplexica search API. All search parameters and configurations are passed through to the underlying Perplexica service:
 88 | 
 89 | - **Focus Modes**: Supports all Perplexica focus modes (webSearch, academicSearch, writingAssistant, wolframAlphaSearch, youtubeSearch, redditSearch)
 90 | - **Model Configuration**: Passes through chat model and embedding model settings to Perplexica
 91 | - **Search Options**: Forwards optimization modes, conversation history, and system instructions
 92 | 
 93 | For detailed information about Perplexica's capabilities and features, please refer to the [Perplexica documentation](https://github.com/ItzCrazyKns/Perplexica).
 94 | 
 95 | ## Contributing
 96 | 
 97 | Contributions are welcome! Please open an issue or submit a pull request.
 98 | 
 99 | ## License
100 | 
101 | This project is licensed under the MIT License. See the LICENSE file for details.
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs


# Current Time
1.6.2025, 11:09:52 PM (Europe/Berlin, UTC+2:00)

# Current Context Size (Tokens)
44.097 (22%)

# Current Cost
$0.09

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
<model>anthropic/claude-sonnet-4-20250514</model>
</environment_details>

---

**Assistant:**

Now let me check the pyproject.toml to understand more about the project structure:

<read_file>
<args>
  <file>
    <path>pyproject.toml</path>
  </file>
</args>
</read_file>

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of the message.]

---

**User:**

[read_file for 'pyproject.toml'. Reading multiple files at once is more efficient for the LLM. If other files are relevant to your current task, please read them simultaneously.] Result:
<files>
<file><path>pyproject.toml</path>
<content lines="1-7">
1 | [project]
2 | name = "perplexica-mcp"
3 | version = "0.1.0"
4 | requires-python = ">=3.12"
5 | dependencies = ["mcp[cli]", "requests", "python-dotenv"]
6 | 
7 | [tool.uv]
</content>
</file>
</files>
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs


# Current Time
1.6.2025, 11:09:55 PM (Europe/Berlin, UTC+2:00)

# Current Context Size (Tokens)
47.511 (24%)

# Current Cost
$0.11

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
<model>anthropic/claude-sonnet-4-20250514</model>
</environment_details>

---

**Assistant:**

Now let me check if the .roo folder exists and create the rules.md file. First, let me check for the .roo folder:

<list_files>
<path>.roo</path>
<recursive>false</recursive>
</list_files>

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of the message.]

---

**User:**

[list_files for '.roo'] Result:
No files found.
<environment_details>
# VSCode Visible Files


# VSCode Open Tabs


# Current Time
1.6.2025, 11:10:00 PM (Europe/Berlin, UTC+2:00)

# Current Context Size (Tokens)
47.511 (24%)

# Current Cost
$0.11

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
<model>anthropic/claude-sonnet-4-20250514</model>
</environment_details>

---

**Assistant:**

The .roo folder doesn't exist yet, so I'll create it along with a comprehensive rules.md file. Based on the project structure, this is a Perplexica MCP Server project, so I'll create rules that are appropriate for this type of codebase.

<write_to_file>
<path>.roo/rules.md</path>
<content>
# Roocode Rules for Perplexica MCP Server

## Project Overview
This is a Model Context Protocol (MCP) server that provides AI assistants with access to Perplexica's AI-powered search engine. The server acts as a proxy between MCP clients and the Perplexica API.

## Code Organization Rules

### File Structure
- **Root level**: Configuration files, documentation, and main entry point
- **`.roo/`**: Roocode-specific configuration and rules
- **Main module**: [`perplexica_mcp_tool.py`](perplexica_mcp_tool.py:1) - Core MCP server implementation

### Naming Conventions
- **Files**: Use snake_case for Python files (e.g., `perplexica_mcp_tool.py`)
- **Variables**: Use snake_case for variables and functions
- **Constants**: Use UPPER_SNAKE_CASE for constants
- **Classes**: Use PascalCase for class names

## Development Guidelines

### Python Standards
- **Version**: Minimum Python 3.12 as specified in [`pyproject.toml`](pyproject.toml:4)
- **Dependencies**: Keep dependencies minimal and well-documented
- **Type Hints**: Use type hints for all function parameters and return values
- **Docstrings**: Use Google-style docstrings for all public functions and classes

### MCP Protocol Compliance
- Follow MCP specification for tool definitions and responses
- Ensure proper error handling for API communication
- Maintain backward compatibility with MCP protocol versions

### API Integration
- **Environment Variables**: Use [`PERPLEXICA_BACKEND_URL`](README.md:40) for backend configuration
- **Error Handling**: Implement robust error handling for network requests
- **Timeouts**: Set appropriate timeouts for API calls
- **Logging**: Use structured logging for debugging and monitoring

## Code Quality Standards

### Testing
- Write unit tests for all core functionality
- Test MCP tool registration and execution
- Mock external API calls in tests
- Maintain test coverage above 80%

### Documentation
- Keep [`README.md`](README.md:1) up-to-date with installation and usage instructions
- Document all configuration options
- Provide clear examples for MCP client integration
- Update [`CHANGELOG.md`](CHANGELOG.md:1) for all releases

### Security
- Validate all input parameters
- Sanitize search queries before forwarding to Perplexica
- Use environment variables for sensitive configuration
- Never log sensitive data or API keys

## Git Workflow

### Commit Messages
- Use conventional commit format: `type(scope): description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Keep first line under 50 characters
- Include detailed description for complex changes

### Branch Strategy
- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: New features and enhancements
- `fix/*`: Bug fixes
- `docs/*`: Documentation updates

### Pull Requests
- Require code review before merging
- Run all tests and linting checks
- Update documentation if needed
- Squash commits when merging

## Performance Guidelines

### Response Times
- Keep search tool response time under 30 seconds
- Implement proper timeout handling
- Cache frequently used configurations

### Resource Usage
- Minimize memory footprint
- Use async/await for I/O operations where beneficial
- Clean up resources properly

## Configuration Management

### Environment Variables
- Use [`.env`](README.md:51) files for local development
- Document all environment variables in [`README.md`](README.md:47)
- Provide sensible defaults where possible
- Validate required environment variables on startup

### MCP Client Configuration
- Provide clear examples in [`README.md`](README.md:33)
- Support multiple deployment scenarios
- Document all configuration options

## Error Handling

### API Errors
- Return meaningful error messages to MCP clients
- Log errors with appropriate severity levels
- Implement retry logic for transient failures
- Gracefully handle Perplexica backend unavailability

### Input Validation
- Validate all tool parameters
- Provide clear error messages for invalid inputs
- Handle edge cases gracefully

## Maintenance

### Dependencies
- Keep dependencies up-to-date
- Monitor for security vulnerabilities
- Document dependency upgrade procedures
- Test thoroughly after dependency updates

### Monitoring
- Log important events and errors
- Monitor API response times
- Track usage patterns
- Set up alerts for critical failures

## Release Process

### Versioning
- Follow semantic versioning (SemVer)
- Update version in [`pyproject.toml`](pyproject.toml:3)
- Tag releases in Git
- Update [`CHANGELOG.md`](CHANGELOG.md:1) with release notes

### Deployment
- Test in staging environment first
- Verify MCP client compatibility
- Update documentation if needed
- Communicate breaking changes clearly

## Best Practices

### Code Style
- Follow PEP 8 style guidelines
- Use black for code formatting
- Use flake8 for linting
- Sort imports with isort

### Architecture
- Keep the MCP server lightweight and focused
- Separate concerns clearly
- Use dependency injection where appropriate
- Design for testability

### Documentation
- Write self-documenting code
- Keep comments concise and relevant
- Update documentation with code changes
- Provide usage examples

## Tools and Utilities

### Development Tools
- Use `uv` for dependency management
- Configure pre-commit hooks
- Set up IDE/editor with Python support
- Use debugger for complex issues

### MCP Testing
- Test with multiple MCP clients
- Verify tool registration works correctly
- Test parameter validation
- Ensure proper error responses

## Collaboration

### Code Reviews
- Review for functionality, style, and security
- Check test coverage and documentation
- Verify MCP protocol compliance
- Test integration scenarios

### Communication
- Use clear and descriptive commit messages
- Document design decisions
- Share knowledge through code comments
- Maintain project documentation
</content>
<line_count>154</line_count>
</write_to_file>

[Response interrupted by a tool use result. Only one tool may be used at a time and should be placed at the end of the message.]

---

**User:**

[write_to_file for '.roo/rules.md'] Result:
The content was successfully saved to .roo/rules.md.
<environment_details>
# VSCode Visible Files
.roo/rules.md

# VSCode Open Tabs
.roo/rules.md

# Current Time
1.6.2025, 11:10:44 PM (Europe/Berlin, UTC+2:00)

# Current Context Size (Tokens)
49.648 (25%)

# Current Cost
$0.14

# Current Mode
<slug>code</slug>
<name>💻 Code</name>
<model>anthropic/claude-sonnet-4-20250514</model>
</environment_details>

---

**Assistant:**

<attempt_completion>
<result>
I've successfully created a comprehensive rules.md file for Roocode in the .roo folder. The rules file includes:

**Project-Specific Guidelines:**
- MCP protocol compliance standards
- Perplexica API integration best practices
- Python 3.12+ development standards

**Code Organization:**
- File structure and naming conventions
- Module organization principles
- Configuration management

**Development Standards:**
- Code quality requirements (testing, documentation, security)
- Git workflow and commit conventions
- Performance guidelines and resource management

**Operational Guidelines:**
- Error handling and input validation
- Monitoring and maintenance procedures
- Release process and versioning

**Best Practices:**
- Code style and architecture principles
- Development tools and MCP testing
- Collaboration and code review standards

The rules are tailored specifically for this Perplexica MCP Server project, referencing actual files like [`perplexica_mcp_tool.py`](perplexica_mcp_tool.py:1), [`pyproject.toml`](pyproject.toml:4), and [`README.md`](README.md:1) to provide contextual guidance for maintaining and developing this codebase.
</result>
</attempt_completion>

