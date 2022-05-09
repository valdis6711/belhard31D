n = int(input("Введите количество элементов списка: "))
a = []
for i in range(0, n):
    elem = int(input("Введите элемент списка: "))
    a.append(elem)
age = sum(a) / n
print("Среднее значение элементов списка",round(age, 3))
