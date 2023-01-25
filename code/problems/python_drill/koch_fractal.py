from tkinter import *
from math import cos, sin, pi


def koch_fractal(n):
    if n < 1:
        return
    yield from koch_fractal(n - 1)
    yield pi / 3  # 60 градусов перевели в радианы
    yield from koch_fractal(n - 1)
    yield -pi * 2 / 3  # -120
    yield from koch_fractal(n - 1)
    yield pi / 3  # 60
    yield from koch_fractal(n - 1)


def draw_line(my_canvas, x1, y1, x2, y2):
    my_canvas.create_line(x1, y1, x2, y2, fill='black')


def new_point(x0, y0, length, angle):
    return x0 + length * cos(angle), y0 - length * sin(angle)


def draw_segment(my_canvas, x0, y0, length, angle, turn):
    angle += turn
    x1, y1 = new_point(x0, y0, length, angle)
    draw_line(my_canvas, x0, y0, x1, y1)
    return x1, y1, angle
   
   
def draw_koch_fractal(n):
    width = 500
    pad = 50
    pad_outer = 20
    height = width / 3 * sin(pi / 3) + pad
    root = Tk()
    my_canvas = Canvas(root, width=width, height=height, bg='white')
    my_canvas.pack(pady=pad_outer, padx=pad_outer)
    
    length = (width - 2 * pad) / 3 ** n
    angle = 0
    x0 = pad
    y0 = height - pad   
    x0, y0, angle = draw_segment(my_canvas, x0, y0, length, angle, 0)
    for i in koch_fractal(n):
        x0, y0, angle = draw_segment(my_canvas, x0, y0, length, angle, i)

    root.mainloop()
    

def draw_koch_snowflake(n):
    width = 400
    pad = 50
    pad_outer = 20
    height = width * 4 / 3 * sin(pi / 3)
    root = Tk()
    my_canvas = Canvas(root, width=width, height=height, bg='white')
    my_canvas.pack(pady=pad_outer, padx=pad_outer)
    
    length = (width - 2 * pad) / 3 ** n
    angle = pi / 3
    x0 = pad
    y0 = height - pad / 2 - width / 3 * sin(pi / 3)
    
    x0, y0, angle = draw_segment(my_canvas, x0, y0, length, angle, 0)
    for i in koch_fractal(n):
        x0, y0, angle = draw_segment(my_canvas, x0, y0, length, angle, i)
    
    angle = -pi / 3  # 60 градусов по часовой стрелке
    x0, y0, angle = draw_segment(my_canvas, x0, y0, length, angle, 0)
    for i in koch_fractal(n):
        x0, y0, angle = draw_segment(my_canvas, x0, y0, length, angle, i)
        
    angle = pi  # 180 градусов 
    x0, y0, angle = draw_segment(my_canvas, x0, y0, length, angle, 0)
    for i in koch_fractal(n):
        x0, y0, angle = draw_segment(my_canvas, x0, y0, length, angle, i)        
        

    root.mainloop() 

    
# draw_koch_fractal(4)
draw_koch_snowflake(4)
