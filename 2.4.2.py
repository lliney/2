st = input()
i=1
newst=''
for c in range(len(st)):
    if c==len(st)-1:
        newst+=st[c]+str(i)
        break
    elif st[c]==st[c+1]:
        i+=1
    else:
        newst+= st[c] + str(i)
        i=1
print(newst)