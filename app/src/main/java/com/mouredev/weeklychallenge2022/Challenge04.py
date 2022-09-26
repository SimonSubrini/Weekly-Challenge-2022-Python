def Surface(polType,params):
    if polType=="Triangle":
        return (params[0]*params[1])/2
    elif polType=="Square":
        return params**2
    elif polType=="Rectangle":
        return params[0]*params[1]
    else:
        return "Ingrese un tipo de poligono adecuado"

print(Surface("Triangle",[2,4]))
print(Surface("Square",3.))
print(Surface("Rectangle",[2,4.]))
print(Surface("Circle",3))
