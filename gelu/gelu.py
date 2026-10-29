import math
import numpy as np

def gelu(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    ans = np.array(x)
    return (ans/2)*(1+np.vectorize(math.erf)(ans/np.sqrt(2)))