a=int(input())
b=int(input())+1
c=int(input())
d=int(input())+1
for j in range(c, d):
    print('\t', j, end='')
print()
for i in range(a,b):
    print(i, end='\t')
    for j in range(c,d):
        print(j*i, end='\t')
    print()