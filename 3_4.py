#a = int(input('введите число: '))
#if a % 2:
    #print('odd')
#else
    #print('even')

#вводится строка, вывести уникальные символы из этой строки
# 1 вариант
#string = 'malashkov vadim aleksandrovich'
#unique = []
#for i in string[::]:
    #if i not in unique:
       # unique.append(i)
#print(len(unique))

# 2 вариант

#вводится строка, вывести уникальные символы из этой строки
#text = input('введи строку: ')
#for symbol in text:
    #if text.count(symbol) == 1:
        #print(symbol)

#n = 5
#i = 1
#while i <= n:
    #print(i**2)
    #i += i + 1

#i = 1

#while True:
    #if i == 128:
        #break
    #i += 1
#print(i)

#i = 1

#while True:
    #i += 1
    #if i % 2:
        #continue
    #print(i)


 #вводится слово, необходимо определить является ли оно полиндромом
#text = input().lower().replace(' ', '')
#n = int(input("input n: "))
#s = str(n)
#l = len(s)
#for i in range(l//2):
    #if s[i] != s[-1-i]:
       #print("It's not palindrome")
       #break
#else:
    #print("It's palindrome")
#ser_word = input("введи слово: ")
#user_word = user_word.lower().replace(" ", "")
#if user_word == user_word[::-1]:
    #print("палиндром")
#else:
    #print(" не палиндром")'
#правильная
#text = input().lower().replace(' ', '')
#result = 'палиндром' if text == text[::1] else'не палиндром'
#print(result)

 #вводится текст, подсчитать количество гласных и согласных букв
#мой вариант
#word = "malashkov vadim"
#vowels = 0
#consonants = 0
#for i in word:
    #letter = i.lower()
    #if letter == "a" or letter == "e" or\
       #letter == "i" or letter == "o" or\
       #letter == "u" or letter == "y":
        #vowels += 1
    #else:
        #consonants += 1
#print("Vowels %i\nConsonants %i" % (vowels, consonants))

#правильный
#text = input().lower()
#vowels_count = 0
#consonants_count = 0
#vowels = 'fdgnnfdчапоапта'
#for symbol in text:
    #if symbol.isalpha():
        #if symbol  in vowels:
#?        #if symbol in vowels:
            #vowels_count +=1
        #else:
            #consonants_count += 1

#print(f'{vowels_count=} {consonants_count=}')

try:
    a = int(input())
    b = int(input())
    c = a / b
except ValueError:
    print('')
    print('Вы ввели не число!')
except ZeroDivisionError:
    print('делить на 0 можно')
except KeyboardInterrupt:
    print('закрыли через Ctrl+C')
import sys
sys.exit(0)
