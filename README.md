# CLI Gemini AI Chat Assistant

A simple command-line tool that sends a prompt to an AI model and prints the response.  
Supports optional verbose output for debugging and inspecting token usage.

## Features

- Send a single prompt from the command line
- Streams the AI’s response to stdout
- Optional `--verbose` mode to show:
  - The original user prompt
  - Number of prompt tokens
  - Number of response tokens

## Installation

This project uses [`uv`](https://docs.astral.sh/uv/) for Python environment and dependency management.

Clone the repository and install dependencies:

```sh
git clone <your-repo-url>.git
cd <your-repo-name>
uv sync
```