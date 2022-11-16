def taxi_tariff(distance):
    return 4 + distance * 1000 // 140 * 0.25

print(f"Цена за услуги ${taxi_tariff(int(input('Введите расстояние в км: ')))}")