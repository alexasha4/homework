price1 = int(input(""))
price2 = int(input())
price3 = int(input())
if price1 < price2 < price3:
    print("Акция! К оплате:", (price1 + price2 + price3) / 2)
elif price3 > price2 > price1:
    print("Акция! К оплате:", (price1 + price2 + price3) / 3)
else:
    print("К оплате:", (price1 + price2 + price3))
