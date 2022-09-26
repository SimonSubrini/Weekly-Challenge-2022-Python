def fact(n):
    if n%1!=0 or n<0:
        return "Ingrese un número entero positivo"
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(0))   # 0! = 1
print(fact(1))   # 0! = 1
print(fact(2))   # 0! = 2
print(fact(3))   # 0! = 6
