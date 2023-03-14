# Напишите программу для нахождения факториала числа. 
# Ваша программа должна запрашивать у пользователя число и выводить на экран его факториал.

number = int(input('Введите целое число больше ноля: '))
endNumber = 1

if number <= 0:
    print('Вы ввели ноль или число меньше ноля')
else:
    for everyNumber in range(1, number + 1):
        endNumber = endNumber * everyNumber
    print(endNumber)

