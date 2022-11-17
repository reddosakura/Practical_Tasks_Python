def greatcomdiv(num1, num2):
    """
    Функция для определения наибольшего обшего делителя
    :param num1: первое число
    :param num2: второе число
    :return: (число) наибольший общий делитель
    """
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return num1 + num2


def reducfraction(numer, denom):
    """
    Функция для сокращения дроби
    :param numer: (число) числитель
    :param denom: (число) знаменатель
    :return: (кортеж) кортеж с новым числителем и знаменателем
    """
    return numer // greatcomdiv(numer, denom), denom // greatcomdiv(numer, denom)


print(reducfraction(numer=int(input('Введите числитель')), denom=int(input('Введите знаменатель'))))
