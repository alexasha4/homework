weight = float(input("Ширина поверхности: "))
length = float(input("Длина поверхности: "))
paint = float(input("Расход краски: "))
v = int(input("Объем банки: "))
percent = int(input("Процент запаса: "))

s = weight * length
n = (s / paint) + (s / paint) * (percent / 100) # кол-во литров
k = (n // v) + 1  # кол-во банок
lost = (k * v) - n

print(round(s, 2), round(n, 2), k, round(lost, 2))

