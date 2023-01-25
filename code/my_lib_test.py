import my_lib as lib  # lib - это псевдоним модуля my_lib
# Декомпозиция: разделение задачи на части, в данном случае две: сортировка и печать.
            
def test_bubble_sort(a, expected):      
    lib.bubble_sort(a)
    if a != expected:
        print(f"Error: {a} != {expected}")


def test_unique(a, expected):
    b = lib.unique(a) # переменной b присвоен результат выполнения функции lib.unique(a)
    if not lib.arrays_equal_in_any_order(b, expected):
        print(f"Error: {a} --> {b}, but {expected} was expected")
    
      
def test_my_range(start, stop, step, expected): 
    a = []
    for i in lib.my_range(start, stop, step): 
        a.append(i)  # добавление значения в массив (append)
    if a != expected:     
        print(f"Error: expected {expected} actual {a} ") 

 
def test_fibonacci(n, expected): 
    a = []           # пустой массив - список, который сформируется после работы функции 
    for i in lib.fibonacci(n): 
        a.append(i)  # добавление значения в массив (append)
    if a != expected:     
        print(f"Error: expected {expected} actual {a} ")  
   

def test_arrays_equal_in_any_order(a, b, expected):
    actual = lib.arrays_equal_in_any_order(a, b)
    if actual != expected:
        print(f"Error: Arrays {a} and {b} must be {'' if expected else 'not '}equal")
 


 
    







# b = [7, 5, 1, 3, 2, 4] # массив, в нем список значений (индекс у значений-0,1,2,3..)
# lib.bubble_sort(b)   # вызываем функцию
# print(b)

# a = [7, 6, 5, 4, 3, 2, 1]
# lib.bubble_sort(a)
# print(a)

print("----- bubble_sort_tests -----")

# a = [1, 3, 2]
# lib.bubble_sort(a)
# if a != [1, 2, 3]:
    # print(f"Error: {a} != [1, 2, 3]")
    
test_bubble_sort([], [])
test_bubble_sort([150], [150])
test_bubble_sort([20, 10], [10, 20])
test_bubble_sort([1, 2, 3], [1, 2, 3])
test_bubble_sort([1, 3, 2], [1, 2, 3])
test_bubble_sort([40, 30, 20, -50], [-50, 20, 30, 40])
test_bubble_sort(['A', 'D', 'B', 'C'], ['A', 'B', 'C', 'D'])
test_bubble_sort(['a', 'A'], ['A', 'a'])
# test_bubble_sort([2, '1'], [1, 2])
# TypeError: '>' not supported between instances of 'int' and 'str' 
# Нельзя сравнивать строки и числа.


print("----- unique_tests -----")


   
test_unique([], [])
test_unique([50], [50])
test_unique([8, 8], [8])
test_unique(['x', 'v'], ['x', 'v'])
test_unique([1, 2, 3, 4, 5, 3, 1], [2, 3, 4, 5, 1])
test_unique(['1', '2', '3', '4', '5', '3', '1'], ['1', '2', '3', '4', '5'])



print("----- my_range_tests -----")

test_my_range(1, 1, 1, [])
test_my_range(1, 1, 1, [])
test_my_range(1, 3, 1, [1, 2])
test_my_range(2, 7, 2, [2, 4, 6])
test_my_range(7, 2, -2, [7, 5, 3])
try: # Включаем режим отлова исключений
    test_my_range(7, 2, 0, [])
    print('Exception expected')
except Exception:
    pass
test_my_range(0.2, 0.5, 0.2, [0.2, 0.4])       


print("----- fibonacci_test -----")





test_fibonacci(-1, [])
test_fibonacci(0, [])
test_fibonacci(1, [0])
test_fibonacci(2, [0, 1])
test_fibonacci(3, [0, 1, 1])
test_fibonacci(4, [0, 1, 1, 2])
test_fibonacci(5, [0, 1, 1, 2, 3])
test_fibonacci(6, [0, 1, 1, 2, 3, 5])
test_fibonacci(7, [0, 1, 1, 2, 3, 5, 8])



print("----- arrays_equal_in_any_order_test -----")


test_arrays_equal_in_any_order([], [], True)
test_arrays_equal_in_any_order([1], [1], True)
test_arrays_equal_in_any_order([1, 2], [1, 2], True)
test_arrays_equal_in_any_order([1, 2, 1], [2, 1, 1], True)
test_arrays_equal_in_any_order(['a', 'b', 'b'], ['b', 'a', 'b'], True)
test_arrays_equal_in_any_order([1], [], False)
test_arrays_equal_in_any_order([], [1], False)
test_arrays_equal_in_any_order([1, 2], [1, 3], False)
test_arrays_equal_in_any_order([1, 2, 2], [1, 1, 2], False)
test_arrays_equal_in_any_order([1, 2], [1, 2, 2], False)
test_arrays_equal_in_any_order(['a', 'b', 'b'], ['a', 'a', 'b'], False)


   










  