expirience = int(input('Введите количество очков опыта: '))
if expirience >= 1000 and expirience < 2500:
    print('У вас второй уровень!')
elif expirience >= 2500 and expirience < 5000:
    print('У вас третий уровень!')
elif expirience >= 5000:
    print('У вас четвёртый уровень!')
else:
    print('У вас первый уровень!')
#Задача на количество опыта до 4 лвл