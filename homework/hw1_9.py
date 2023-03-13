numbers = int(input("число"))
a = numbers // 100
c = numbers % 10 * 100
b = numbers // 10 % 10 * 10
print(a + b + c)
