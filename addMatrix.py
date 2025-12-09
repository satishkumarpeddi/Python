def addMatrix(A,B):
    """
    This method is used for visualization of addition of Matrix A and B
    
    :param A: Matrix A 
    :param B: Matrix B
    """
    rows = len(A)
    cols = len(A[0])
    result = [[0 for _ in range(cols)]for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = A[i][j]+B[i][j]
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

result = addMatrix(A,B)
for row in result:
    print(row)