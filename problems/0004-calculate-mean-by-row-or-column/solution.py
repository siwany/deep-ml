import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    map = {'row':1, 'column':0}
    return np.mean(matrix, map[mode])