import math
import numpy as np


def jacobi(A, B, N = 100):
    X = [0] * len(A)
    D = np.diag(A)  				
    R = A - np.diagflat(D) 		
    for i in range(N):  
        X = (B - np.dot(R, X)) / D
    return X
    

if __name__ == '__main__':
    A = [
        [2,  5, 4],
        [1, 3, 2,],
        [2, 10, 9],
    ]
    B = [30, 150, 110]
    print(f'Result: {jacobi(A, B)}')
