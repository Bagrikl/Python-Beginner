player, owner = int(input('Число игрока: ')), int(input('Число владельца: '))
sum = player + owner
if player >= owner:
    player -= owner
    print('Игрок платит.')
else:
    print('Владелец платит.')
    print('Сумма =', sum)
print('Игра окончена.')
#Задача с игрой в кубики