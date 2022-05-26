N = input('введи число: ')
M = input('введи число: ')
K = input('введи число: ')
counter = 0
while counter < 5:
    if N % M == 0 and N / M > K:
        positive = N
        print(positive)
        counter += 1
        N += 1
    else:
        N += 1





