import json

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