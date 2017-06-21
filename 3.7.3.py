dic1={}
dic2={}
d=int(input())
for i in range(d):
    slovo = input()
    slovo=slovo.lower()

    dic1[slovo]=slovo
l=int(input())
for i in range(l):
    a = [str(j).lower() for j in input().split()]
    for slovo2 in a:
        dic2[slovo2]=slovo2
for j in dic2:
    if j not in dic1:
        print(j)