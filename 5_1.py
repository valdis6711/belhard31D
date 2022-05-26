while not (number := input()).isdigit():
    print('Оператор инвалид, повторите ввод')
number = int(number)

#c = 0
#for i in range(2, number+1, 2):
    #if c < 5:
        #c += 1
        #print(i, end=' ')
    #else:
        #print()
        #c = 1
        #print(i, end=' ')

for i in range(2, number+1, 10):
    for j in range(i, i+9, 2):
        if j <= number:
            print(j, end=' ')
    else:
        break
    print()