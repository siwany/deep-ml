import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    for i in range(n_iter):
        # computer the prediction for the samples
        index = i % X.shape[0] # i mod n_samples
        y_pred = np.dot(X[index], weights)
        # compute MSE gradient with respect to the weights
        error = y_pred - y[index]
        mse = 2 * error * X[index]

        # update the weight using SGD rule 
        weights = weights - mse * learning_rate
    return weights
