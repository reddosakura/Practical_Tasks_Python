values = {  # словарь со списками, в которых будут хранится значения
    'pos': [],
    'negat': [],
    'null': []
}


def converttoint(__list):
    """
    Функция для сортировки списка с числами и строками. Если в списке находятся числа, в формате строк, они преводятся в
    тип данных int

    :param __list: список значений строк и чисел
    :return: список содержащий числа
    """
    for i in range(len(__list)):
        try:  # ловим исключение
            __list[i] = int(__list[i])  # переводим числа в тип данных int
        except ValueError:  # исключаем ошибку с типом данных
            pass

    return list(filter(lambda x: isinstance(x, int), __list))  # возвращаем список отфитрованный
    # с помощью функции filter и лямбда-высказывания проверяем принадлежность параметра к классу int
    # таким образом удаляем все лишние строковые значения


all_values = []
while (inp := input()) != '':
    all_values.append(inp)

for i in converttoint(all_values):
    if i < 0:  # если число отрицательное отправляем его в список отрицательных значений
        values['negat'].append(i)
    elif i == 0:  # если нулевое, то в список нулей
        values['null'].append(i)
    else:  # иначе в список положительных чисел
        values['pos'].append(i)

print(*sorted(values['negat']), *values['null'], *sorted(values['pos'], reverse=True), sep='\n')  # сортируем
# и выводим значения
