import numpy as np

def summarize(data, axis):
    """Returns: np.ndarray of shape (4, k), rows are mean, std, min, max"""    
    means = np.mean(data, axis=axis)
    stds = np.std(data, axis=axis)
    mins = np.min(data, axis=axis)
    maxs = np.max(data, axis=axis)

    return np.vstack((means, stds, mins, maxs))