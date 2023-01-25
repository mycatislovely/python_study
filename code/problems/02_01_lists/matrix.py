print("---------- Сумма крестиком (матрица) ----------")
inp = [
    '9 5 3', 
    '0 7 -1',
    '-5 2 9',
    'end'
]
for r in inp:
    print(r)
m = [] 
while True:
    # s = input()
    s = inp.pop(0)
    if s == 'end':
        break 
    m.append([int(i) for i in s.split()]) 
    
M = len(m)
for i in range(M):
    R = len(m[i])
    for j in range(R):
        print(m[i - 1][j] + m[(i + 1) % M][j] + m[i][j - 1] + m[i][(j + 1) % R], end=' ')
    print()