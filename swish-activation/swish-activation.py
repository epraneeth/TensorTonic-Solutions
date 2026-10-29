import numpy as np

def swish(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    ans = np.array(x)
    return ans*(1/(1+np.exp(-ans)))