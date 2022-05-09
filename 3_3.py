#3.Пользователь вводит Имя, Возраст и Город, сформировать приветственное сообщение путем форматирования 3-мя способами
#а) format
first_name = "Vadim"
last_name = "Malashkov"
age = 25
town = "Minsk"
text = 'Hello:) My name is {name} {last}! I am {age} years old! I live in {town} and I am happy!:D'.format(name=first_name, last=last_name, age=age, town=town)
print(text)

#б) f - форматирование
first_name = "Vadim"
last_name = "Malashkov"
age = 25
town = "Minsk"
text = f'hello {first_name} {last_name}! I am {age} years old. I live in {town}.'
print(text)

#в) %
name = "Vadim Malashkov"
age = 25
town = "Minsk"
квартира = 3
text = "Hy everybody:) My name is %s. I am %d years old. I live in %s. я проживаю на улице Янки Мавра %s " %(name, age, town, квартира)
print(text)