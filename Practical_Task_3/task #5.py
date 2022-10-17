inp_list = []
while (num := int(input())) != 0:  # также как и в предыдущей программе заполняем список
    inp_list.append(num)

print('Отсортированные значения:', *sorted(inp_list, reverse=True), sep='\n')  # выводим сортированные значения,
# указывая значение true параметра reverse функции sorted
