import numpy as np

def jordan_gauss(A, B):
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
        X[i] = arr[i][len(A)]
    return X
      


if __name__ == '__main__':
       A = [
        [2,  5, 4],
        [1, 3, 2,],
        [2, 10, 9],
    ]
    B = [30, 150, 110]
    print(f'Result: {jordan_gauss(A, B)}')