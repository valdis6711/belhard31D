def check(string, ch):
    if not string:
        return 0
    elif string[0] == ch:
        return 1 + check(string[1:], ch)
    else:
        return check(string[1:], ch)
vadim = input("Введите строку:")
ch = input("Введите букву для проверки:")
print("Количество вхождений:")
print(check(vadim, ch))



