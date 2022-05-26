first_number = int(input('1-е число: '))
user_actions = input('действие: ')
second_number = int(input('2-е действие: '))
if user_actions == '-':
    print(first_number - second_number)
elif user_actions == '*':
    print(first_number * second_number)
elif user_actions == '+':
    print(first_number + second_number)
elif user_actions == '/':
    print(first_number / second_number)
elif user_actions == '**':
    print(first_number ** second_number)
elif user_actions == '//':
    print(first_number // second_number)
elif user_actions == '%':
    print(first_number % second_number)


    # - * + / % ** //