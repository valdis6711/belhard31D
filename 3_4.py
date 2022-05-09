#4. Пользователь вводит 3 числа, сказать сколько из них положительных и сколько отрицательных
a = int(input('Введите значение a = '))
b = int(input('Введите значение b = '))
c = int(input('Введите значение c = '))
summ = 0;
if a > 0:
    summ = summ + 1
if b > 0:
    summ = summ + 1
if c > 0:
    summ = summ + 1
print('Количество положительных чисел: ', summ)

a = int(input('Введите значение a = '))
b = int(input('Введите значение b = '))
c = int(input('Введите значение c = '))
summ = 0;
if a < 0:
    summ = summ + 1
if b < 0:
    summ = summ + 1
if c < 0:
    summ = summ + 1
print('Количество отрицательных чисел: ', summ)