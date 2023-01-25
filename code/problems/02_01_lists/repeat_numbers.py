print("---------- Повторение чисел ----------")
# n = int(input())
n = 7
print(n)
d = 1
nd = 0
for i in range(n):
    if nd >= d:
        nd = 0
        d += 1
    print(d, end=" ")
    nd += 1   