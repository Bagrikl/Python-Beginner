income = int(input('Введите сумму заработка: '))
if income < 0:
    print('Ошибка, отрицательный доход')
elif income < 10000:
    tax =income * 13 / 100
    print('Сумма налога:', tax)
elif income < 50000:
    tax = income * 20 / 100
    print('Сумма налога:', tax)
else:
    tax = income * 30 / 100
    print('Сумма налога:', tax)
#Задача на нарастающий налог при увеличении заработка