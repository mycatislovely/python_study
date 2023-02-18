def convert_to_python_case(text):
    result = [[]]
    current = result[0]
    for c in text:
        if c.isupper():
            current = []
            result.append(current)
        current.append(c)
    return '_'.join([''.join(e).lower() for e in result if len(e) > 0])
    
# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))