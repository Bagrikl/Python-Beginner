a, b, c = int(input()), int(input()), int(input())
if a > b and a > c:
    print('Максимальное число:', a)
elif b > a and b > c:
    print('Максимальное число:', b)
elif c > a and c > b:
    print('Максимальное число:', c)
else:
    print('Числа равны.')
#Задача на максимальное число
