import numpy as np

def matrix_vector_multiply(A, x):
    """
    Returns: 1-D float64 array, the product A @ x.
    """
    matrix = np.asarray(A)
    vec = np.asarray(x)

    return np.dot(matrix, vec)