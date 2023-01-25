from io import StringIO 

def crypt(string, d_crypt):
    result = StringIO()
    for i in string:        
        result.write(d_crypt[i])  
    return result.getvalue()
      

d_encrypt = {}
d_decrypt = {}
for c1, c2 in zip(input(), input()):
    d_encrypt[c1] = c2
    d_decrypt[c2] = c1    

print(crypt(input(), d_encrypt))   
print(crypt(input(), d_decrypt))    
     
