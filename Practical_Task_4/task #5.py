import random


def generatesign():
    """
    Функция генерирует знаки
    :return: (строка) номерной знак
    """
    alphabet = list('абвгдеёжзиклмнопрстуфхцчшщыэюя')  # список букв алфавита
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    signs = [f'{random.choice(alphabet).title()}'  # генерация первого номерного знака в старом формате
             f'{random.choice(alphabet).title()}'
             f'{random.choice(alphabet).title()}'
             f'{random.choice(numbers)}'
             f'{random.choice(numbers)}'
             f'{random.choice(numbers)}',
             f'{random.choice(numbers)}'  # генерация второго знака в новом формате
             f'{random.choice(numbers)}'
             f'{random.choice(numbers)}'
             f'{random.choice(numbers)}'
             f'{random.choice(alphabet).title()}'
             f'{random.choice(alphabet).title()}'
             f'{random.choice(alphabet).title()}']
    return random.choice(signs)  # случайный выбор знаков в списке из двух элементов


print(generatesign())
