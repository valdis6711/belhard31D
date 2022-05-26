N = int(input("Введи число: "))
M = int(input("Введи число: "))
K = int(input("Введи число: "))
c = 0
while c < 5:
    if N % M == 0 and N / M > K:
        positive = N
        print(positive)
        c += 1
        N += 1
    else:
        N += 1