def area(figure, number):
    if figure == 'прямоугольник':
        a, b = number       
        s = (a * b) 
        print(s)
    if figure == 'треугольник':
        a, b, c = number        
        p = ((a + b + c) / 2) # полупериметр
        s = (p * (p-a) * (p-b) * (p-c)) ** (1/2)
        print(s)
    if figure == 'круг':
        r = number[0]
        PI = 3.14
        s = PI * r ** 2
        print(s)