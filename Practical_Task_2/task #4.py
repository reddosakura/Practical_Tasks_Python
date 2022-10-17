
namerow = ["Название", "$ Цена", "$ Цена со скидками"]
first_col = [f"Товар #{i}|" for i in range(1, 6)]  # генератор списков, хранит первую строчку матрицы с наименованиями товара
second_col = [4.95, 9.95, 14.95, 19.95, 24.95]
third_col = [round(i - i * 0.6, 2) for i in second_col]  # генератор списков, хранит цены со скидкой
tab = [first_col, second_col, third_col]  # матрица со всеми значениями
transposed_tab = [[tab[k][l] for k in range(len(tab))] for l in range(len(tab[0]))]  # транспонирование матрицы посредством итератора
transposed_tab.insert(0, namerow)  # вствляем в матрицу строчку с названиями столбцов


for i in transposed_tab:
    for j in i:
        print(j, end=" ")
    print()
