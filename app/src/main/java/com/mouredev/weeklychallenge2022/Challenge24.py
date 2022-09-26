def Op1():
    for i in range(1,11):
        print(i)

def Op2(n=0):
    if n>9:
        return
    else:
        n+=1
        print(n)
        Op2(n)
    
def Op3():
    [print(i) for i in range(1,11)]  

# Op1()
# Op2()
Op3()
