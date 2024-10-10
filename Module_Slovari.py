# Словари
from Module_2_Kartej import list_

phone_book = {'kto tam': 1232132132, 'tru': 56767658767}
print(phone_book['kto tam']) # выводит по ключу
phone_book['kto tam'] = 354342 # заменяет значение в ключе
phone_book['qeqe'] = 12356519099 # ранее не сущ. список, он добавится
del phone_book['kto tam'] # удаление
phone_book.update({'shasa': 655443546,
                   'lex': 123213123444}) # обновление ключей
print(phone_book)

# Вывод опреленное значение по ключу / не создаст значение если его нет
print(phone_book.get('lex'))
print(phone_book.get('wasd', 'Обознался братишка')) # пишет "None" по умолчанию если нет текста

# Удаление ключа и возвращение ему соответствующее значение
a = phone_book.pop('tru') # сохраняется в переменной
print(phone_book)
print(a)

# Получение списка ключей
print(phone_book.keys())
# Получение значений из словаря
print(phone_book.values())
# Получение ключ/значние парой
print(phone_book.items())

# Множества, хранит уникальные значения / не содержит повторяющиеся элементы
set_ = {1, 2, 3, 4, 5, 1, 2, 3, 'str', True, (1, 2, 3)}
print(set_)
list_ = [1, 2, 3, 1, 2, 3] # пример
list_ = set(list_)
print(list_)
print(list_.discard(1)) # или можно использовать remove
print(list_.add(6)) # или добвить
print(list_)