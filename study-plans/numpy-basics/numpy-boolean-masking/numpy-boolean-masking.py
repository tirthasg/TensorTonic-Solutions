import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    arr = np.asarray(data, dtype=np.float64)
    
    mask = (arr > threshold).astype(np.int64)
    arr_any = np.where(mask.any(axis=1)[:, np.newaxis], arr, 0.0)
    arr_all = np.where(mask.all(axis=1)[:, np.newaxis], arr, 0.0)

    return np.array([mask, arr_any, arr_all])