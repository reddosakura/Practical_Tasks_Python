# a  = int(input())
# if a < 1:
#     raise Exception('Возбуждено исключение')
# else:
#     print('1a')

def simplenum(num):
    if num < 1:
        raise Exception('Введено значение меньше единицы')

    for i in range(1, num + 1):
        if i != num and i != 1 and num % i == 0:
            return False
    return True


print(simplenum(20))
print(simplenum(3))