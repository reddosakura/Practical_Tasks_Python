inp_list = []
while (num := int(input())) != 0:  # заполнение списка значений, пока не будет введен ноль
    inp_list.append(num)


print('Введенные значения:', *inp_list, sep='\n')  # выводим введенные значения
print("Отсортированные значения:", *sorted(inp_list), sep='\n')  # выводим сортированные значения