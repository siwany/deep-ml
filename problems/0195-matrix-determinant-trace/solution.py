def determinant_2x2(matrix:list[list[float]]):
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def determinant(matrix):
    if len(matrix) == 2:
        return determinant_2x2(matrix)

    det = 0
    for j in range(len(matrix)):
        # 1. Build minor matrix excluding row 0 and column j
        minor = [[row[k] for k in range(len(matrix)) if k != j] for row in matrix[1:]]
        # 2. Calculate determinant of minor recursively
        minor_det = determinant(minor)
        # 3. Add (-1)**j * matrix[0][j] * minor determinant
        det += (-1) ** j * matrix[0][j] * minor_det

    return det

def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    trace = 0
    for i in range(len(matrix)):
        trace += matrix[i][i]
    return (determinant(matrix), trace)