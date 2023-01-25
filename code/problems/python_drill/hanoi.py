

def hanoi(n, s1, s2, s3):
    if n < 1:
        return
    elif n < 2:
        yield s1, s3
    else:
        yield from hanoi(n-1, s1, s3, s2) # разворачивает генератор как for и возвращает значение
        yield s1, s3
        yield from hanoi(n-1, s2, s1, s3)
        
        
for i in hanoi(3, 1, 2, 3):
    print(i)
        
               
        
def test_hanoi(n, s1, s2, s3):
    sticks = [[], [], []]
    #  Заполняем массив с индексом s1 числами от `n` до 1 и в убывающем порядке.
    stick = sticks[s1]
    for i in range(n, 0, -1):
        stick.append(i)
    #  Выполняем перекладывания и проверки. 
    i = 0    
    for s_from, s_to in hanoi(n, s1, s2, s3):
        # s_to = 2  #  "вредоносный" код для проверки самого теста.
        i = i + 1
        disk = sticks[s_from].pop() #  сняли диск с первого стержня.
        stick_to = sticks[s_to]  # стержень, на который перекладываем.
        if len(stick_to) > 0:  # массив stick_to не пустой.
            over = stick_to[len(stick_to) - 1]  # диск, на который перекладываем.   
            if disk >= over:
                print(f"Eror: arguments n={n}, s1={s1}, s2={s2}, s3={s3}, step {i}, " 
                      f"disk {disk} over {over}")
                return
        stick_to.append(disk)  # добавление значения в массив (append)
    # проверяем, что в массиве с индексом s3 находится `n` элементов. 
    if len(sticks[s3]) != n:        
        print(f"Eror: arguments n={n}, s1={s1}, s2={s2}, s3={s3}, final height " 
                      f"is {len(sticks[s3])}")
     

    
print("----- hanoi_tests -----")
   
test_hanoi(3, 0, 1, 2)   
test_hanoi(5, 0, 1, 2)   
test_hanoi(3, 1, 0, 2)   
test_hanoi(3, 0, 2, 1)   
test_hanoi(0, 1, 2, 0)   
test_hanoi(1, 0, 2, 1)   
# test_hanoi(20, 0, 2, 1)  # Работает уже заметное время. 
  




 