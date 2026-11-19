import numpy as np
def activation_derivatives(x: float) -> dict[str, float]:
    """
    Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
    
    Args:
        x: Input value
        
    Returns:
        Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
    """
    def sigmoid(x):
        return 1 / (1+np.exp(-x))
    def der_sigmoid(x):
        return sigmoid(x) * (1-sigmoid(x))
    def der_relu(x):
        return 1 if x > 0 else 0
    # Your code here
    return {'sigmoid': der_sigmoid(x), 'tanh': 1-np.tanh(x)**2, 'relu': der_relu(x) }