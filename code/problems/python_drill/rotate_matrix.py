
def rotate_matrix(m):
    n = len(m)
    levels = n // 2
    for level in range(levels):
        for x in range(level, n - level - 1):
            temp = m[x][n - level - 1]
            m[x][n - level - 1] = m[level][x]
            temp1 = m[n - level - 1][n - x - 1]
            m[n - level - 1][n - x - 1] = temp 
            temp = m[n - x - 1][level]
            m[n - x - 1][level] = temp1
            m[level][x] = temp
            
            
def print_matrix(m):
    for line in m: 
        for cell in line:
            print(str(cell).rjust(3, ' '), end=" ")
        print()


def demonstrate_rotation(m):
    print('================')
    print_matrix(m)
    rotate_matrix(m)
    print('----------------')
    print_matrix(m)

demonstrate_rotation([[1]])
   
demonstrate_rotation([
    [ 1,  2],
    [ 3,  4],
    ])

demonstrate_rotation([
    [ 1,  2,  3],
    [ 4,  5,  6],
    [ 7,  8,  9]
    ])


demonstrate_rotation([
    [ 1,  2,  3,  4],
    [ 5,  6,  7,  8],
    [ 9, 10, 11, 12],
    [13, 14, 15, 16]
    ])

def picture_to_matrix(picture):
    lines = picture.splitlines()
    width = 0
    for line in lines:
        if len(line) > width:
            width = len(line)
    n = width if width > len(lines) else len(lines)
    for _ in range(n - len(lines)):
        lines.append("")
    for i in range(len(lines)):    
        lines[i] = lines[i].ljust(n)
    return [list(line) for line in lines]    
   

def matrix_to_picture(m):
    return "\n".join([''.join(line) for line in m])



picture = (
"""         
      * 
      ***
***********
************* 
***********
      ***
      *    
""")


print('================')
print(picture)
m = picture_to_matrix(picture)
rotate_matrix(m)
print('----------------')
print(matrix_to_picture(m))



