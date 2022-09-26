def isPrime(n):
    for i in range(2,n): # No incluyo al 1 ni a n
        if n%i==0:
            return False
    return True

n=100

for i in range(1,n+1):
    if (isPrime(i)):
        print(i)
