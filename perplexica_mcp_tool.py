#!/usr/bin/env python3

import requests
from mcp.server.fastmcp import FastMCP
from pydantic import Field
from typing import Annotated

# Create an MCP server
mcp = FastMCP("Perplexica", dependencies=["requests", "mcp", "pydantic"])


# Add the search tool
@mcp.tool(
    name="search",
    description="Search using Perplexica's AI-powered search engine"
)
def search(
    query: Annotated[str, Field(description="Search query string")],
    focus_mode: Annotated[str, Field(description="Focus mode, must be one of: 'webSearch', 'academicSearch', 'writingAssistant', 'wolframAlphaSearch', 'youtubeSearch', 'redditSearch'")],
    chat_model: Annotated[str, Field(description="Chat model configuration with provider (e.g., openai, ollama), name (e.g., gpt-4o-mini), and optional customOpenAIBaseURL and customOpenAIKey", default=None)],
    embedding_model: Annotated[str, Field(description="Embedding model configuration with provider (e.g., openai) and name (e.g., text-embedding-3-large)", default=None)],
    optimization_mode: Annotated[str, Field(description="Optimization mode: 'speed' (prioritize speed) or 'balanced' (balance speed and quality)", default=None)],
    history: Annotated[list[tuple[str, str]], Field(description="Conversation history as list of [role, message] pairs where role is 'human' or 'assistant'", default=None)],
    system_instructions: Annotated[str, Field(description="Custom instructions to guide the AI's response style, format, or focus area", default=None)],
    stream: Annotated[bool, Field(description="Whether to stream responses (default: False)", default=False)]
) -> dict:
    """
    Search using Perplexica's AI-powered search engine

    Args:
        query: The search query or question
        focus_mode: Focus mode, must be one of: 'webSearch', 'academicSearch', 'writingAssistant', 'wolframAlphaSearch', 'youtubeSearch', 'redditSearch'
        chat_model: Chat model configuration with provider (e.g., openai, ollama), name (e.g., gpt-4o-mini), and optional customOpenAIBaseURL and customOpenAIKey
        embedding_model: Embedding model configuration with provider (e.g., openai) and name (e.g., text-embedding-3-large)
        optimization_mode: Optimization mode: 'speed' (prioritize speed) or 'balanced' (balance speed and quality)
        history: Conversation history as list of [role, message] pairs where role is 'human' or 'assistant'
        system_instructions: Custom instructions to guide the AI's response style, format, or focus area
        stream: Whether to stream responses (default: False)

    Returns:
        dict: The search results
    """
    return perplexica_search(
        query=query,
        focus_mode=focus_mode,
        chat_model=chat_model,
        embedding_model=embedding_model,
        optimization_mode=optimization_mode,
        history=history,
        system_instructions=system_instructions,
        stream=stream
    )


def perplexica_search(
    query, focus_mode,
    chat_model=None,
    embedding_model=None,
    optimization_mode=None,
    history=None,
    system_instructions=None,
    stream=False
) -> dict:
    """
    Search using the Perplexica API

    Args:
        query (str): The search query
        chat_model (dict, optional): Chat model configuration with:
            provider: Provider name (e.g., openai, ollama)
            name: Model name (e.g., gpt-4o-mini)
            customOpenAIBaseURL: Optional custom OpenAI base URL
            customOpenAIKey: Optional custom OpenAI API key
        embedding_model (dict, optional): Embedding model configuration with:
            provider: Provider name (e.g., openai)
            name: Model name (e.g., text-embedding-3-large)
        optimization_mode (str, optional): Optimization mode ('speed' or 'balanced')
        focus_mode (str, required): Focus mode, must be one of:
            'webSearch', 'academicSearch', 'writingAssistant',
            'wolframAlphaSearch', 'youtubeSearch', 'redditSearch'
        history (list, optional): Conversation history as list of [role, message] pairs
        system_instructions (str, optional): Custom instructions for AI response
        stream (bool, optional): Whether to stream responses (default: False)

    Returns:
        dict: The search results
    """
    url = 'http://localhost:3000/api/search'
    payload = {
        'query': query,
        'focusMode': focus_mode
    }

    if chat_model:
        payload['chatModel'] = chat_model
    if embedding_model:
        payload['embeddingModel'] = embedding_model
    if optimization_mode:
        payload['optimizationMode'] = optimization_mode
    if history:
        payload['history'] = history
    if system_instructions:
        payload['systemInstructions'] = system_instructions
    if stream:
        payload['stream'] = stream

    response = requests.post(url, json=payload)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()