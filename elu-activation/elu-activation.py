import math

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    return [y if y>0 else  alpha*(math.exp(y)-1)for y in x]