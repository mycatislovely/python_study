def merge_sort(a):
    merge_sort_part(a, 0, len(a))
        
def merge_sort_part(a, left, right):
    if right - left > 1:
        middle = (right + left) // 2
        merge_sort_part(a, left, middle)
        merge_sort_part(a, middle, right)
        a[left:right] = merge(a, left, middle, right)

def merge(a, left, middle, right):
    tmp = []
    i1 = left
    i2 = middle
    while i1 < middle and i2 < right:
        if a[i2] < a[i1]:
            tmp.append(a[i2])
            i2 += 1
        else:
            tmp.append(a[i1])
            i1 += 1
    for i in range(i1, middle):
        tmp.append(a[i])
    for i in range(i2, right):
        tmp.append(a[i])
    return tmp
    

        
