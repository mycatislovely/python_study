def _how_many_alive(m, h, w, y, x):
    top = y - 1
    bottom = (y + 1) % h
    left = x - 1
    right = (x + 1) % w
    return (m[top][left] + m[top][x] + m[top][right] + m[y][right] + 
            m[bottom][right] + m[bottom][left] + m[bottom][x] + m[y][left]) 


def life(m):
    h = len(m)
    w = len(m[0]) if h > 0 else 0
    m1 = [[0] * w for _ in range(h)]
    for y in range(h):
        for x in range(w):
            a = _how_many_alive(m, h, w, y, x)  # Сколько живых вокруг
            if a == 3 and m[y][x] == 0:
                m1[y][x] = 1
            elif 2 <= a <= 3:
                m1[y][x] = m[y][x]
            else:
                m1[y][x] = 0
    return m1
    
    
def input_matrix():
    y, x = [int(i) for i in input().split()] 
    return [[1 if c == "X" else 0 for c in input().strip()] for _ in range(y)]    
    

def print_matrix(m):
    for line in m: 
        for cell in line:
            print("X" if cell == 1 else ".", end="")
        print()

if __name__ == "main":   
    m = input_matrix() 
    m = life(m) 
    print_matrix(m)            
          