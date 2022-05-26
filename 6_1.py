#1
def binary(n):
    i = ''
    while n > 0:
        i = str(n % 2) + i
        n //= 2
    return i


while 1:
    n = int(input())
    if n != 0:
        print(binary(n))
    else:
        break