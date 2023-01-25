
x = 0
y = 0
f = {'север': (0, 1),
     'юг': (0, -1),
     'запад': (-1, 0),
     'восток': (1, 0)
     }
for _ in range(int(input())):
    dir, n = input().split()
    n = int(n)
    k1, k2 = f[dir]
    x += k1 * n
    y += k2 * n
print(x, y)   





        