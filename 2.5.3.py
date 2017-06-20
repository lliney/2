a=[int(i) for i in input().split()]
b = sorted(a)
i=0
if len(b)>1:
    for c in range(len(b)):
        if  c==len(b)-1:
            if i>=1:
                print(b[c], end=' ')

            else:
                break


        elif b[c]==b[c+1]:

            i += 1
        else:
            if i >=1:
                print(b[c],end=' ')
                i = 0