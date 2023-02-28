from random import randint 

word_list = ['ЖЕНЩИНА', 'МУЖЧИНА', 'ЧЕЛОВЕК', 'РЫБА', 'ПТИЦА', 'СОБАКА', 'ВОШЬ', 'ДЕРЕВО', 
             'СЕМЯ', 'ЛИСТ', 'КОРЕНЬ', 'КОРА', 'КОЖА', 'МЯСО', 'КРОВЬ', 'КОСТЬ', 'ЖИР', 'ЯЙЦО', 
             'РОГ', 'ХВОСТ', 'ПЕРО', 'ВОЛОСЫ', 'ГОЛОВА', 'УХО', 'ГЛАЗ', 'НОС', 'РОТ', 'ЗУБ', 
             'ЯЗЫК', 'НОГОТЬ', 'НОГА', 'КОЛЕНО', 'РУКА', 'ЖИВОТ', 'ГОРЛО', 'ГРУДЬ', 'СЕРДЦЕ', 
             'ПЕЧЕНЬ', 'СОЛНЦЕ', 'ЛУНА', 'ЗВЕЗДА', 'ВОДА', 'ДОЖДЬ', 'КАМЕНЬ', 'ПЕСОК', 'ЗЕМЛЯ', 
             'ОБЛАКО', 'ДЫМ', 'ОГОНЬ', 'ПЕПЕЛ', 'ДОРОГА', 'ТРОПА', 'ГОРА', 'НОЧЬ', 'ИМЯ']
             
alf = set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                  ---
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                  ---
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                  ---
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                  ---
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                  ---
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                  ---
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                  ---
                '''
    ]
    
victory =  '''
                   --------
                   |      |
         O         |    
        \\|/        |    
         |         |    
        / \\        |    
                  ---
                '''
    
def input_letter(used_letters):
    while True:
        letter = input('Назовите букву: ').strip().upper()
        if len(letter) != 1:
            print('Надо ввести одну букву!')
        elif letter not in alf:
            print('Надо ввести букву из алфавита!')
        elif letter in used_letters:
            print('Такая буква уже была!')
        else:
            return letter
    
            
word = word_list[randint(0, len(word_list) - 1)]
guessed_word = '*' * len(word)
print('И так, начинаем игру "Поле чудес"!')
tries  = 6 
used_letters = set()

while guessed_word != word:
    print(stages[tries])
    print('У вас осталось попыток:', tries)
    if tries < 1:
        print('Увы, вы проиграли :(')
        print('Это было слово:', word)
        break
    print('Использованные буквы:', ''.join(sorted(used_letters)))
    print('Угадайте слово:', guessed_word)
    letter = input_letter(used_letters)
    used_letters.add(letter)
    for i in range(len(word)):
        if letter == word[i]:
            guessed_word = guessed_word[:i] + letter + guessed_word[i + 1:]
    if letter not in guessed_word:
        tries -= 1
        print('Нет такой буквы в этом слове :(')
    else:
        print('Есть такая буква в этом слове!')
        
else:
    print('Вы угадали:', guessed_word)            
    print(victory)
            
        









