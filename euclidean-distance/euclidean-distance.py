import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    X = np.asarray(x)
    Y = np.asarray(y)

    diff = np.abs(len(X) - len(Y))

    a = np.zeros(diff)

    if (len(Y) != len(X)):
        raise ValueError("not equal vectors")

    n = len(X)
    sum = 0

    for i in range(n):
        diff = X[i] - Y[i]
        sq = np.square(diff)
        sum = sum + sq
    
    d = np.sqrt(sum)

    return float(d)