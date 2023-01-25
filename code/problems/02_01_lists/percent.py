print("---------- процентное содержание символов ----------")
# g = input().lower()
g = "acAcCcagggf"
print(g)
g = g.lower()
cnt = 0
for n in g:
    if n == 'c' or n == 'g':
        cnt += 1
print(cnt / len(g) * 100)