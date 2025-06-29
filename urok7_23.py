hours = int(input('Введите время: '))
if 0 <= hours < 8 or hours > 22 or 14 <= hours <= 15 or 10 <= hours <= 12 or 18 <= hours <= 20:
    print('Вы не можете получить посылку')
else:
    print('Вы можете получить посылку')
#Задача на получение посылки