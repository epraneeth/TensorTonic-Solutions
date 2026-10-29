import math

def selu(x: list) -> list:
    """
    Returns SELU values rounded to four decimal places.
    """
    return [1.0507*y if y>0 else 1.0507*1.6733*(math.exp(y)-1) for y in x]