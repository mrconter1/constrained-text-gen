import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Specify the model directly in the code
OPENROUTER_MODEL = "anthropic/claude-3.7-sonnet"

# Initialize OpenAI client with OpenRouter base URL
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=OPENROUTER_API_KEY,
)

def generate_text(prompt):
    """
    Generate text using Claude 3.7 Sonnet via OpenRouter API.
    
    Args:
        prompt (str): The input prompt for the LLM
        
    Returns:
        str: Generated text from the LLM
    """
    try:
        if not OPENROUTER_API_KEY:
            # Fallback to hardcoded responses if API key is missing
            print("Warning: Using fallback responses. Set OPENROUTER_API_KEY in .env file.")
            return _fallback_generate(prompt)
        
        # Make API request to OpenRouter
        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        # Extract and return the generated text
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print(f"Error calling LLM API: {e}")
        # Fallback to hardcoded responses in case of error
        return _fallback_generate(prompt)

def _fallback_generate(prompt):
    """Fallback function that returns hardcoded responses for testing."""
    # Parse the prompt to see how many sentences are requested
    import re
    sentences_requested = 1
    match = re.search(r'generate (\d+) sentences', prompt.lower())
    if match:
        sentences_requested = int(match.group(1))
    
    # Sample sentences for simulation
    sample_sentences = [
        "astronauts launch toward distant mars",
        "space vehicles carry precious cargo",
        "exploration begins with careful preparation",
        "scientific instruments record valuable data",
        "human presence extends beyond earth"
    ]
    
    import random
    
    # Generate the requested number of sentences
    selected_sentences = []
    for _ in range(min(sentences_requested, len(sample_sentences))):
        selected_sentences.append(random.choice(sample_sentences))
    
    # Return sentences, one per line
    return "\n".join(selected_sentences) 