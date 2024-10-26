one = int(input('Первое целое число: '))
two = int(input('Второе целое число: '))
three = int(input('Третье целое число: '))
if one == two and one == three:
    print('Все три целых числа равны между собой')
elif one == two or one == three or two == three:
    print('Только два целых числа равны между собой')
else:
    print('Все целые числа не равны')