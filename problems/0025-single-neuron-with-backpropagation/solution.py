import numpy as np

def sigmoid(z):
    return 1/(1+np.exp(-z))

def sigmoid_der(z):
    return sigmoid(z) * (1-sigmoid(z))

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray, initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):
    # Your code here
    updated_weights = initial_weights
    updated_bias = initial_bias
    sig = 0
    mse_values = []
    # in each epoch
    for _ in range(epochs):
        # forward pass over all training examples,
        z = np.dot(features, updated_weights) + updated_bias
        sig = sigmoid(z)
        mse_values.append(np.mean((sig - labels)**2)) # compute MSE loss
        # compute gradients averaged across the entire batch
        # backward pass (gradient aclculation)
        error = sig - labels
        delta = error * sigmoid_der(z) # (3,) features (3,2)
        weight_der = 2 * np.mean(delta[:,None] * features,axis = 0)
        bias_der = 2 * np.mean(delta)
        # param update
        updated_weights = updated_weights - learning_rate * weight_der
        updated_bias = updated_bias - learning_rate * bias_der
        
    updated_weights = np.round(updated_weights, 4).tolist()
    updated_bias = np.round(updated_bias,4)
    mse_values = np.round(mse_values, 4)
    return updated_weights, updated_bias, mse_values