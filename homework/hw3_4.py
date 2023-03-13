products = input("Категория товара: ")
price = int(input("Цена: "))
if products == "продукты":
    if price < 100:
        print("Попробуйте нашу выпечку!")
    elif price >= 100 and price < 500:
        print("Как насчет орехов в шоколаде?")
    elif price >= 500:
        print("Попробуйте экзотические фрукты!")
else:
    print("Загляните в товары для дома!")
