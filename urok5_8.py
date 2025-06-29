krug = 100
sportik_1, sportik_2, sportik_3 = int(input('Введите количество метров:')), int(input('Введите количество метров:')), int(input('Введите количество метров:'))
distance_1, distance_2, distance_3 = sportik_1 % krug, sportik_2 % krug, sportik_3 % krug
quantity_1, quantity_2, quantity_3 = sportik_1 // 100, sportik_2 // 100, sportik_3 // 100
print('Количество метров с очередного круга:', str(distance_1) + ',', str(distance_2) + ',', str(distance_3) + '.')
print('Количество кругов:', str(quantity_1) + ',', str(quantity_2) + ',', str(quantity_3) + '.')
#Задача на количество пройденных кругов и количество метров с нового круга для каждого спортсмена
