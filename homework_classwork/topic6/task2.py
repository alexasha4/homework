word = input('Введите слово: ').lower()
word1 = word[::-1]
if word == word1:
    print('палиндром')
else:
    print('не палиндром')



