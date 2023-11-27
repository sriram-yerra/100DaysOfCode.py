def matrix(mat,n,m):
    row = [0]*n
    col = [0]*m
    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                row[i]=1
                col[j]=1
    for i in range(n):
        for j in range(m):
            if row[i] == 1 or col[j] == 1:
                mat[i][j] = 0
    return mat
mat = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
n=len(mat)
m=len(mat[0])
matrix(mat,n,m)
print(mat)
for i in range(n):
    for j in range(m):
        print(mat[i][j],end=" ")
    print(" ")