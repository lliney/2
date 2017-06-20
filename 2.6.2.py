a=[]
n = int(input())
for i in range(n):
    for j in range(i+1):
        if len(a)+1>n:
            break
        else:
            a.append(i+1)
for k in a:
    print(k, end=' ')