# Algoritmo Iterativo
def FiboI(n):
    if n<=0 or n%1!=0:
        print("Ingrese un valor entero mayor a cero")
        return
    elif n==1:
        print(0)
    else:
        a=0
        b=1
        print(a)
        print(b)
        for i in range(3,n+1):
            c=a+b
            print(c)
            a=b
            b=c

# Algoritmo Recursivo
def FiboR(n):
    if n<=0 or n%1!=0:
        print("Ingrese un valor entero mayor a cero")
        return -1
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        Fib=FiboR(n-1)+FiboR(n-2)
        return Fib
    
n=6
print("---------------------------------")
print("Algoritmo iterativo\n")
FiboI(n)
print("---------------------------------")
print("Algoritmo recursivo\n")
for i in range(1,n+1):
    print(FiboR(i))
print("---------------------------------")
