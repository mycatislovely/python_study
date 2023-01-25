



# x = 0
# print(f'x = {x}')   # (1)
# try: 
    # y = 5 / x 
# except ZeroDivisionError:
    # y = 0       # (2)
# print(f'y = {y}') 

# print("---------- Функция как параметр ----------")  
# def print_field(string, transform):
    # print('[' + transform(string) + ']')
    
# def simple_transform(string):
    # return string   # Что пришло, то функция и вернула
    
# def password_transform(string):
    # return '*' * len(string)
    
# print_field("I love my cat", simple_transform)
# print_field("my secret", password_transform)




  
# def colatc(n):
    # while True:
        # yield n
        # if n == 1:
            # return
        # if n % 2 == 0:
            # n = n // 2
        # else:
            # n = 3 * n + 1 
    
# for n in colatc(int(input())):
    # print(n, end = ' ')
    
    


def colatc(n):
    # limit = 5  # Гипотеза Коллатца - это гипотеза, поэтому мало ли что........
    # cunt = 0
    while True:
        yield n
        # cunt += 1
        # if cunt > limit:
            # raise Exception(f"Результат не достигнут за {limit} шагов")
        if n == 1:
            return
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1 
    
# for n in colatc(int(input())):
    # print(n, end = ' ')


def colatc_len(n):
    cunt = 0
    for _ in colatc(n):
        cunt += 1
    return cunt
        
print(colatc_len(1001))


    



# print("---------- Cписок ----------")
# def modify_list(l):
    # l[:] = [i//2 for i in l if not i % 2]
    
    
# def modify_list(l):
    # for x in l[:]:
        # if x % 2 == 0:
            # l.append(x//2)
        # l.remove(x)    

