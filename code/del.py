counter = 0
for i in range(99, 102):
    temp = i
    while temp > 0:
        counter += 1
        temp //= 10
print(counter)

n = int(input())
for i in range(1, 11):
    
    for j in range(n):
       print(f" n={n} + i={i} = {n + i}, end=' '")
    print()