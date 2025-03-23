from llm_interface import generate_text
from text_processor import process_generated_text, validate_sentence
from output_utils import print_constraint_results, print_final_results
from prompt_utils import create_prompt

def generate_sentences(context, constraints, total_needed, sentences_per_request, max_attempts):
    """
    Generate sentences using the LLM that adhere to the given constraints.
    
    Args:
        context (str): The context for generation
        constraints (dict): The constraints to check against
        total_needed (int): Total number of sentences needed
        sentences_per_request (int): Number of sentences to request in each LLM call
        max_attempts (int): Maximum number of attempts to try
        
    Returns:
        list: List of valid sentences
    """
    # Create the prompt
    prompt = create_prompt(context, constraints, sentences_per_request)
    print(f"Generated prompt:\n{prompt}\n")
    
    # Try to generate the requested number of valid sentences
    valid_sentences = []
    attempts = 0
    
    print("Generating sentences...")
    while len(valid_sentences) < total_needed and attempts < max_attempts:
        attempts += 1
        
        # Generate text using the LLM interface
        generated_text = generate_text(prompt)
        
        print(f"\nAttempt {attempts}:")
        print(f"Generated text:\n{generated_text}")
        
        # Process the generated text into candidate sentences
        candidate_sentences = process_generated_text(generated_text)
        
        print(f"Found {len(candidate_sentences)} candidate sentences in response")
        
        # Check each sentence against constraints
        for i, sentence in enumerate(candidate_sentences):
            # Validate the sentence
            is_valid, constraint_results = validate_sentence(sentence, constraints)
            
            # Print validation results
            print_constraint_results(sentence, constraint_results, i)
            
            # Save valid sentences
            if is_valid:
                print("✓ Valid sentence! Adding to collection.")
                valid_sentences.append(sentence)
                # Stop if we have enough sentences
                if len(valid_sentences) >= total_needed:
                    break
            else:
                print("✗ Invalid sentence! Discarding.")
    
    # Print final results
    print_final_results(valid_sentences, total_needed, attempts, max_attempts)
    
    return valid_sentences 