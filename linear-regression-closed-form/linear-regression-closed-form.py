import numpy as np

def linear_regression_closed_form(X: list, y: list) -> list:
    """
    Returns the optimal weight vector as a list.
    """
    X_np = np.array(X)
    y_np = np.array(y)
    gram_matrix = X_np.T@X
    inv_gram = np.linalg.inv(gram_matrix)
    Xty = X_np.T@y
    w=inv_gram@Xty
    return w