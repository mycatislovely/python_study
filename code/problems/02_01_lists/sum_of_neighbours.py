print("---------- Сумма соседей ----------")        
#a = [int(i) for i in input().split()]  
a = '1 3 5 6 10' 
print(f"a = {a}")
a = [int(i) for i in a.split()]  
l = len(a)
if l == 1:
    print(a[0])
else:
    for i in range(l):
        if i == 0:
            print(a[1] + a[-1], end=' ') 
        elif i == l-1: 
            print(a[0] + a[l-2])
        else:
            print(a[i+1] + a[i-1], end=' ')