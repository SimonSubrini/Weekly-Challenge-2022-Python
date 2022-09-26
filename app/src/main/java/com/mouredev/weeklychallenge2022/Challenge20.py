import time
import threading # Módulo para realizar procesos asincronos


def sumWithDelay(a,b,t):
    time.sleep(t)
    print(a+b)

    
def asynchronousCall(a,b,t):
    threading_sum = threading.Thread(target=sumWithDelay, args=(a,b,t))
    threading_sum.start()
    
a=3
b=2
t=5
asynchronousCall(a,b,t)

print("Aca puedo ejecutar código, mientras se corre la función asincrona")
