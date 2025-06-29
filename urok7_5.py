coin_1, coin_2, coin_3 = int(input()), int(input()), int(input())
if coin_1 == coin_2:
    print('Фальшивая монета -', coin_3)
elif coin_1 == coin_3:
    print('Фальшивая монета -', coin_2)
else:
    print('Фальшивая монета -', coin_1)
#Задача на фальшивую монету, где две монеты одинаковы