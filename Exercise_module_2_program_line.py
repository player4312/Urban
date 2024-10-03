#1st program
my_string = 'Сколько символов в строке?:'
end = 'Если ввел 24, то это верно!'
number = len(my_string) - my_string.count(' ')
print('Всего символов в строке', number)
print(input(my_string))
print(end)

#2st program
print('Сколько символов в строке?:' .upper())
print('Сколько символов в строке?:' .lower())
print('Сколько символов в строке?:' .replace(' ',''))
print(my_string[0])
print(my_string[26])