import numpy as np

def vector_norms(v):
    """
    Returns: float64 array of shape (3,) containing [L1, L2, L-inf] norms.
    """
    arr = np.asarray(v, dtype=np.float64)
    
    l1_norm = np.sum(np.abs(arr))
    l2_norm = np.sqrt(np.sum(arr**2))
    linf_norm = np.max(np.abs(arr))

    return np.array([l1_norm, l2_norm, linf_norm])