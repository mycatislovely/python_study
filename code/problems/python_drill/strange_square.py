

def strange_square(n):
    m = [[0] * n for _ in range(n)]
    for level in range(n // 2):
        m [level][level] = 1 + level
        m [level][n - level - 1] = 1 + level 
        m [n - level - 1][level] = n - level 
        m [n - level - 1][n - level - 1] = n - level 
    return m

def print_matrix(m):
    for line in m: 
        for cell in line:
            print(str(cell).rjust(3, ' '), end=" ")
        print()

print('-----------------')
print_matrix(strange_square(2))


print('-----------------')
print_matrix(strange_square(3))


print('-----------------')
print_matrix(strange_square(4))



print('-----------------')
print_matrix(strange_square(5))



print('-----------------')
print_matrix(strange_square(6))

# Вывод
# -----------------
#   1   1
#   2   2
# -----------------
#   1   0   1
#   0   0   0
#   3   0   3
# -----------------
#   1   0   0   1
#   0   2   2   0
#   0   3   3   0
#   4   0   0   4
# -----------------
#   1   0   0   0   1
#   0   2   0   2   0
#   0   0   0   0   0
#   0   4   0   4   0
#   5   0   0   0   5
# -----------------
#   1   0   0   0   0   1
#   0   2   0   0   2   0
#   0   0   3   3   0   0
#   0   0   4   4   0   0
#   0   5   0   0   5   0
#   6   0   0   0   0   6
