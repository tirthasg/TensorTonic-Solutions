import numpy as np

def create_sequence(start, stop, param, kind):
    """
    Returns: 1D ndarray of float64 values
    """
    return (
        np.arange(
            start=start,
            stop=stop,
            step=param,
            dtype=np.float64,
        )
        if kind == "arange"
        else
        np.linspace(
            start=start,
            stop=stop,
            num=param,
            endpoint=True,
            dtype=np.float64
        )
    )
