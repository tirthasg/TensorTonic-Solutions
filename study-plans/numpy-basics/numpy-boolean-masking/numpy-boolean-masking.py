import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    arr = np.array(data)
    
    mask = arr > threshold
    any_row = np.where(mask.any(axis=1)[:, np.newaxis], arr, 0.0)
    all_row = np.where(mask.all(axis=1)[:, np.newaxis], arr, 0.0)

    return np.array([mask, any_row, all_row], dtype=np.float64)