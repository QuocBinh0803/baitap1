def rotate_matrix(matrix):
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n -1 - layer 
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
matrix = [
    [7,2,1],
    [4,5,6],
    [9,8,3],
]
print("Original Matrix:")
for row in matrix:
    print(row)
rotate_matrix(matrix)
print("\nRotated Matrix:")
for row in matrix:
    print(row)