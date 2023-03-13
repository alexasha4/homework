time = int(input("Время: "))
price = int(input("Цена: "))
if time > 10 and time < 12:
    print(price / 2, time)
elif time > 20 and time < 22:
    print(price / 4, time)
else:
    print(price, time)
