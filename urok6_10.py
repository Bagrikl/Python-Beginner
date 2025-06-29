pirce1, price2, price3 = int(input('Введите первую цену: ')), int(input('Введите вторую цену: ')), int(input('Введите третью цену:' ))
sum = pirce1 + price2 + price3
if sum >= 10000:
     discount = sum * 10 / 100
     sum -= discount
     print(sum)
else:
    print(sum)
#Задача на определение скидки