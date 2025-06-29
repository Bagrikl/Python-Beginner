income = int(input('Введите свой доход: '))
if income < 10000:
    income *= 13 / 100
    print('Налог:', income)
elif income < 50000 and income > 10000:
    income = 0.2 * (income - 10000) + 0.13 * 10000
    print('Налог:', income)
else:
    income = 0.3 * (income - 50000) + 0.2 * (50000 - 10000) + 0.13 * 10000
    print('Налог:', income)
#Задача на расчёт прогрессивного налога