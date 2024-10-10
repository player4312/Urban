# 1st program

my_dict = {'Mari': 1999, 'Kuzya': 2000}
print('Dict:', my_dict)
print('Existing value:', my_dict.get('Mari'))
print('Not existing value:', my_dict.get('Joe'))
my_dict.update({'Alex': 2005,
'Mila': 1974})
del my_dict['Mari']
print('Modified dictionary:', my_dict)

# 2st program
my_set = {1, 1, 'str', 'str', False, False, (1, 2, 3.4), (1, 2, 3.4) }
print('Set:', my_set)
my_set.add(6)
my_set.add('qwe')
my_set.remove(1)
print('Modified set:', my_set)