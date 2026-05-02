import numpy as np

def row_summary(data, threshold):
    """Returns: np.ndarray of shape (3, m, n), stacked element mask, any-filtered, all-filtered"""
    arr = np.asarray(data, dtype=np.float64)

    mask = (arr > threshold).astype(np.float64)
    mask_any = np.any(mask, axis=1, keepdims=True)
    mask_all = np.all(mask, axis=1, keepdims=True)

    return np.stack([
        mask,
        arr * mask_any,
        arr * mask_all,
    ])