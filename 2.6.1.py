a=[int(input())]
while sum(a) != 0:
    a.append(int(input()))
suma=0
for i in range(len(a)):
    suma+=a[i]**2
print(suma)