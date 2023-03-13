games = []
game = input('Введите название игры: ')
while game !='0':
    if game in games:
        print('Эта игра уже в списке')
    else:
        games.append(game)
        print('Игра добавлена')
    game = input('Введите название игры: ')
games.sort()
print(games)












