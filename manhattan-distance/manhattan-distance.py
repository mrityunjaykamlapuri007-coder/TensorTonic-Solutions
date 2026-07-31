import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    X = np.asarray(x)
    Y = np.asarray(y)

    n = len(X)

    sum = 0

    for i in range (n):
        ab = np.abs(X[i]-Y[i])
        sum = sum + ab

    return float(sum)