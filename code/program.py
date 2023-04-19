def digit_sum(num):
    return sum(int(i) for i in str(num))


s = 0
for i in range(1000, 10000):
    if digit_sum(i) == 20:
        s += i
print(s)

print(tuple(range((n := int(input())) + (n + 1) % 2, n * n + 1, 2)))
