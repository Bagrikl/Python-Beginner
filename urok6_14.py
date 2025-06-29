hours, credit, comida = int(input('Введите количество часов: ')), int(input('Введите остаток от кредита: ')), int(input('Введите количество денег на еду: '))
salary = (200 * hours / (2**3)) + hours
if salary >= credit + comida:
    print('Часов хватает, отдыхай')
else:
    print('Часов не хватает, работай')
#Задача на вычисление зарплаты
