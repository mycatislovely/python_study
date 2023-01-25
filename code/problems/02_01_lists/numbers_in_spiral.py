    
print("---------- Цифры по спирали ----------")
# n = int(input())
n = 5
print(n)
m = [[0] * n for i in range(n)] # массив с вложенными массивами

v = 0
for lev in range(n // 2):
    last = n - 1 - lev 
    for i in range(lev, last):
        v += 1
        m[lev][i] = v
    for j in range(lev, last):
        v += 1
        m[j][last] = v
    for i in range(last, lev, -1):
        v += 1
        m[last][i] = v   
    for j in range(last, lev, -1):
        v += 1
        m[j][lev] = v 
        
if n % 2 != 0:
    v += 1
    k = n // 2
    m[k][k] = v 

for r in m:
    for E in r:
        print(str(E).rjust(3, ' '), end=" ")
    print()