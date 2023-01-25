 
print("---------- Средне-арифметическое ----------")    
# a = int(input())
# b = int(input())
a, b = -5, 12
s = 0
n = 0
r = a % 3
if r > 0:
    a += 3 - r
for i in range(a, b + 1, 3):
        s += i
        n += 1
print(s / n)   