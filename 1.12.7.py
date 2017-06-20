a = int(input())
a1 = a//100000
a=a%100000
a2=a//10000
a=a%10000
a3=a//1000
a=a%1000
a4=a//100
a=a%100
a5=a//10
a=a%10
a6=a
if (a1+a2+a3)==(a4+a5+a6):
    print('Счастливый')
else:
    print('Обычный')