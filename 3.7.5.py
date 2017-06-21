b = [[1, 0,0], [2, 0,0], [3, 0,0], [4, 0,0], [5, 0,0], [6, 0,0], [7, 0,0], [8, 0,0], [9, 0,0], [10, 0,0], [11, 0,0]]
with open('dataset_3380_5.txt') as f:
    for line in f:
        l=[line.strip() for line in f]
mas=[j.split('\t') for j in l]
#print(mas[0][0])
for i in range(len(mas)):
    if int(mas[i][0])==1:
        b[0][1]+=int(mas[i][2])
        b[0][2]+=1
    elif int(mas[i][0])==2:
        b[1][1]+=int(mas[i][2])
        b[1][2]+=1
    elif int(mas[i][0])==3:
        b[2][1]+=int(mas[i][2])
        b[2][2]+=1
    elif int(mas[i][0])==4:
        b[3][1]+=int(mas[i][2])
        b[3][2]+=1
    elif int(mas[i][0])==5:
        b[4][1]+=int(mas[i][2])
        b[4][2]+=1
    elif int(mas[i][0])==6:
        b[5][1]+=int(mas[i][2])
        b[5][2]+=1
    elif int(mas[i][0])==7:
        b[6][1]+=int(mas[i][2])
        b[6][2]+=1
    elif int(mas[i][0])==8:
        b[7][1]+=int(mas[i][2])
        b[7][2]+=1
    elif int(mas[i][0])==9:
        b[8][1]+=int(mas[i][2])
        b[8][2]+=1
    elif int(mas[i][0])==10:
        b[9][1]+=int(mas[i][2])
        b[9][2]+=1
    elif int(mas[i][0])==11:
        b[10][1]+=int(mas[i][2])
        b[10][2]+=1

for i in range(len(b)):
    if b[i][2]==0:
        b[i][1]='-'
        print(b[i][0],end=' ')
        print(b[i][1])
    else:
        b[i][1]=(b[i][1])/(b[i][2])
        print(b[i][0], end=' ')
        print(b[i][1])


