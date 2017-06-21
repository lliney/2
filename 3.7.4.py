x=0
y=0
n=int(input())
for i in range(n):
    my_str=[str(j) for j in input().split()]
    if my_str[0]=='север':
        y+=int(my_str[1])
    elif my_str[0]=='юг':
        y-=int(my_str[1])
    elif my_str[0]=='восток':
        x+=int(my_str[1])
    elif my_str[0]=='запад':
        x-=int(my_str[1])
print(x, end=' ')
print(y)