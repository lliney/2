a= int(input())
if a%100==11 or a%100==12 or a%100==13 or a%100==14:
    print(a, 'программистов')
elif a%10==1:
    print(a, 'программист')
elif a%10==2 or a%10==3 or a%10==4:
    print(a, 'программиста')
else:
    print(a, 'программистов')