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
    
    # Check word count range constraint if specified
    if "word_count_range" in constraints:
        word_count = len(text.split())
        min_words, max_words = constraints["word_count_range"]
        satisfied = min_words <= word_count <= max_words
        results["word_count_range"] = {
            "target_range": constraints["word_count_range"],
            "actual": word_count,
            "satisfied": satisfied
        }
        all_satisfied = all_satisfied and satisfied
    
    # Check word count constraint (legacy/exact) if specified
    elif "word_count" in constraints:
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