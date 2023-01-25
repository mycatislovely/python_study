import tkinter
import time
import random
from life import life, input_matrix


animation_window_width=800
animation_window_height=600
animation_refresh_seconds = 0.3

def create_animation_window():
  window = tkinter.Tk()
  window.title("Tkinter Animation Demo")
  window.geometry(f'{animation_window_width}x{animation_window_height}')
  return window

def create_animation_canvas(window):
  canvas = tkinter.Canvas(window)
  canvas.configure(bg="black")
  canvas.pack(fill="both", expand=True)
  return canvas

colors = ["black", "gray"]


def fill_matrix(canvas, matrix, m):
    for y in range(len(m)):
        for x in range(len(m[y])):
            canvas.itemconfig(matrix[y][x], fill=colors[m[y][x]])
  
def animate_ball(window, canvas, m):

    start_y = 30
    start_x = 30
    rect_h = 15
    rect_w = 15
    
    h = len(m)
    w = len(m[0]) if h > 0 else 0
    matrix = []
    i = -1
    for y in range(h):
        i += 1
        line = []
        j = -1
        for x in range(w):
            j += 1
            line.append(canvas.create_rectangle(start_x + j * rect_w, start_y + i * rect_h, 
                        start_x + (j + 1) * rect_w, start_y + (i + 1) * rect_h, 
                        fill="black", outline="#202020", width=1))
        matrix.append(line)

    fill_matrix(canvas, matrix, m)
    window.update()
    # time.sleep(animation_refresh_seconds * 5) 
    
    while True:
        m = life(m)
        fill_matrix(canvas, matrix, m)
        window.update()
        time.sleep(animation_refresh_seconds)

m = input_matrix()
# m = [
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    # [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    # [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
    # [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# Заполнить матрицу... как-то и где-то


        
  
animation_window = create_animation_window()
animation_canvas = create_animation_canvas(animation_window)
animate_ball(animation_window, animation_canvas, m)

animation_window.mainloop()
  
