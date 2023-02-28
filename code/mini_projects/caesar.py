import sys


alfs = {'en': 'abcdefghijklmnopqrstuvwxyz', 
        'ru': 'абвгдежзийклмнопрстуфхцчшщъыьэюя',
        }
indexes = {k:{v[i] : i for i in range(len(v))} for k, v in alfs.items()}

def caesar(sring, shift, lang):
    alf = alfs[lang]
    l = len(alf)
    index = indexes[lang]
    result = []
    for c in sring:
        c_lower = c.lower()
        c_isupper = c.isupper()
        if c_lower not in index:
            result.append(c)
        else:
            c_new = alf[(index[c_lower] + shift) % l]
            result.append(c_new.upper() if c_isupper else c_new)
    return ''.join(result)
    

shift = sys.argv[1]
lang = sys.argv[2].strip().lower()
        
while True:
    try:
        sring = input()
    except EOFError:
        break
    if shift == '?':
        for i in range(1, len(alfs[lang])):
            print(f"{i}:".rjust(4, ' '), caesar(sring, i, lang))
    else:
        print(caesar(sring, int(shift), lang))
                  

    
    

