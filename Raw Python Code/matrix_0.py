matrix = [[1,1,1],[1,0,0],[1,1,1]]
# Output: [[1,0,0],[0,0,0],[1,0,0]]

l1 = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == 0:
            l1.append([i, j])
print(l1)
for i in range(len(l1)):
    for j in range(len(matrix[0])):
        matrix[l1[i][0]][j] = 0
    for k in range(len(matrix)):
        matrix[k][l1[i][1]] = 0
print(matrix)