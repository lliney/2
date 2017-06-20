a=int(input())
b=int(input())+1
sum =0
i=0
for j in range(a,b):
    if j%3==0:
        sum+=j
        i+=1
print(sum/i)