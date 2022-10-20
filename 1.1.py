'''1. Написать программу, которая переводит число из десятичной
системы счисления в двоичную или восьмеричную (по
указанию пользователя)'''

number = int(input('Введите число в десятичной системе счисления: '))
scale_of_notation = int(input('Введите целевую систему счисления: '))
final_number = '' #переменная содержит число, переведенное в другую систему счисления в строковом виде
number1 = number

if scale_of_notation==2:
    #перевод в двоичную систему счисления
    while number1 > 0:
        final_number = str(number1 % 2) + final_number #преобразование остатка от деления на 2 к строковому виду и соединение со строкой final_number
        number1 = number1 // 2
    print('Вывод: ', number, '->', final_number)
elif scale_of_notation==8:
    #перевод в восьмиричную систему счисления
    while number1 > 0:
        final_number = str(number1 % 8) + final_number #преобразование остатка от деления на 8 к строковому виду и соединение со строкой final_number
        number1 = number1 // 8
    print('Вывод: ', number, '->', final_number)
else:
    print('Ошибка: Введите корректную систему счисления')
        
        
        
    
    
