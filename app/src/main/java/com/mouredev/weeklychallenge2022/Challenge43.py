
def trucoOTrato(option,arr):
    sustos="🎃 👻 💀 🕷 🕸 🦇".split()
    dulces="🍰 🍬 🍡 🍭 🍪 🍫 🧁 🍩".split()
    result=""
    if option.lower()=="truco":
        cantLetras=0
        edadPar=0
        altTotal=0
        for person in arr:
            nombre=person["Nombre"]
            edad=person["Edad"]
            altura=person["Altura"]
            
            cantLetras+=int(len(nombre)/2)
            edadPar+=1 if edad%2==0 else 0
            altTotal+=altura
        result=cantLetras+2*edadPar+3*int(altTotal/100)
        
    elif option.lower()=="trato":
        cantLetras=0
        condEdad=0
        condAlt=0
        for person in arr:
            nombre=person["Nombre"]
            edad=person["Edad"]
            altura=person["Altura"]
            
            cantLetras+=len(nombre)
            condEdad+=int(edad/3) if edad<=30 else 10
            condAlt+=int(altura/50) if altura<150 else 3
        result=cantLetras+condEdad+2*condAlt
    else:
        return 'error, formato incorrecto'
    return result

print(trucoOTrato("Truco",[{"Nombre":"Simon","Edad":24,"Altura":175},{"Nombre":"Pepe","Edad":15,"Altura":150},{"Nombre":"Pepa","Edad":21,"Altura":165}]))
print(trucoOTrato("TRATO",[{"Nombre":"Simon","Edad":24,"Altura":175},{"Nombre":"Pepe","Edad":15,"Altura":150},{"Nombre":"Pepa","Edad":21,"Altura":165}]))
