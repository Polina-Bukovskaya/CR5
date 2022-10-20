'''1. Написать программу, которая переводит число из десятичной
системы счисления в двоичную или восьмеричную (по
указанию пользователя)'''
#Создаём функцию, содержащую алгоритм перевода числа из десятичной в введенную пользователем систему счисления
def convertation (number, scale_of_notation):
    number1 = number
    final_number = ''
    while number1 > 0:
        final_number = str(number1 % scale_of_notation) + final_number #преобразование остатка от деления на основание системы счисления к строковому виду и соединение со строкой final_number
        number1 = number1 // scale_of_notation
    print('Вывод:', number, '->', final_number)

#Задание пользователем числа и системы счисления
number = int(input('Введите число в десятичной системе счисления: '))
scale_of_notation = int(input('Введите целевую систему счисления: '))

#Вызов функции convertation при 2 и 8 системе счисления
if scale_of_notation == 2 or scale_of_notation ==8:
    convertation (number, scale_of_notation)
else:
    print('Ошибка: Введите корректную систему счисления')
