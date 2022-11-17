
def simplenum(num):
    """
    Функция проверяет числовое значение, является ли оно простым или нет
    :param num: число
    :return: Булевое значение
    """
    if num < 1:
        raise Exception('Введено значение меньше единицы')

    for i in range(1, num + 1):
        if i != num and i != 1 and num % i == 0:
            return False
    return True


print(simplenum(num=int(input("Введите число"))))
