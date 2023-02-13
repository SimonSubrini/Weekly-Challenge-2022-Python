import datetime
import random

def adviento(fecha):
    fechaInicio=datetime.datetime(2022,12,1).date()
    fechaFin=datetime.datetime(2022,12,24).date()
    gifts=['gift1', 'gift2', 'gift3', 'gift4', 'gift5', 'gift6', 'gift7', 'gift8', 'gift9', 'gift10', 'gift11', 'gift12', 'gift13', 'gift14', 'gift15', 'gift16', 'gift17', 'gift18', 'gift19', 'gift20', 'gift21', 'gift22', 'gift23', 'gift24']
    
    if fecha<fechaInicio:
        diferencia=fechaInicio-fecha
        return "Todavia faltan {} dias".format(diferencia.days)
    elif fecha>fechaFin:
        diferencia=fecha-fechaFin
        return "Ya pasaron {} dias".format(diferencia.days)
    else:
        return "Tu regalo es: {}".format(random.choice(gifts))
        



fecha = datetime.datetime.now().date()

# test
print(adviento(fecha)) # regalo aleatorio
print(adviento(datetime.datetime(2022,11,6).date())) # Todavia faltan 25 dias
print(adviento(datetime.datetime(2023,1,10).date())) # Ya pasaron 17 dias
