bank = int(input('Введите сумму на карте: '))
if bank >= 75000:
    bank -= 75000
    if bank < 5000:
        bank += 1000
        print('Сделана скидка!')
else:
    print('Недостаточно денег на счёте.')
print('Остаток денег на счёте:', bank)
print('Хорошего дня!')
#Задача на предоставление скидки