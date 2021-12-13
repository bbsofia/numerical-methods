

def check(A, B, X):
    result = 0
    for i in range(0, len(A)):
        for j in range(0, len(A[i])):
            result += A[i][j] * X[j]
        if result != B[i]:
            return False
        result = 0
    return True



if __name__ == '__main__':
    A = [
        [2,  1, 1],
        [1, -1, 0,],
        [3, -1, 2],
    ]
    B = [2, -2, 2]
    X = [-1.0, 1.0, 3.0]
    print(check(A, B, X))