num_1, num_2, num_3 = int(input()), int(input()), int(input())
if num_1 == num_2 == num_3:
    print('3')
elif num_1 == num_2 or num_1 == num_3 or num_2 == num_3:
    print('2')
else:
    print('0')
#Задача на определение одинаковых чисел