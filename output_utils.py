def print_constraint_results(sentence, constraint_results, index):
    """
    Print the constraint check results for a sentence.
    
    Args:
        sentence (str): The sentence
        constraint_results (dict): Results of constraint checks
        index (int): Index of the sentence in the current batch
    """
    print(f"\nCandidate {index+1}: {sentence}")
    print("Constraint check results:")
    for constraint, result in constraint_results.items():
        print(f"  {constraint}: {result}")

def print_final_results(valid_sentences, total_needed, attempts, max_attempts):
    """
    Print the final results after all attempts.
    
    Args:
        valid_sentences (list): List of valid sentences
        total_needed (int): Total number of sentences needed
        attempts (int): Number of attempts made
        max_attempts (int): Maximum number of attempts allowed
    """
    print("\n" + "="*50)
    print(f"Generated {len(valid_sentences)}/{total_needed} valid sentences in {attempts} attempts.")
    
    if valid_sentences:
        print("\nValid sentences:")
        for i, sentence in enumerate(valid_sentences, 1):
            print(f"{i}. {sentence}")
    
    # Report if couldn't generate enough sentences
    if len(valid_sentences) < total_needed:
        print(f"\nWarning: Could only generate {len(valid_sentences)} valid sentences after {max_attempts} attempts.") 