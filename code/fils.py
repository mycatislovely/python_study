alf = " abcdefghijklmnopqrstuvwxyz"
n = int(input())
s = input().strip()
l = len(alf)
d = {alf[i] : i for i in range(l)}
result = [alf[(d[c] + n) % l] for c in s]
print('Result:',' ','"',''.join(result),'"', sep='')  # "lcdpcfdhvdu"

   
    


# s = input().lower().split()
# d = {}
# for w in s:
    # d [w] = d.get(w, 0) + 1
# for k, v in d.items():
    # print(k, v)

# def word_count(file_name):
    # d = {}
    # with open(file_name, 'r', encoding = 'UTF-8') as f:       
        # while True:
            # line = f.readline()
            # if line == '':
                # break
            # words = line.lower().split()
            # for w in words:  # ввожу слова в словарь
                # if w not in d:  # проверяю, есть ли слово в словаре, если нет, то добавляю 
                    # d[w] = 1
                # else:           # если слово уже есть, то +1 к количеству
                    # d[w] += 1  
    # return d 
    
    
# def most_frequent_word(word_counts):
    # w_max = ''
    # n_max = 0
    # for w, n in word_counts.items():
        # if n > n_max or n == n_max and w < w_max:
            # n_max = n
            # w_max = w    
    # return w_max, n_max


# d = word_count('dataset_3363_3 (6).txt')
# d = word_count('word_count_text.txt')
# print(d)
# w, n = most_frequent_word(d)
# print(w, n)
# with open('word_count.txt', 'w', encoding = 'UTF-8') as o:
    # o.write(w + ' ' + str(n))






# n = int(input())
# d = {}
# for i in range(n):
    # x = int(input())
    # if x not in d:
        # d[x] = f(x)
    # print(d[x])
 