"""Создайте словарь с количеством элементов не менее 5-ти.
Поменяйте местами первый и последний элемент объекта.
Удалите второй элемент. Добавьте в конец ключ «new_key» со значением «new_value».
Выведите на печать итоговый словарь. Важно, чтобы словарь остался тем же (имел тот же адрес в памяти).
"""
some_dict = {'colour1': 'yellow', 'colour2': 'blue', 'colour3': 'green', 'colour4': 'pink', 'colour5': 'purple'}

del some_dict['colour2']
some_dict['new_key'] = 'new_value'
print(some_dict.values())

