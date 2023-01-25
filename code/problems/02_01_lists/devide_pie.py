a = int(input())
b = int(input())
ma = 1
mb = 1
Pa = a * ma
Pb = b * mb
while Pa != Pb:
    if Pa < Pb:
        ma = ma + 1
        Pa = a * ma
    else:
        mb = mb + 1
        Pb = b * mb
print(Pa)
