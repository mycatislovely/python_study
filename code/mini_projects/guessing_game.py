from random import randint


def to_number(s, n_max=0):
    if not s.isdigit():
        return 0
    n = int(s)
    if n_max == 0 or n <= n_max:
        return n
    return 0
    
    
def play(n):
    d = randint(1, n)
    print(f'Задумано целое число от 1 до {n}. Угадывайте...')
    count = 0
    while True:
        s = input("Введите ваше предположение: ") 
        i = to_number(s, n) 
        if i == 0:
            print(f'А может быть все-таки введете целое число от 1 до {n}?')
            continue
        count += 1   
        if i > d:
            print('Ваше число больше загаданного, попробуйте еще разок')
        elif i < d:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            print(f'Количество попыток: {count}')
            break    

        
another_game = False
print('Добро пожаловать в числовую угадайку')
while True:
    if another_game:
        print()
        print('Играем ещё раз?')
    s = input("Введите целое число больше нуля\n(или что-то иное для завершения): ") 
    n = to_number(s) 
    if n > 0:
        play(n)
    else:
        break
    another_game = True
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')

