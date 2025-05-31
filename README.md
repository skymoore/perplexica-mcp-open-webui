# Perplexica MCP Server

Perplexica MCP Server is a Model Context Protocol (MCP) server that acts as a proxy to provide LLM access to Perplexica's AI-powered search engine. This server enables AI assistants and other MCP clients to perform searches through the Perplexica API.

## What This MCP Server Provides

- **Single Search Tool**: Exposes Perplexica's search functionality as an MCP tool
- **API Proxy**: Acts as a bridge between MCP clients and the Perplexica search endpoint
- **Parameter Passthrough**: Forwards all search parameters (focus modes, models, etc.) to the Perplexica API
- **MCP Protocol Compliance**: Implements the Model Context Protocol for seamless integration with AI assistants

## Installation

To use the Perplexica MCP Server, you'll need to have Python 3.12 or later installed on your system.

1. Clone this repository:

  ```bash
  git clone https://github.com/yourusername/perplexica-mcp.git
  cd perplexica-mcp
  ```

2. Install the required dependencies:

  ```bash
  pip install -e .
  ```

## MCP Server Configuration

This server is designed to be used with MCP-compatible clients. Add the following configuration to your MCP client:

```json
{
  "mcpServers": {
    "perplexica": {
      "command": "uv",
      "args": ["run", "/path/to/perplexica-mcp/perplexica_mcp_tool.py"],
      "env": {
        "PERPLEXICA_BACKEND_URL": "http://localhost:3000/api/search"
      }
    }
  }
}
```

## Backend URL Configuration

The Perplexica MCP Server uses an environment variable to configure the backend URL. To set this up:

1. Create a `.env` file in the root of the project (if it doesn't already exist)
2. Add the `PERPLEXICA_BACKEND_URL` variable with your desired backend URL:

```ini
PERPLEXICA_BACKEND_URL=http://localhost:3000/api/search
```

The server will use this URL to communicate with the Perplexica backend. If the environment variable is not set, it will default to `http://localhost:3000/api/search`.

## Usage

This MCP server provides a `search` tool that can be used by MCP clients to perform searches through Perplexica. The tool accepts the following parameters:

### Search Tool Parameters

- `query` (required): The search query string
- `focus_mode` (required): The search focus mode
- `chat_model` (optional): Chat model configuration
- `embedding_model` (optional): Embedding model configuration
- `optimization_mode` (optional): Performance optimization setting
- `history` (optional): Conversation history
- `system_instructions` (optional): Custom AI guidance
- `stream` (optional): Whether to stream responses

### Example Usage via MCP Client

When connected to an MCP client, you can use the search tool like this:

```none
Search for "Python programming best practices" using webSearch focus mode
```

The MCP client will automatically invoke the search tool with the appropriate parameters.

## Perplexica Integration

This MCP server acts as a proxy to the Perplexica search API. All search parameters and configurations are passed through to the underlying Perplexica service:

- **Focus Modes**: Supports all Perplexica focus modes (webSearch, academicSearch, writingAssistant, wolframAlphaSearch, youtubeSearch, redditSearch)
- **Model Configuration**: Passes through chat model and embedding model settings to Perplexica
- **Search Options**: Forwards optimization modes, conversation history, and system instructions

For detailed information about Perplexica's capabilities and features, please refer to the [Perplexica documentation](https://github.com/ItzCrazyKns/Perplexica).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
