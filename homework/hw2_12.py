tag = input("Введите тег: ").replace("<span>", "").replace("</span>", "").replace("&nbsp;", "").replace("P", "")
print(int(tag) + 1)
