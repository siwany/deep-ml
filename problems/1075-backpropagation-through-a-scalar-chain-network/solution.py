import numpy as np

def sigmoid(z):
    return 1 / (1+np.exp(-z))

def backprop_chain(a0: float, y: float, w: list, b: list) -> dict:
    """
    Compute gradients of C = (a_L - y)^2 with respect to each weight and bias
    in a chain network where every layer has a single sigmoid neuron.

    Args:
        a0: input activation (scalar)
        y: target value (scalar)
        w: list of L weights
        b: list of L biases

    Returns:
        Dictionary with keys 'dW' and 'dB', each a list of L floats rounded to 6 places.
    """
    # run the forward pass for z^l and a^l
    L = len(w)
    z = []
    activations = [a0]
    for l in range(L): # make z and activation list 
        z.append(w[l] * activations[l] + b[l])
        activations.append(sigmoid(z[l])) # correct 

    # 2.initialize delta = 2 a^L - y
    delta = 2 * (activations[-1] - y) # correct
    dW = []
    dB = []
    # 3. for l=L  L-1,., 1
    for l in range(L):
        der_sigmoid = activations[L-l] * (1-activations[L-l]) 
        dW.insert(0,round(float(delta * der_sigmoid * activations[L-l-1]),6))
        dB.insert(0,round(float(delta * der_sigmoid),6))
        delta = delta * der_sigmoid * w[L-l-1]

    return {'dW': dW, 'dB': dB}
