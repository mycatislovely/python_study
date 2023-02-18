
    
    
# def quick_merge(lists):
    # result = []
    # pointers = [0] * len(lists)
    # i_min = 0
    # while i_min >= 0:
        # v_min = None
        # i_min = -1
        # for i in range(len(lists)):
            # if pointers[i] < len(lists[i]):
                # v = lists[i][pointers[i]]
                # if v_min is None or v < v_min:
                    # v_min = v
                    # i_min = i
        # if i_min >= 0:            
            # result.append(v_min)
            # pointers[i_min] += 1
        
    # return result

# считываем данные
# lists = [[int(i) for i in input().split()] for _ in range(int(input()))]
# lists = [[1, 2, 3, 400], [50, 60, 700], [10, 11, 17]]
# print(lists)
# вызываем функцию
# print(quick_merge(lists))

def merge(list1, list2):
    tmp = []
    i1 = 0
    i2 = 0
    while i1 < len(list1) and i2 < len(list2):
        if list2[i2] < list1[i1]:
            tmp.append(list2[i2])
            i2 += 1
        else:
            tmp.append(list1[i1])
            i1 += 1
    for i in range(i1, len(list1)):
        tmp.append(list1[i])
    for i in range(i2, len(list2)):
        tmp.append(list2[i])
    return tmp
    
    
def quick_merge(lists):
    result = []
    for l in lists:
        result = merge(result, l)
    return result    
    
lists = [[1, 2, 3, 400], [50, 60, 700], [10, 11, 17]]

print(quick_merge(lists))