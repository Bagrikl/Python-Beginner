client, seller, salary = int(input('Количество клиентов: ')), int(input('Количество продавцов: ')), int(input('Количетсво зарплаты: '))
if client / seller > 4:
    print('Мало продавцов')
    if salary < 20000:
        salary +=2000
else:
    print('Продавцов достаточно')
print('Зарплата продавцов:', salary)
#Задача на продавцов