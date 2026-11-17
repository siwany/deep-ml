import numpy as np

def gradient_descent(X, y, weights, learning_rate, n_epochs, batch_size=1, method='batch'):
    """
    Perform gradient descent optimization.
    
    Args:
        X: Feature matrix of shape (m, n)
        y: Target values of shape (m,)
        weights: Initial weights of shape (n,)
        learning_rate: Step size for gradient descent
        n_epochs: Number of complete passes through the dataset
        batch_size: Size of batches for mini-batch gradient descent (default: 1)
        method: Type of gradient descent ('batch', 'stochastic', or 'mini_batch')
    
    Returns:
        Optimized weights
    """
    # return updated weights
    if method == 'batch': # full batch GD
        for i in range(n_epochs):
            m = X.shape[0] # 4
            mse = np.dot(X, weights) - y # X = (4,2) y = (4,) weights = (2,) -> mse = (4,2)
            weights = weights - learning_rate * 2/m * np.dot(mse,X)
    elif method == 'stochastic':
        for epoch in range(n_epochs):
            m = X.shape[0]
            for i in range(m):
                mse = np.dot(X[i],weights) - y[i]
                weights = weights - 2*learning_rate * mse * X[i]
    elif method =='mini_batch':
        for epochs in range(n_epochs):
            m = X.shape[0] # (4,)
            for i in range(0, m, batch_size):
                mse = np.dot(X[i: i+batch_size], weights) - y[i:i+batch_size] 
                weights = weights - learning_rate * 2/len(X[i:i+batch_size]) * np.dot(mse,X[i:i+batch_size]) # last batch can be smaller
    else:
        raise ValueError()
    return weights
