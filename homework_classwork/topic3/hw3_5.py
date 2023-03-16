n = input()
lst = list(map(int, list(n)))

if int(n[-1]) % 2 == 0 and sum(lst) % 3 == 0:
    print(True)
else:
    print(False)
