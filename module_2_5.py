def get_matrix(n, m, value):
    matrix = []
    a = []
    for i in range( n ):
        matrix[:] = []
        for j in range( m ):
            matrix.append( (value) )
        a.append(matrix)
    return a
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)