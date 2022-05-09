#1. Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами
#а)
first_name = "Vadim"
last_name = "Malashkov"
age = 25
town = "Minsk"
text = f'hello {first_name} {last_name}! I am {age} years old. I live in {town}.'
words = text.split(' ')
text = ' --'.join(words)
print(text)

#б) 
first_name = "Vadim"
last_name = "Malashkov"
age = 25
town = "Minsk"
text = f'hello {first_name} {last_name}! I am {age} years old. I live in {town}.'
words = text.split(' ')
text = '  '.join(words)
text_2 = text.replace(' ', '-').replace('Hello', 'Goodbye')
print(text)
print(text_2)
