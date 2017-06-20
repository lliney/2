operaciya = input()
if operaciya=='треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a+b+c)/2
    print((p*(p-a)*(p-b)*(p-c))**0.5)
elif operaciya=='прямоугольник':
    a = int(input())
    b = int(input())
    c = float(a * b)
    print(c)
elif operaciya == 'круг':
    a = int(input())
    print((a * a * 3.14))