import math
import numpy as np 
import copy

def cramer(A, B):
    det = [0] * (len(A)+1) 
    if len(A) > 4: 
        return 0 
    det[0] = np.linalg.det(A) 
    if (det[0] != 0):
        X = [0] * len(A) 
        for j in range(0, len(A)): 
            C = copy.deepcopy(A)
            print(A) 
            for i in range(0, len(C)): 
                C[i][j] = B[i] 
                print(C) 
            det[j+1] = np.linalg.det(C) 
            X[j] = det[j+1]/det[0]  
        return X 
    else:
        return 0


if __name__ == '__main__':
    A = [
        [2,  5, 4],
        [1, 3, 2,],
        [2, 10, 9],
    ]
    B = [30, 150, 110]
    print(f'Result: {cramer(A, B)}')
       