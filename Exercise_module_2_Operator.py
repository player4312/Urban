one = int(input('Program: '))
two = int(input('Program: '))
three = int(input('Program: '))
if one == two and one == three:
    print('Все три целых числа равны между собой')
elif one == two or one == three or two == three:
    print('Только два числа равны между собой')
else:
    print('Все не равны')