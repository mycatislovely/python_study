print("---------- Сумма квадратов ----------")
inp = [1, -3, 5, -6, -10, 13, 4, -8]
print(inp)
s = 0
sq = 0
while True:
    # a = int(input())
    a = inp.pop(0)
    s += a
    sq += a * a
    if s == 0:
        print(sq)
        break