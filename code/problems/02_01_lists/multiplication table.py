print("---------- Таблица умножения ----------")
# a = int(input())  
# b = int(input())
# c = int(input())
# d = int(input())
a, b, c, d = 3, 6, 5, 7
print('\t', end='')
for i in range(c, d + 1):
    print(i, end='\t')
print()
for i in range(a, b + 1):
    print(i, end='')
    for j in range(c, d + 1):
        print('\t', i * j, sep='', end='')
    print()