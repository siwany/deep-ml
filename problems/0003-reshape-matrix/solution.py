import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    try:
        reshape_matrix = np.reshape(a, new_shape)
        reshape_matrix.tolist()
        return reshape_matrix
    except ValueError:
        return []