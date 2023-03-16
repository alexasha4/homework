"""
Напишите программу печатающую скидку на поездку в зависимости от набранных баллов.
Программа должна запрашивать количество набранных баллов и печатать сообщение «Ваша скидка:» и скидку:
— от 0 до 49 баллов — «Скидка 10%»;
— от 50 до 99 баллов — «Скидка 15%»;
— от 100 баллов и выше — «Скидка 20%».

Примечание. Наличие функции является обязательным. Функция должна принимать количество набранных баллов.
"""


def amount_score():
    score = int(input('Введите балл: '))
    while score != 0:
        if score >= 1 and score <= 49:
            return 10
        elif score >= 50 and score <= 99:
            return 15
        elif score == 100:
            return 20
        else:
            return 0
print('Скидка на поезку(%): ', amount_score())
