import numpy as np

def tanh(x: list) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    ans = np.array(x)
    ex=np.exp(ans)
    exn=np.exp(-ans)
    answer = (ex-exn)/(ex+exn)
    return answer