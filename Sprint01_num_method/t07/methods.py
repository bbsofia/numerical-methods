import numpy as np
import math 
import copy


class Method:

    def __init__(self):
        pass

    def degeneracy(self, matrix):
        det = np.linalg.det(matrix)
        if (det != 0): 
            return True
        else: 
            return False


    def checking(self, A, B, X):
        result = 0
        for i in range(0, len(A)):
            for j in range(0, len(A[i])):
                result += A[i][j] * X[j]
            if result != B[i]:
                return False
            result = 0
        return True

     
    def cramer(self, A, B):
        det = [0] * (len(A)+1) 
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
                X[j] = round(det[j+1]/det[0], 2)
            return True, X 
        else:
            return False


    def gauss(self, A, B):
        X = [0] * len(A)
        arr = [0] * len(A)
        for i in range(0, len(A)):
            arr[i] = [0] * (len(A) + 1)
            arr[i][len(A)] = B[i]
            for k in range(0, len(A[i])):
                arr[i][k] = A[i][k]
        for i in range(0, len(arr)):
            if i == 0: 
                for k in range(0, len(arr[i])-1):
                    if arr[0][k] != 0:
                        index = k
                        break
            else:
                if index > 0:
                    for k in range(0, len(arr[i])):
                        p = arr[0][k]
                        arr[0][k] = arr[index][k]
                        arr[index][k] = p
                    break  
        index = 0
        x = 1
        while x != 0 :
            x = 0
            for i in range(index + 1, len(arr)):
                x += 1
                if arr[i][index] == 0:
                    continue
                else:
                    point = arr[i][index]/arr[index][index]
                    for k in range(index, len(arr[i])):
                        arr[i][k] -=  point * arr[index][k]
            index += 1
        for i in range(len(arr) - 1, -1, -1):
            for k in range(len(arr) - 1, i, -1):
                arr[i][len(arr)] = arr[i][len(arr)] - arr[i][k] * X[k]
            X[i] = round(arr[i][len(arr)] / arr[i][i], 2)  
        return True, X
            


    def seidel(self, A, b):
        eps = 1
        n = len(A)
        x = np.zeros(n)  # zero vector
        converge = False
        while not converge:
            x_new = np.copy(x)
            for i in range(n):
                s1 = sum(A[i][j] * x_new[j] for j in range(i))
                s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
                x_new[i] = round((b[i] - s1 - s2) / A[i][i], 2)
            converge = np.sqrt(sum((x_new[i] - x[i]) for i in range(n))) <= eps
            x = x_new

        return True, x



    def jordan_gauss(self, A, B):
        arr = [0] * len(A)
        for i in range(0, len(A)):
            arr[i] = [0] * (len(A) + 1)
            arr[i][len(A)] = B[i]
            for k in range(0, len(A[i])):
                arr[i][k] = A[i][k]
        for i in range(0, len(arr)):
            if i == 0: 
                for k in range(0, len(arr[i])-1):
                    if arr[0][k] != 0:
                        index = k
                        break
            else:
                if index > 0:
                    for k in range(0, len(arr[i])):
                        p = arr[0][k]
                        arr[0][k] = arr[index][k]
                        arr[index][k] = p
                    break  
        index = 0
        x = 1
        while x != 0 :
            x = 0
            for i in range(index + 1, len(arr)):
                x += 1
                if arr[i][index] == 0:
                    continue
                else:
                    point = arr[i][index]/arr[index][index]
                    for k in range(index, len(arr[i])):
                        arr[i][k] -=  point * arr[index][k]
            index += 1

        for i in range(0, len(arr)):
            point = arr[i][i]
            for k in range(0, len(arr[i])):
                arr[i][k] = arr[i][k]/point
        
        index = 1
        x = 2
        while x != 4 :
            d = 0
            for i in range(len(arr) - 2, -1, -1):
                d += 1
                index = len(arr[i]) - 2
                if arr[i][index] == 0:
                    if i == index - 1:
                        d = 0
                        continue
                    else:
                        index -=1
                point = arr[i][index]
                for k in range(0, len(arr[i])):
                    arr[i][k] -=  point * arr[i+d][k]
            x += 1
        X = [0] * len(A)
        for i in range(0, len(A)):
            X[i] = round(arr[i][len(A)], 2)
        return True, X

    def jacobi(self, A, B, N = 100):
        X = [0] * len(A)
        D = np.diag(A)  				
        R = A - np.diagflat(D) 		
        for i in range(N):  
            X = round((B - np.dot(R, X)) / D, 2)
        return True, X