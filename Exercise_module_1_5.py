# 1st program
immutable_var = 5, 8, 'kek', 'bob'
print('Immutable tuple:', immutable_var)

# 2st program / Неизменяемая коллекция, т.е не поддерживает обращение по элементам
# Immutable_var[0] = 10
# print(immutable_var)

# 3st program
mutable_list = 4, 'list', False
mutable_list = ((4, 'list', False) + (2, 'kak je tak')) * 2
print('Mutable list:', mutable_list)