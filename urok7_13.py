position, grants = int(input('Введите место в списке: ')), int(input('Введите количество баллов: '))
if position <= 10 and position > 0 and grants >= 290:
    print('Вы поступили и получили стипендию!')
elif position > 10:
    print('Вы не поступили.')
else:
    print('Вы поступили, но не получили стипендию.')
#Задача на поступление