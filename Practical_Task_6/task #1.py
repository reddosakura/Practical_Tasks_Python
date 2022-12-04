import csv
from tabulate import tabulate
import os


def generateitem(_type: str, count: int, price: int, weight: int) -> dict:
    if not _type or not count or not price or not weight:
        raise Exception('Не все параметры были введены')
    return {'Type:': _type, 'Count:': count, 'Price, $:': price, 'Weight, kg:': weight}


if not os.path.exists('tab.csv'):
    data = []
    for i in range(int(input('Введите количесво типов: '))):
        try:
            data.append(generateitem(input('Введите тип: '), int(input('Введите количество товаров(число): ')),
                                     int(input('Введите цену($) всех товаров(число): ')),
                                     int(input('Введите массу(кг) всех товаров(число): '))))
        except ValueError:
            print('Введено неверное значение для параметра')
    with open('tab.csv', 'w') as f:
        writer = csv.DictWriter(
            f, fieldnames=list(data[0].keys()), quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in data:
            writer.writerow(d)


def main() -> None:
    global loadcapacity
    import sys

    # sys.path.remove('tab.csv')
    try:
        loadcapacity = int(input('Введите грузоподъемность контейнера: '))
    except ValueError:
        print('Введено не числовое значение')
    newtab = []
    with open('tab.csv') as tab:
        reader = csv.DictReader(tab)
        # print(list(reader))
        # print(tabulate(reader, headers='keys'))
        for i in list(reader):
            newtab.append({'Type: ': i['Type:'],
                           'Count:': 0 if int(i['Weight, kg:']) // int(i['Count:']) > loadcapacity else loadcapacity / (int(i['Weight, kg:']) / int(i['Count:'])),
                           'Price:': 0 if int(i['Weight, kg:']) // int(i['Count:']) > loadcapacity else (int(i['Price, $:']) // int(i['Count:'])) * (loadcapacity / (int(i['Weight, kg:']) / int(i['Count:']))),
                           'Weight:': loadcapacity
                           })

    print(tabulate(newtab, headers='keys'))


if __name__ == '__main__':
    main()
