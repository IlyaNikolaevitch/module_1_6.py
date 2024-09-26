my_dict = {'Иван': 1990, 'Сергей': 1995, 'Ирина': 2000}
print(my_dict)
print(my_dict.get('Сергей'))
my_dict['Николай'] = 1981
print(my_dict)
my_dict.update({'Петр': 2001, 'Наталья': 1985})
del my_dict['Ирина']
print(my_dict.get('Ирина'))
print(my_dict)
my_set = {1,2,3,4,1,4,2,2, 'Вишня', True, 'Слива', 'Вишня', True}
print(my_set)
my_set.update({10,'Яблоко'})
my_set.remove(4)
print(my_set)
