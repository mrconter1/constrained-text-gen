from constraint_utils import check_constraints

def process_generated_text(text):
    """
    Process the generated text by splitting it into individual sentences.
    
    Args:
        text (str): The generated text
        
    Returns:
        list: List of candidate sentences
    """
    # Split the response into individual sentences (assuming one per line)
    candidate_sentences = [s.strip() for s in text.strip().split('\n') if s.strip()]
    return candidate_sentences

def validate_sentence(sentence, constraints):
    """
    Validate if a sentence meets the specified constraints.
    
    Args:
        sentence (str): The sentence to validate
        constraints (dict): Dictionary of constraints to check against
        
    Returns:
        tuple: (is_valid, constraint_results)
    """
    # Add sentence_count constraint for checking
    single_sentence_constraints = constraints.copy()
    single_sentence_constraints["sentence_count"] = 1
    
    return check_constraints(sentence, single_sentence_constraints) 