import numpy as np

def make_diagonal(v):
    """
    Returns: (n, n) NumPy array with v on the main diagonal
    """
    V = np.asarray(v)
    n = len(V)
    
    V_n = np.zeros((n,n), dtype = V.dtype)
    
    for i in range(n):
        for j in range(n):
            if (i == j):
                V_n[i][j] = V[i]
            else:
                V_n[i][j] = 0

    return V_n

    
