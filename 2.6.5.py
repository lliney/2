q = int(input())
b = [[0 for i in range(q)] for j in range(q)]
count = q - 1 #количество проходов в одном напрвлении
n = 0 #счетчик, показывающий нам когда сменить направление
way = 0 # начальное направление вправо
x = 0
y = 0
i = 1 # начальное значение
while (i <= q * q):
    if (n == count):
        if (way == 3): # если завершен один круг, корректируем начальную позицию и направление
            way = 0
            y += 1
            x += 1
            count -= 2
        else: # меняем направление
            way += 1
        n = 0
    b[y][x] = i
    if (way == 0):  # right
        x += 1
    elif (way == 1):  # down
        y += 1
    elif (way == 2):  # left
        x -= 1
    elif (way == 3):  # up
        y -= 1
    n += 1
    i += 1
for i in range(q):
    for j in range(q):
        print(b[i][j], end=' ')
    print()