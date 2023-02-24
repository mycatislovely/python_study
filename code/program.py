from random import *
import sys

def investigate_random(max_num, count):
    results = [0] * max_num
    for _ in range(count):
        results[randint(0, max_num - 1)] += 1
    return results
    
   
def visualize_list(lst, right): 
    v_max = max(lst)
    factor = 1               # if v_max <= right else (right / v_max)
    divider = 1
    if v_max > right:
        factor = right
        divider = v_max
    for v in lst:
        print('*' * (v * factor // divider))
        
max_num = int(sys.argv[1])
count = int(sys.argv[2])      
right = int(sys.argv[3])      
lst = investigate_random(max_num, count)
visualize_list(lst, right)