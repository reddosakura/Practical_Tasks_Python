def delivery(goodscount):
    """
    Функция для рассчета цены доставки
    :param goodscount: (число) количество товарод
    :return: (число) цена доставки
    """
    return(10.95 + ((goodscount - 1) * 2.95))


print(f"Цена доставки ${delivery(goodscount=int(input('Введите количество товаров: ')))}")