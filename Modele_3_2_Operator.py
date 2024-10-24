# name = input('Введи ваше имя: ')
# if name == 'Константин':
#     print('Здравствуйте, админитсратор: ', name)
# if name == 'Екатерина':
#     print('Здравствуйте, пользователь')
# else:
#     print('Привет', name)

number = int(input('Введите число: '))
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuz')
elif number % 3 == 0:
    print('Fizz')
elif number % 5 ==0:
    print('Buzz')
else:
    print('NO')