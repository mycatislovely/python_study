def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result


def quick_power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent % 2 == 0:
        return quick_power(base * base, exponent / 2)
    else:
        return quick_power(base, exponent - 1) * base


def print_power(base, exponent):
    print(f"{base} ^ {exponent} = {power(base, exponent)}")
 
def print_quick_power(base, exponent):
    print(f"{base} ^ {exponent} = {quick_power(base, exponent)}")
 
 
 
print('------------- normal power --------------')
print_power(2, 0)     
print_power(2, 2)     
print_power(2, 3)     
print_power(3, 1)     
print_power(3, 2)     
print_power(2, 10)   


print('------------- quick power --------------')
print_quick_power(2, 0)     
print_quick_power(2, 2)     
print_quick_power(2, 3)     
print_quick_power(3, 1)     
print_quick_power(3, 2)     
print_quick_power(2, 10)   

