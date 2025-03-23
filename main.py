from llm_interface import generate_text

def check_constraints(text, constraints):
    """
    Check if the generated text meets the specified constraints.
    
    Args:
        text (str): The generated text to check
        constraints (dict): Dictionary of constraints to check against
        
    Returns:
        dict: Results of constraint checks
    """
    results = {}
    
    # Check word count constraint if specified
    if "word_count" in constraints:
        word_count = len(text.split())
        results["word_count"] = {
            "target": constraints["word_count"],
            "actual": word_count,
            "satisfied": word_count == constraints["word_count"]
        }
    
    # Check allowed characters constraint if specified
    if "allowed_chars" in constraints:
        allowed_chars = set(constraints["allowed_chars"])
        invalid_chars = [c for c in text if c not in allowed_chars]
        results["allowed_chars"] = {
            "satisfied": len(invalid_chars) == 0,
            "invalid_chars": invalid_chars
        }
    
    return results

def main():
    # Example prompt
    prompt = "Generate a simple greeting"
    
    # Generate text using the LLM interface
    generated_text = generate_text(prompt)
    print(f"Generated text: {generated_text}")
    
    # Example constraints
    constraints = {
        "word_count": 2,
        "allowed_chars": "abcdefghijklmnopqrstuvwxyz "
    }
    
    # Check if the generated text meets the constraints
    constraint_results = check_constraints(generated_text, constraints)
    print("\nConstraint check results:")
    for constraint, result in constraint_results.items():
        print(f"{constraint}: {result}")

if __name__ == "__main__":
    main() 