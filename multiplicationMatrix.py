def multiplicationMatrix(A,B):
    """
    This method is used for visualization of multiplication of Matrix A and B
    
    :param A: Matrix A 
    :param B: Matrix B
    """
    rows = len(A)
    cols = len(B[0])
    result = [[0 for _ in range(cols)]for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            for k in range(len(B[0])):
                result[i][j] += A[i][k]*B[k][j]
    return result
A = [
    [1,2,4,5,6],
    [4,2,6,7,8],
    [1,3,4,5,6],
    [0,1,4,1,1],
    [1,3,4,5,6]
]

B = [
    [1,2,4,5,6],
    [4,2,6,7,8],
    [1,3,4,5,6],
    [0,1,4,1,1],
    [1,3,4,5,6]
]

result = multiplicationMatrix(A,B)
for row in result:
    print(row)