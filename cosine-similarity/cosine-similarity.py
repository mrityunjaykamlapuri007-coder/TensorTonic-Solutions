import numpy as np

def cosine_similarity(a,b):

    A = np.asarray(a)
    B = np.asarray(b)

    n1 = len(A)
    n2 = len(B)

    S1 = 0
    S2 = 0

    d = np.dot(A,B)

    if (d == 0):
        c = 0
    
    else:
        for i in range(n1):
            S1 = S1 + np.square(A[i])
        l2_A = np.sqrt(S1)

        for i in range(n2):
            S2 = S2 + np.square(B[i])

        l2_B = np.sqrt(S2)

        c = d/(l2_A * l2_B)

    
    return float(c)