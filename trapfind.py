import random


row = int(input())
col = int(input())

boom = [0,1]

matrix = []
for i in range(row):
    y = []
    for j in range(col):
        x = random.choice(boom)
        y.append(x)

    matrix.append(y)    
    y = []

for i in matrix:
    for j in i :
        print(j, end=' ')
    print()
print()

for i in range(len(matrix)) :
    for j in range(len(matrix[i])) :
        if matrix[i][j] == 0:            
            starcount = matrix[i-1][j-1:j+2].count(1) + matrix[i][j-1:j+2].count(1) + matrix[i+1][j-1:j+2].count(1)
            matrix[i][j]=starcount
        else :
            matrix[i][j] = '*'
        print(matrix[i][j],end=' ')
    print()

