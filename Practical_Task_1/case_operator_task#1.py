""" Единицы массы пронумерованы следующим образом: 1 — килограмм,
2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер
единицы массы (целое число в диапазоне 1–5) и масса тела в этих
единицах (вещественное число). Найти массу тела в килограммах.
"""

mass_units = input('Введите номер единицы массы: ')  # ввод номера единицы массы
weight = int(input('Введите значение массы: '))  # ввод значения массы
match mass_units:  # вывод конвертированной массы в соответсвии с введенной единицы
    case '1':  # если введена единица
        print(f'Результат в килограммах: {weight}кг')  # вывод результата в килограммах
    case '2':  # если введен номер два, перевод из миллиграмм в кг
        print(f'Результат в киллограммах: {weight / 10 ** 6}')
    case '3':  # если введен номер три, перевод из грамм в кг
        print(f'Результат в киллограммах: {weight / 1000}')
    case '4':  # если введен номер четыре, перевод из тонн в кг
        print(f'Результат в киллограммах: {weight * 1000}')
    case '5':  # если введен номер пять, перевод из центнеров в кг
        print(f'Результат в киллограммах: {weight * 100}')
    case _:  # если присутствует посторонний ввод
        print('Введенное значение не является номером единицы массы')
