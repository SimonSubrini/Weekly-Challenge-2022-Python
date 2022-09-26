def calc(archivo):
    row=0
    result=0
    sigOp=' '
    operation=''
    for linea in archivo:
        # Recorro cada renglon
        char=linea.split()[0] # Con esto elimino el \n al final de cada renglon
        operation+=char+' ' # En operation voy "escribiendo" la operación y al final le sumo el resultado
        
        for digit in char: # Reviso si el caracter o caracteres del renglon son validos
            if digit not in '-+*/0123456789':
                return 'Syntax Error 1: {}'.format(digit)
            
        if row==0:  # Verifico, para el primer renglon que solo se hayan ingresado números o un signo negativo
            for digit in char:
                if digit not in '-0123456789':
                    return 'Syntax Error 2: {}'.format(digit)
            if char=='-':
                sigOp='-'
            else:
                result+=int(char)
        
        
        if row>0: # Analisis para los demás renglones, primero verifico si es una operación, y que no haya dos seguidas
            if sigOp=='-':
                if char in '+-*/':
                    return 'Syntax Error 3: {}'.format(char)
                sigOp=''
                result-=int(char)
            elif sigOp=='+':
                if char in '+-*/':
                    return 'Syntax Error 3: {}'.format(char)
                sigOp=''
                result+=int(char)
            elif sigOp=='*':
                if char in '+-*/':
                    return 'Syntax Error 3: {}'.format(char)
                sigOp=''
                result*=int(char)
            elif sigOp=='/':
                if char in '+-*/':
                    return 'Syntax Error 3: {}'.format(char)
                sigOp=''
                result/=int(char)
            else: # Si el caracter recibido no es una operación, entonces guardo la operacion para usarla en el proximo renglon
                sigOp=char
        
        row+=1
    operation+='= '+str(result)
    return operation
        


with open("calculadora.txt","r") as archivo:
    print(calc(archivo))
