import numpy as np

def softmax(x: list) -> np.ndarray:
    """
    Returns stable softmax probabilities as a NumPy array matching the shape of x.
    """
    ans = np.array(x)
    m=np.max(ans,axis=-1,keepdims=True)
    return np.exp(ans-m)/np.sum(np.exp(ans-m), axis=-1, keepdims=True)