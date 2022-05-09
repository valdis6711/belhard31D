a = int(input("Введите количество элементов списка: "))
b = []
for i in range(0, a):
    elem = int(input("Введите элемент списка: "))
    b.append(elem)
age = sum(b) / a
print("Среднее значение элементов списка",round(age, 3))