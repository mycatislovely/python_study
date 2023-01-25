
x = 0
y = 0
f = {'север': lambda n: (x, y + n),
     'юг': lambda n: (x, y - n),
     'запад': lambda n: (x - n, y),
     'восток': lambda n: (x + n, y)
     }
for _ in range(int(input())):
    dir, n = input().split()
    x, y = f[dir](int(n))
print(x, y)     