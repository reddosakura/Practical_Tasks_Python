import csv
from tabulate import tabulate
import os


def generateitem(number: str, carmodel: str, breaking: str) -> dict:
    """
    Функция генерирует строчку таблицы
    :param number: Номер машины(строка)
    :param carmodel: Марка машины(строка)
    :param breaking: Неисправность(строка)
    :return: словарь с заполненными значениями
    """
    if not number or not carmodel or not breaking:
        raise Exception('Не все параметры были введены')
    return {'carnumber': number, 'carmodel': carmodel, 'breaking': breaking}


if not os.path.exists('cars.csv'):
    data = []
    for i in range(int(input('Введите количесво автомашин: '))):
        try:
            data.append(generateitem(input('Введите номер машины: '), input('Введите марку машины: '),
                                     input('Введите неисправность: ').upper()))
        except ValueError:
            print('Введено неверное значение для параметра')
    with open('cars.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(
            f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in data:
            writer.writerow(d)


def main() -> None:
    """
    Основная функция
    :return:
    """
    file = csv.reader(of := open('cars.csv'))  # открытие файла
    tab = list(file)

    del tab[0]  # удаляем первую строчку
    print('Таблица с автомашинами, идеющими неисправности:')
    print(tabulate([_ for _ in list(filter(lambda x: x, tab)) if _[-1] != 'ОТСУТСТВУЕТ'], headers=['Car number:', 'Car model:', 'Breaking:']))  # фильтруем и выводим таблицу по неисправностям
    of.close()  # закрытие файла


if __name__ == '__main__':
    main()