def poke(type1,type2,ataq,defe):
    types=["agua","fuego","planta","electrico"]
    if type1.lower() not in types or type2.lower() not in types:
        return "Se han ingresado tipos de pokemon incorrectos"
    
    effective=1   
    if type1.lower()=="agua":
        if type2.lower()=="fuego":
            effective=2
        elif type2.lower()=="planta" or type2.lower()=="agua":
            effective=0.5
            
    elif type1.lower()=="fuego":
        if type2.lower()=="planta":
            effective=2
        elif type2.lower()=="agua" or type2.lower()=="fuego":
            effective=0.5
            
    elif type1.lower()=="planta":
        if type2.lower()=="agua":
            effective=2
        elif type2.lower()=="fuego" or type2.lower()=="planta":
            effective=0.5
    
    else:
        if type2.lower()=="agua":
            effective=2
        elif type2.lower()=="electrico" or type2.lower()=="planta":
            effective=0.5
    
    return 50*(ataq/defe)*effective

poke("agua","agua",8,4)
