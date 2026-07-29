import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.asarray(A)
    n,n = A.shape
    sum = 0

    for i in range(n):
        for j in range(n):
            if (i == j):
                sum += A[i][j]
    return sum
