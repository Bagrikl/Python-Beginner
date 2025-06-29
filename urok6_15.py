#mileage - пробег
mileage, num = int(input('Введите пробег: ')), int(input('Введите число текущего дня: '))
n = (mileage % 10) + (mileage % 100 // 10) + (mileage % 1000 // 100)
if mileage < 100:
    print('Число должно быть трёхзначным!')
if n > num:
    print('Сломалось')
else:
    print('Сегодня работает')
print(mileage)
#Задача на сломанный циферблат