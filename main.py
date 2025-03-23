from generator import generate_sentences

# Constants
DEFAULT_CONTEXT = """
Theme: Space Exploration
Setting: Near future, first human mission to Mars
Tone: Inspirational, scientific, adventurous
"""

DEFAULT_CONSTRAINTS = {
    "word_count_range": [4, 6],  # Accept sentences with 4-6 words
    "allowed_chars": "abcdefghijklmnopqrstuvwxyz "
}

TOTAL_SENTENCES_NEEDED = 5
SENTENCES_PER_REQUEST = 3
MAX_ATTEMPTS = 10

def main():
    """
    Main function that orchestrates the constrained text generation process.
    """
    # Use the default context and constraints
    context = DEFAULT_CONTEXT
    constraints = DEFAULT_CONSTRAINTS.copy()
    
    # Generate sentences
    generate_sentences(
        context, 
        constraints, 
        TOTAL_SENTENCES_NEEDED, 
        SENTENCES_PER_REQUEST, 
        MAX_ATTEMPTS
    )

if __name__ == "__main__":
    main() 