import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    X = np.asarray(x)
    Y = np.asarray(y)

    if(len(X) != len(Y)):
        raise ValueError("Not equal lengths vectors")

    n = len(X)

    d = 0
    for i in range(n):
        d = d + (X[i]*Y[i])
        
    return float(d)