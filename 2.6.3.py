lst = [int(i) for i in input().split()]
x = int(input())
s=0
for j in range(len(lst)):
    if x==lst[j]:
        print(j, end=' ')
        s+=1
if s==0:
    print('Отсутствует')