numbers = int(input("3-х значное число"))
a = numbers % 10
b = numbers // 100
c = numbers // 10 % 10
print(sum([a, b, c]))