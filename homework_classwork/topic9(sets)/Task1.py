"""
Даны два списка чисел. Выведите все числа, которые входят как в первый, так и во второй список в порядке возрастания.
"""
list1 = [1,2,3,4,5,6]
list2 = [4,16,1,3,8,2]
list1_1 = set(list1)
list2_2 = set(list2)
list = (list1_1 | list2_2)
print(list)


