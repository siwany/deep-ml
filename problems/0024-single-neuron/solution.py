import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
    # Your code here
    mse = []
    probabilities = []
    for feature in features:
        z = sum(w * f for w, f in zip(weights, feature)) + bias
        probabilities.append(round(1/(1+math.exp(-z)),4))
    mse = 1/len(probabilities) * sum((p - l)**2 for p,l in zip(probabilities, labels))
    return (probabilities, mse)