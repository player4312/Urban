# Картеж незменяемая коллекция который хранит в себе изменяемые
tuple_ = 1, 2, 3, True, 'qweqe'
tuple_1 = 1, 2, 3, 4
tuple_2 = 1, 2, 3, 4
print(type(tuple_))
print(tuple_)
print(tuple_1)
print(tuple_2)

# Сопостовимость размеров занимаемой памяти
tuple_4 = 1, 2, 3, True, 'qweqe'
list_ = [1, 2, 3, True, 'qweqe']
print(tuple_4.__sizeof__())
print(list_.__sizeof__())

# Поддерживает сложение и умножения
tuple_5 = ([1, 2], 0) + (1, 2)
print(tuple_5)
tuple_5[0][0] = 2
print(tuple_5)
tuple_5 = ([1, 2], 0) * 3
print(tuple_5)