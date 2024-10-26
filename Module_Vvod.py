# Целые числа
print(5 + 5) # сумма
print(5 - 5) # вычетание
print(5 * 5) # умножение
print(5 / 5) # деление
print(5 // 5) # целочисленное деление
print(1234.56 % 10) # процентный остаток
print(5 ** 5) # возведение в степень
print(type(5.0)) # тип данных float с плавающей точкой
print(type(5)) # тип данных int целые числа

# Работа со строками int
print(type('hello world')) # тип данных int
print('hello "world"') # одинарные ковычки
print("hello 'world'") # двойные ковычки
print('hello, ' + 'world') # в строках только сложение
#print('1' + 1) ошибка

# Логический тип данных boolean
print(type(False), type(False)) # логический тип данных boolean
#print(True, False )
print(5 < 10, 5 > 10, 5 == 10, 5 <= 10, 5 != 10)
print( 5 != 5 and 5 < 10) # И строгий оператор
print( 5 != 5 or 5 < 10) # ИЛИ не строгий оператор

print(type(int('5')))