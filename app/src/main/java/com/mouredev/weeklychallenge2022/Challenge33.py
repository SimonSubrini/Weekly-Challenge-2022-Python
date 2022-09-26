import math
def chineseSexagenariumCycle(year):
    elements=["madera", "fuego", "tierra", "metal", "agua"]
    animals=["rata", "buey", "tigre", "conejo", "dragón", "serpiente", "caballo", "oveja", "mono", "gallo", "perro", "cerdo"]
    relativeYear=year-1984
    while relativeYear>60:
        relativeYear-=60
    while relativeYear<-60:
        relativeYear+=60
    
    element=elements[math.floor(relativeYear/2)%len(elements)]
    animal=animals[relativeYear%len(animals)]
    return element,animal
    
print(chineseSexagenariumCycle(1929))  
