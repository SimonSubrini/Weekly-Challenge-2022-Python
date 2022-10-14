def verifyParams(V,I,R):
    if((V=='' and (I=='' or R=='')) or (I=='' and (V=='' or R=='' or R==0)) or (R=='' and (V=='' or I=='' or I==0))) or (V!='' and I!='' and R!=''):
        return False
    return True

def Ohm(V='',I='',R=''):
    if(verifyParams(V,I,R)):
        if V=='':
            return round(I*R, 2)
        elif I=='':
            return round(V/R, 2)
        else:
            return round(V/I, 2)
    else:
        return "Invalid values"

print(Ohm(V=10,I=2.3))
print(Ohm(V=10,R=5))
print(Ohm(R=3,I=2))
print(Ohm(V=10,I=2,R=3))
print(Ohm(R=3))
print(Ohm(V=10))
