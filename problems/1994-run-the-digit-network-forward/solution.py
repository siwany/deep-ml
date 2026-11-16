import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def digit_network_forward(image, weights, biases):
    """Run an image through a fully connected sigmoid network.

    Returns (output activations rounded to 4 decimals, predicted digit).
    """
    flattened = np.array(image).flatten()
    a = flattened
    for weight, bias in zip(weights, biases):
        z = np.matmul(weight, a) + bias # previous layer * weight + bias
        a = sigmoid(z)
    return (a.tolist(), np.argmax(a))


