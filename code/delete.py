
sum = 0
while True:
    a = int(input())
    if a < 0:
        break
    sum += a
print(sum)




# def minimum(*args):
    # if len(args) < 1:
        # return None
    # min_valiu = args[0]
    # for v in args:
        # if v < min_valiu:
            # min_valiu = v
    # return min_valiu
    
# print(minimum()) 
# print(minimum(42)) 
# print(minimum('b', 'a')) 
# print(minimum(2, 3, 5, 0, 1)) 

 
# def split_decode_series(string):
    # """Функция принимает строку и возвращает генератор кортежей"""
    # n = 0
    # for c in string:
        # if c.isdigit(): 
            # n = n * 10 + int(c)  
        # else:
            # yield n if n > 0 else 1, c
            # n = 0
    # if n > 0:
        # raise Exception('Строка завершилась цифрой')
        
# def decode_series(series):
    # """ Принимает генератор кортежей и возвращает строку"""
    # s = []
    # for n, c in series:
        # s.append(c * n) 
    # return ''.join(s) 
    
# def rle_decode(string):
    # return decode_series(split_decode_series(string))


# print(rle_decode(input())  
   
       



# ss = input().split()
# print(f'{ss.count("A")/len(ss):.2f}')

# for v in split_decode_series("3ac2s"):
    # print(v)
# series = split_decode_series('3a b 4c 2C a B')
# print(decode_series(series)) 


# def rle_decode(string):
    # return decode_series(split_decode_series(string))




# def decode_str(inp):
    # n = 0
    # s = []
    # for c in inp:
        # if c.isdigit(): 
            # n = n * 10 + int(c)  
        # else:
            # s.append((c * n) if n > 0 else c)
            # n = 0
    # if n > 0:
        # raise Exception('Строка завершилась цифрой')
    # return ''.join(s)


# print(decode_str(input()))

            
# print(inpyt())            