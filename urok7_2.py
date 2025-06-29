wallet = int(input('Введите количество денег: '))
cheese = 60
icecream = 20
if wallet >= cheese:
    wallet -= cheese
    print('На сыр денег хватает.')
    if wallet >= icecream:
        print('На мороженное тоже!')
    else:
        print('На мороженное не хватило.')
else:
    print('Денег не хватает.')
#Задача на покупки в магазине