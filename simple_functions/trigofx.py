import numpy as np
from math import factorial


def cosx(n):
    """Return sin(x) for a non-negative integer n."""
    return np.cos(n)


def cosx_taylor(n):
    '''Return cos(x) but using Taylor Series'''
    taylor_cosx = 1
    - (n**2)/factorial(2)
    + (n**4)/factorial(4)
    - (n**6)/factorial(6)
    + (n**8)/factorial(8)
    - (n**10)/factorial(10)
    + (n**12)/factorial(12)
    - (n**14)/factorial(14)
    + (n**16)/factorial(16)
    return taylor_cosx
