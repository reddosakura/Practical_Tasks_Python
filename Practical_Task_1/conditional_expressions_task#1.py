"""Дано целое число. Если оно является положительным, то прибавить к
нему 1; в противном случае не изменять его. Вывести полученное число.
"""

input_number = int(input('Введите число: '))  # Ввод числа с клавиатуры.
# int преобразует данные введенные с клавиатуры из строкового в челочисленный тип данных

if input_number > 0:  # условие, если введенное число больше нуля
    print('Введено положительное число, к нему прибавлена единица. Результат:', input_number + 1)
    # Вывод результата, если число положительное, то прибавить к нему единицу
else:
    print('Введено отрицательное число. Результат:', input_number)  # Иначе вывод числа без изменений
