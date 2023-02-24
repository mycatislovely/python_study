from random import randint, shuffle

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' 
punctuation = '!#$%&*+-=?@^_.'
ambiguous = 'il1Lo0O'


def input_true_false(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer == 'да':
            return True
        if answer == 'нет':
            return False
        else:
            print('Надо ввести: да или нет.')


def generate_password(length, chars_list):
    if length < 1:
        raise Exception ('Длина пароля < 1.') # Выброс исключения
    if len(chars_list) < 1:
        raise Exception ('Количество типов символов < 1.') # Выброс исключения 
    if len(chars_list) > length:
        raise Exception ('Количество типов символов > длины пароля.') # Выброс исключения         
    password = []
    for chars in chars_list:
        password.append(chars[randint(0, len(chars) - 1)])
    for _ in range(length - len(chars_list)):
        chars = chars_list[randint(0, len(chars_list) - 1)]
        char = chars[randint(0, len(chars) - 1)]
        password.append(char)
    shuffle(password)
    return ''.join(password)
        

chars_list = []
num = int(input('Сколько паролей нужно? '))
length = int(input('Какая длина одного пароля? '))
if input_true_false(f'Включать цифры ({digits})? [да/нет]: '):
    chars_list.append(set(digits))
if input_true_false(f'Включать прописные буквы ({uppercase_letters})? [да/нет]: '):
    chars_list.append(set(uppercase_letters))
if input_true_false(f'Включать строчные буквы ({lowercase_letters})? [да/нет]: '):
    chars_list.append(set(lowercase_letters))
if input_true_false(f'Включать символы пунктуации ({punctuation})? [да/нет]: '):
    chars_list.append(set(punctuation))
if input_true_false(f'Исключать неоднозначные символы ({ambiguous})? [да/нет]: '):
    to_remove = set(ambiguous)
    for i in range(len(chars_list)):
        chars_list[i] = chars_list[i] - to_remove
chars_list = [list(el) for el in chars_list]

        
for _ in range(num):  
    print(generate_password(length, chars_list))  
    
