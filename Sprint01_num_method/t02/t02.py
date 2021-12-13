import numpy as np


def gauss(A, B):
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
        X[i] = arr[i][len(arr)] / arr[i][i]  
    return X  





if __name__ == "__main__":
        A = [
        [2,  5, 4],
        [1, 3, 2,],
        [2, 10, 9],
    ]
    B = [30, 150, 110]
    print(f'Result: {gauss(A, B)}')
