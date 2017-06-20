matrix=[]
while True:
    p=[str(n) for n in input().split()]
    if p==['end']:
        break
    matrix+=[p]

for i in range(len(matrix)) :
    for j in range(len(matrix[0])) :
        if i == len(matrix)-1 and j == len(matrix[0])-1 :
            print(int(matrix[i - 1][j]) + int(matrix[0][j]) + int(matrix[i][j - 1]) + int(matrix[i][0]), end=' ')
        elif j == len(matrix[0])-1 :
            print(int(matrix[i - 1][j]) + int(matrix[i + 1][j]) + int(matrix[i][j - 1]) + int(matrix[i][0]), end=' ')
        elif i == len(matrix)-1 :
            print(int(matrix[i - 1][j]) + int(matrix[0][j]) + int(matrix[i][j - 1]) + int(matrix[i][j + 1]), end=' ')
        else :
            print(int(matrix[i - 1][j]) + int(matrix[i + 1][j]) + int(matrix[i][j - 1]) + int(matrix[i][j + 1]), end=' ')
    print()