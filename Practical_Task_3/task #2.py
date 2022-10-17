import datetime  # импортируем библиотеку по работе с датами

dictionary = {  # словарь, в котором хранятся фамилии, даты рождений и адреса электронных почт
    "Петров": {'21.02.2006', "example1@email.com"},
    "Иванов": {'27.02.1998', 'example2@email.com'},
    "Сидоров": {'13.01.1978', 'example3@email.com'},
    "Ивушкин": {'01.09.1988', 'example4@email.com'},
    "Миллер": {'08.02.1990', 'example5@email.com'},
    "Дикоян": {'26.02.2001', 'example6@email.com'},
    "Болтиков": {'10.08.2077', 'example7@email.com'}
}

key = '23.06.2000'  # ключ сортировки


def sortnames(iter_dict, date_key):
    """
    Функция для сортировки фамилий из словаря по дате рождения

    :param iter_dict: словарь с множествами, ключами которого являются фамилии
    :param date_key:  ключ сортировки в виде даты
    :return: итерируемый объект сордержащий фамилии
    """
    tup_list = []  # список кортежей, в которых будут хранится фамилий и даты рождений
    lastnames = []  # список в который будут помещаться сортированные фамилии
    for i in iter_dict:
        for j in iter_dict[i]:
            if not "email" in j:  # если элемент множетства не является адресом электронной почты
                tup_list.append((i, datetime.datetime.strptime(j, '%d.%m.%Y')))  # добавляем в список кортежей,
                # кортеж с парой: фамили, дата рождения

    for k in tup_list:
        if datetime.datetime.strptime(date_key, '%d.%m.%Y') < k[1]:  # условие, если ключ-дата раньше даты рождения
            lastnames.append(k[0])  # добавляем фамилии в список фамилий

    yield lastnames


for i in sortnames(dictionary, key):
    print(*i, sep='\n')
