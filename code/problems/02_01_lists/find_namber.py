print("---------- Выводит индекс числа ----------")
# lst = [int(i) for i in input().split()]
# x = int(input())
lst = [5, 8, 2, 7, 8, 8, 2, 4]
print(lst)
x = 8
print(x)
printed = False
for i in range(len(lst)):
    if lst[i] == x:
        print(i, end=' ')
        printed = True
if not printed:
    print("Отсутствует")
print()