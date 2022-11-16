def delivery(goodscount):
    return(10.95 + ((goodscount - 1) * 2.95))


print(f"Цена доставки ${delivery(int(input('Введите количество товаров: ')))}")