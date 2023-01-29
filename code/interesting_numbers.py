# def is_interesring(i):
    # c = 0
    # d = int(i ** 1 / 3)
    # a = 0
    # while a <= d:
        # a3 = a ** 3
        # b = 0
        # while b < a:
            # if a3 + b ** 3 == i:
                # c += 1
                # if c > 2:
                    # return False
            # b += 1
        # a += 1
    # return c == 2 
    
    
    
    # for a in range(0, d + 1):
        # a3 = a ** 3
        # for b in range(0, a):
            # if a3 + b ** 3 == i:
                # c += 1
                # if c > 2:
                    # return False
    # return c == 2    
    

# count = 5
# i = 0
# while count > 0:
    # i += 1
    # if i % 100 == 0:
        # print("log:", i)
    # if is_interesring(i):
        # count -= 1
        # print(i)

 



 
cache = {}
twice = {}

a = 0
while len(twice) < 8:
    a += 1
    b = 0
    while b < a:
        b += 1
        n = a ** 3 + b ** 3

        if n in cache:
            twice[n] = [cache[n], [a, b]]
        else:
            cache[n] = [a, b]

for n in twice:
    print(n, twice[n])



