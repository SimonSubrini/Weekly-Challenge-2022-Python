def parentesis(txt):
    chars=[]
    signoA='([{'
    signoC=')]}'
    for char in txt:
        if char in signoA or char in signoC:
            if len(chars)==0 and char not in signoA:
                return False

            elif char in signoA:
                chars.append(char)

            elif (chars[-1]=='(') and char==')':
                chars.pop()    
            elif (chars[-1]=='[') and char==']':
                chars.pop()    
            elif (chars[-1]=='{') and char=='}':
                chars.pop()
            else:
                return False
        
    return True

print(parentesis('{[a*(c+d)]-5}'))
print(parentesis('{a*(c+d)]-5}'))
print(parentesis('(((([[{[]}]])())))'))
print(parentesis('(((([{[{}]}]])))'))
print(parentesis(''))
