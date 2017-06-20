a = float(input())
b = float(input())
operaciya = input()
if operaciya=='+':
    print(a+b)
elif operaciya=='-':
    print(a - b)
elif operaciya == '*':
    print(a * b)
elif operaciya == '/':
    if b==0:
        print('Деление на 0!')
    if b!=0:
        print(a/b)
elif operaciya == 'mod':
    if b != 0:
        print(a%b)
    else:
        print('Деление на 0!')
elif operaciya == 'pow':
    print((a**b))
elif operaciya == 'div':
    if b != 0:
        print((a//b))
    else:
        print('Деление на 0!')