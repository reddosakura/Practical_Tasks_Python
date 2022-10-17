user_input = input()
print(*[user_input[i].lower() if i % 2 == 0 else user_input[i].upper() for i in range(len(user_input))], sep='')  #
#итератор с тернарным условием, если индекс элемента введенной строки делется на 2 без остатка, т.е. четный, то переводим в нижний регистр, иначе переводим в верхний