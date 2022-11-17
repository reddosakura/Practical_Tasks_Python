def taxi_tariff(distance):
    """
    Функция возвращает рассчитанную цена за тариф такси
    :param distance: расстояние в километрах
    :return: (число) цена услуги
    """
    return 4 + distance * 1000 // 140 * 0.25

print(f"Цена за услуги ${taxi_tariff(distance=int(input('Введите расстояние в км: ')))}")