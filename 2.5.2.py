a=[int(i) for i in input().split()]
b=[0]*len(a)
if len(a)<=2:
    b=a
else:
    for c in range(len(a)):
        if c==0:
            b[c]=a[c+1]+a[len(a)-1]
            #print(b[c])
        elif c==len(a)-1:
            b[c]=a[0]+a[len(a)-2]
           # print(b[c])
        else:
            b[c]=a[c-1]+a[c+1]
            #print(b[c])
for d in b:
    print(d, end=' ')