def reverseLookup(__dict, value):  # определеяем функцию
    """
    Функция для возвращения ключей по заданному значению

    :param __dict: словарь
    :param value: значение, по которому будут возврщаться ключи
    :return: список ключей
    """
    keys = []
    for item in __dict.items():  # проходка по кортежам с ключом и значением
        if item[1] == value:  # если параментр значения равен значению словаря
            keys.append(item[0])  # добавлем ключ в список ключей
    return keys


dict_ = {1: 2,
         2: 2,
         3: 2,
         4: 1,
         5: 3,
         'value1': 2,
         'value2': 2}

print(reverseLookup(dict_, 0))
print(reverseLookup(dict_, 1))
print(reverseLookup(dict_, 2))
