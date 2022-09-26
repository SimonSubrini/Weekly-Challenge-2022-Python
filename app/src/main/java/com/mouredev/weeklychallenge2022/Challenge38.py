def bin2dec(n):
    dec=0
    for i in range(len(n)):
        dec+=int(n[i])*(2**(len(n)-i-1))
    return dec
    
print(bin2dec('1010'))
print(bin2dec('1011'))
print(bin2dec('11010'))
