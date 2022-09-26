import math
def dec2bin(n):
    bits=math.ceil(math.log2(n+1))
    bin=[]
    auxN=n
    for i in range(bits):
        bin.append(auxN%2)
        auxN=math.floor(auxN/2)
    return list(reversed(bin))
    
print(dec2bin(14))
