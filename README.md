# Constrained Text Generation

A Python project for generating text using Large Language Models (LLMs) with specified constraints.

## Project Structure

- `main.py` - Main entry point that handles text generation and constraint checking
- `llm_interface.py` - Interface for interacting with LLMs (currently returns hardcoded responses)

## Getting Started

1. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

2. Run the main script:
   ```
   python main.py
   ```

## Features

- Text generation via LLM interface (placeholder for now)
- Constraint checking:
  - Word count
  - Allowed characters
  - More constraints to be added

## Future Improvements

- Connect to actual LLM APIs (OpenAI, Hugging Face, etc.)
- Add more sophisticated constraints
- Implement constraint-aware prompting 