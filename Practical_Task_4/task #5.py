import random


def generatesign():
    alphabet = list('абвгдеёжзиклмнопрстуфхцчшщыэюя')
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    signs = [f'{random.choice(alphabet).title()}'
             f'{random.choice(alphabet).title()}'
             f'{random.choice(alphabet).title()}'
             f'{random.choice(numbers)}'
             f'{random.choice(numbers)}'
             f'{random.choice(numbers)}',
             f'{random.choice(numbers)}'
             f'{random.choice(numbers)}'
             f'{random.choice(numbers)}'
             f'{random.choice(numbers)}'
             f'{random.choice(alphabet).title()}'
             f'{random.choice(alphabet).title()}'
             f'{random.choice(alphabet).title()}']
    return random.choice(signs)

print(generatesign())
