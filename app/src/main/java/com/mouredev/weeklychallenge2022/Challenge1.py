def isAnagram(word1: str,word2:str):
    word1=word1.lower()
    word2=word2.lower()
    if len(word1)!=len(word2):
        return False
    dict1={}
    dict2={}
    for char1 in word1:
        if char1 in dict1:
            dict1[char1]+=1
        else:
            dict1[char1]=1
            
    for char2 in word2:
        if char2 in dict2:
            dict2[char2]+=1
        else:
            dict2[char2]=1
    if  dict1==dict2:
        return True
    else:
        return False

print(isAnagram('Amor','Roma'))
print(isAnagram('Holaa','Chauu'))
