

d =[['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
    ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
    ['', 'C', 'CC', 'CC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
    ['', 'M', 'MM', 'MMM']]

def rome_number(n):
    a = 0
    result = []
    while n > 0:
        i = n % 10
        n //= 10
        result.append(d[a][i])  # Заполняем список
        a += 1
    result.reverse()  # Переворачиваем список на месте
    return ''.join(result)  # Соединяем все элементы списка в строку 

if __name__ == "__main__":       
    print(rome_number(int(input())))


# print(rome_number(134))
# print(rome_number(3245))
# print(rome_number(12))
# print(rome_number(7))

