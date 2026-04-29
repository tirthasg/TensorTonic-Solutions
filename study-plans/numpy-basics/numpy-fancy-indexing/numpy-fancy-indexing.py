import numpy as np

def select_by_index(arr, indices, axis):
    """
    Returns: 2D ndarray of float64
    """
    arr = np.asarray(arr, dtype=np.float64)
    return arr[indices, :] if axis == 0 else arr[:, indices]