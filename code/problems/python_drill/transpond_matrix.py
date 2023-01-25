def input_matrix():
    x, y = [int(i) for i in input().split()] 
    return [input().split() for _ in range(y)]
        
def transpond_matrix(m):
    y = len(m)
    x = len(m[0]) if y > 0 else 0
    m1 = []
    for i in range(x):
        m1.append([m[j][i] for j in range(y)])
    return m1

def print_matrix(m):
    for line in m: 
        for cell in line:
            print(str(cell).rjust(3, ' '), end=" ")
        print()
