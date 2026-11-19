import numpy as np

def compute_chain_rule_gradient(functions: list[str], x: float) -> float:
    """
    Compute derivative of composite functions using chain rule.
    
    Args:
        functions: List of function names (applied right to left)
                  Available: 'square', 'sin', 'exp', 'log'
        x: Point at which to evaluate derivative
    
    Returns:
        Derivative value at x
    
    Example:
        ['sin', 'square'] represents sin(x²)
        ['exp', 'sin', 'square'] represents exp(sin(x²))
    """
    # Your code here
    value = x
    derivative = 1.0
    for function in reversed(functions):
        if function == 'square':
            derivative *= 2 * value
            value = value ** 2
        elif function == 'sin':
            derivative *= np.cos(value) # 2 * cos(1)
            value = np.sin(value) # sin(1)
        elif function == 'exp':
            derivative *= np.exp(value)
            value = np.exp(value)
        elif function == 'log':
            derivative *= 1/value
            value = np.log(value)
        else:
            ValueError()
    return derivative
        
        