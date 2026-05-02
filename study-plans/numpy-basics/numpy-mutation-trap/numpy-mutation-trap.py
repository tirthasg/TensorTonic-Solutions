import numpy as np

def original_and_clipped(data, row_idx, lo, hi):
    """
    Returns: 2D ndarray of float64 with shape (2, ncols)
    """
    arr = np.asarray(data, dtype=np.float64)

    original = arr[row_idx]
    clipped = np.clip(original, lo, hi)
    return np.stack([original, clipped])