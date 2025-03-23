from llm_interface import generate_text

def check_constraints(text, constraints):
    """
    Check if the generated text meets the specified constraints.
    
    Args:
        text (str): The generated text to check
        constraints (dict): Dictionary of constraints to check against
        
    Returns:
        tuple: (bool, dict) indicating if all constraints are satisfied and detailed results
    """
    results = {}
    all_satisfied = True
    
    # Check word count constraint if specified
    if "word_count" in constraints:
        word_count = len(text.split())
        satisfied = word_count == constraints["word_count"]
        results["word_count"] = {
            "target": constraints["word_count"],
            "actual": word_count,
            "satisfied": satisfied
        }
        all_satisfied = all_satisfied and satisfied
    
    # Check allowed characters constraint if specified
    if "allowed_chars" in constraints:
        allowed_chars = set(constraints["allowed_chars"])
        invalid_chars = [c for c in text if c not in allowed_chars]
        satisfied = len(invalid_chars) == 0
        results["allowed_chars"] = {
            "satisfied": satisfied,
            "invalid_chars": invalid_chars
        }
        all_satisfied = all_satisfied and satisfied
    
    # Check sentence count constraint if specified
    if "sentence_count" in constraints:
        # Simple sentence splitting by ., !, ?
        import re
        sentences = re.split(r'[.!?]+', text)
        # Remove empty strings that might result from the split
        sentences = [s.strip() for s in sentences if s.strip()]
        sentence_count = len(sentences)
        satisfied = sentence_count == constraints["sentence_count"]
        results["sentence_count"] = {
            "target": constraints["sentence_count"],
            "actual": sentence_count,
            "satisfied": satisfied
        }
        all_satisfied = all_satisfied and satisfied
    
    return all_satisfied, results

def create_prompt(context, constraints, sentences_per_response=1):
    """
    Create a prompt for the LLM based on context and constraints.
    
    Args:
        context (str): The theme and context for text generation
        constraints (dict): Dictionary of constraints to guide the generation
        sentences_per_response (int): Number of sentences to request in each response
        
    Returns:
        str: Formatted prompt for the LLM
    """
    # Format constraints as JSON
    import json
    
    # Format constraints as JSON
    constraints_json = json.dumps(constraints, indent=2)
    
    # Create prompt in the requested format
    prompt = f'''
Given the following context:

{context}

try to generate {sentences_per_response} sentences that adhere to that while simultaneously making sure that each sentence adheres to the following constraints:

{constraints_json}

only reply with sentences and nothing else, one line per sentence
'''
    
    return prompt

def main():
    # Context variable (multiline theme/context description)
    context = """
    Theme: Space Exploration
    Setting: Near future, first human mission to Mars
    Tone: Inspirational, scientific, adventurous
    """
    
    # Number of sentences to generate in total
    total_sentences_needed = 5
    
    # Number of sentences to request in each LLM call
    sentences_per_request = 3
    
    # Maximum number of attempts to generate sentences
    MAX_ATTEMPTS = 10
    
    # Example constraints
    constraints = {
        "word_count": 5,
        "allowed_chars": "abcdefghijklmnopqrstuvwxyz "
    }
    
    # Create the prompt
    prompt = create_prompt(context, constraints, sentences_per_request)
    print(f"Generated prompt:\n{prompt}\n")
    
    # Try to generate the requested number of valid sentences
    valid_sentences = []
    attempts = 0
    
    print("Generating sentences...")
    while len(valid_sentences) < total_sentences_needed and attempts < MAX_ATTEMPTS:
        attempts += 1
        
        # Generate text using the LLM interface
        generated_text = generate_text(prompt)
        
        print(f"\nAttempt {attempts}:")
        print(f"Generated text:\n{generated_text}")
        
        # Split the response into individual sentences (assuming one per line)
        candidate_sentences = [s.strip() for s in generated_text.strip().split('\n') if s.strip()]
        
        print(f"Found {len(candidate_sentences)} candidate sentences in response")
        
        # Check each sentence against constraints
        for i, sentence in enumerate(candidate_sentences):
            # Check if the generated text meets the constraints
            # Add sentence_count constraint for checking
            single_sentence_constraints = constraints.copy()
            single_sentence_constraints["sentence_count"] = 1
            
            is_valid, constraint_results = check_constraints(sentence, single_sentence_constraints)
            
            print(f"\nCandidate {i+1}: {sentence}")
            print("Constraint check results:")
            for constraint, result in constraint_results.items():
                print(f"  {constraint}: {result}")
            
            # Save valid sentences
            if is_valid:
                print("✓ Valid sentence! Adding to collection.")
                valid_sentences.append(sentence)
                # Stop if we have enough sentences
                if len(valid_sentences) >= total_sentences_needed:
                    break
            else:
                print("✗ Invalid sentence! Discarding.")
    
    # Display final results
    print("\n" + "="*50)
    print(f"Generated {len(valid_sentences)}/{total_sentences_needed} valid sentences in {attempts} attempts.")
    
    if valid_sentences:
        print("\nValid sentences:")
        for i, sentence in enumerate(valid_sentences, 1):
            print(f"{i}. {sentence}")
    
    # Report if couldn't generate enough sentences
    if len(valid_sentences) < total_sentences_needed:
        print(f"\nWarning: Could only generate {len(valid_sentences)} valid sentences after {MAX_ATTEMPTS} attempts.")

if __name__ == "__main__":
    main() 