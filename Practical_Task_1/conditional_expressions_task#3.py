"""Даны три переменные вещественного типа: A, B, C. Если их значения
упорядочены по возрастанию, то удвоить их; в противном случае
заменить значение каждой переменной на противоположное. Вывести
новые значения переменных A, B, C
"""

input_num_a = float(input('Введите число А: '))  # ввод числа А
input_num_b = float(input('Введите число В: '))  # ввод числа В
input_num_c = float(input('Введите число С: '))  # ввод числа С
# Функция float переводит возвращенное строковое значение из функции input в вещественное значение

if input_num_a < input_num_b < input_num_c:  # сравнение значений переменных
    print(f'Результат: А = {input_num_a * 2}; B = {input_num_b * 2}; C = {input_num_c * 2}')  # если значения
    # переменных введены по возрастанию, то удваиваем их
else:  # иначе выводим сообщение и противоположные значения переменных
    print(f'Результат: А = {-input_num_a}; B = {-input_num_b}; C = {-input_num_c}')
