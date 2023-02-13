def mostCommonVowel(txt):
    cont={'a':len(txt.split('a'))-1,'e':len(txt.split('e'))-1,'i':len(txt.split('i'))-1,'o':len(txt.split('o'))-1,'u':len(txt.split('u'))-1}
    maxCont=max(cont.values())
    if maxCont==0:
        return None
    return max(cont, key=cont.get)

# test
print(mostCommonVowel('Hoola')) # o
print(mostCommonVowel('sdfghjkl')) # None
print(mostCommonVowel('aeeiiioooouuuuu')) # u
