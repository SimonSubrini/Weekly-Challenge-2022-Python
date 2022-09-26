def square(n):
    word='*'*n
    for i in range(n):
        print(word)
        
def triangle(n):
    word='*'
    txt=''
    for i in range(n+1):
        txt+=' '*int((n-i)/2)
        txt+=word*i
        print(txt)
        txt=''
            
    
    
square(5) 
triangle(10)  
