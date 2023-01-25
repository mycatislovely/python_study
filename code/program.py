





  
# def list_contains(l,x):
    # for i in l:
        # if i == x:
            # return True
    # return False

# print(list_contains([1, 2, 3], 2))       
# print(list_contains([1, 2, 3], 5))       
                
            
# Написать функцию, которая принимает список l и возвращает новый список с теми элементами, 
# которые повторяются.

# def repiting_value(l):
    # resalt = set()
    # faund = set()
    # for i in l:
        # if i in faund:
            # resalt.add(i)
        # else:
            # faund.add(i)
    # return resalt
                
# print(repiting_value([1, 2, 3, 1, 2, 4]))              



# for i in range(N-1):
    # for j in range(i+1, N):
        # if arr[i] == arr[j]:
            # print("Есть одинаковые")
            # quit()
# print("Все элементы уникальны")






# n = int(input()) 

# a = int(input())
# b = int(input())
# ma = 1
# mb = 1
# Pa = a * ma
# Pb = b * mb
# while Pa != Pb:
    # if a > b:
        # ma = ma + 1
        # Pa = a * ma
    # else:
        # mb = mb + 1
        # Pb = b * mb
        # print(Pa)


# s = 'abcdefghijk'
# s[3:6]
# s[:6]
# s[3:]
# s[::-1]
# s[-3:]
# s[:-6]
# s[-1:-10:-2]







# i = 0
# while i < 5:
    # print('*')
    # if i % 2 == 0:
        # print('**')
    # if i > 2:
        # print('***')
    # i = i + 1

















# a = int(input())
# b = int(input())
# c = int(input())
# if a > b:
    # maks = a
# else:
    # maks = b    
# if  c > maks :
    # maks = c
# print(maks)

# n1 = int(input())
# n2 = int(input())
# n3 = int(input()) 
# n4 = int(input())
# n5 = int(input()) 
# s = 0
# while s == n1 + n2 + n3+ n4 + n5:
    # print(s) 









# if a < b:
    # min = a
# else: 
    # min = b
# if  c < min:
    # min = c
# print(min)
# print(a + b + c - min - maks)
    
    




# a = int(input())
# b = int(input()) 
# c = int(input())
# p = ((a + b + c) / 2) # полупериметр
# s = (p * (p-a) * (p-b) * (p-c)) ** (1/2)
# result = math.sqrt(s)
# print(s)








# a = float(input("first number: "))    # калькулятор
# b = float(input("second number: "))
# c = input("action: ")
# if b == 0 and (c in ['//', '%', '/']):
    # print('Деление на 0!')
# elif c == '+':
    # print(a + b)
# elif c == '-':
    # print(a - b)
# elif c == '*':
    # print(a * b)
# elif c == '/':
    # print(a / b)
# elif c == '%':
    # print (a % b)
# elif c == '//':
    # print(a // b)
# elif c == '**':
    # print (a ** b )
# else:
    # print('Unknown action!')
    
    
# a, d, c = int(input()), int(input()), int(input())   
    
    
    
    
    
    
    
    
    
    
    

# def area(figure, number):
    # if figure == 'прямоугольник':
        # a, b = number       
        # s = (a * b) 
        # print(s)
    # if figure == 'треугольник':
        # a, b, c = number        
        # p = ((a + b + c) / 2) # полупериметр
        # s = (p * (p-a) * (p-b) * (p-c)) ** (1/2)
        # print(s)
    # if figure == 'круг':
        # r = number[0]
        # PI = 3.14
        # s = PI * r ** 2
        # print(s)
        
        
# figure = input()
# if figure == 'прямоугольник':
    # a = int(input())
    # b = int(input())
    # area(figure,(a, b))
# if figure == 'треугольник':
    # a = int(input())
    # b = int(input())
    # c = int(input())
    # area(figure,(a, b, c))
# if figure == 'круг':    
    # r = int(input())
    # area(figure,(r,))








# a = (3)
# b = (4)  #s_triangle
# c = (5)
# p = ((a + b + c) * 2)
# print(p)










# a = int(input())
# print(a * 2)  
# def get_tuple():
    # return 5, "с", True  # возвращает картеж из трех элементов разного типа. 
# А, В, С = get_tuple()
# print(А, В, С)

# x = 5
# y = 10
# y > x * x or y >= 2 * x and x < y



# X = int(input())
# print(X // 60)
# print(X % 60)




# put your python code here: x = 50 мин, h = 1 час, m = 50 мин 
# x = int(input())
# h = int(input())
# m = int(input())
# x = x + h * 60 + m
# print(x // 60)
# print(x % 60)


# X = int(input()) + int(input()) * 60 + int(input())
# print (X // 60, "\n", X % 60)


  
# fib1 = 1
# fib2 = 1
# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
# i = 0
# while i < n - 2:
    # fib_sum = fib1 + fib2
    # fib1 = fib2
    # fib2 = fib_sum
    # i = i + 1
# print("Значение этого элемента:", fib2)



# class Book:
    # def __init__(self, author, title, year, page_count):    
        # self.author = author
        # self.title = title
        # self.year = year
        # self.page_count = page_count
    
    # def colofon(self):
        # return(self.author + ' "' + self.title + '", ' + str(self.year) + ' г., ' +  
            # str(self.page_count) + ' c.')



# book1 = Book('А. Блок', 'Ветер', 1975, 45) # выражение, создающее экземпляр класса Book
# print(book1.author)
# print(book1.title)
# print(book1.colofon()) 


# n= int(input())
# if n%4==0 and n%100!=0:
    # print("Високосный")
# elif n%400==0:
     # print("Високосный")
# else:
     # print("Обычный")



# Проверяем что все значения сохранены.
    # for x in a:
        # found = False
        # for y in b: # цикл 1
            # if x == y:
                # found = True
                # break # досрочный выход из цикла 1
        # if not found:
            # print(f"Error: {a} --> {b}: {x} not found")
    # Проверяем что ничего лишнего не появилось
    # for x in b:
        # found = False
        # for y in a:
            # if x == y:
                # found = True
                # break
        # if not found:
            # print(f"Error: {a} --> {b}: extra element {x}")
    # Проверяем что нет дубликатов
    # for i in range(len(b) - 1): 
        # for j in range(i + 1, len(b)):
            # if b[i] == b[j]:
                # print(f"Error: {a} --> {b}: duplicate at index {i} - {b[i]}")