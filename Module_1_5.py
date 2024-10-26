#Замена первого элемента
food = ['apple', 'coconut', 'banana', 'peach']
print(food[0])
food[0] = 'kek'
print(food)

#Добавление элемента с другим типом данных
food = ['apple', 'coconut', 'banana', 'peach']
food.append(True) #позволяет добавить элемент в конец списка
food.append(1)
food.append('prosto tak')
food.extend('kuda') #перебор элементов в конце списка
print(food)
food.extend(['kuda', 2]) #добавленная строка сама стала элементом последовательности
print(food)

#Удалить из списка
food.remove('banana') #удаление из списка
print(food)

#Проверка, есть ли в списке указанный элемент
print('kuda' in food)
print('kuda' not in food)