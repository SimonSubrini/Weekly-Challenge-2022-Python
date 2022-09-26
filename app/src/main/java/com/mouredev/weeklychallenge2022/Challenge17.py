def obstacleRace(action:list, road:str):
    auxRoad=''
    if len(action) != len(road):
        return 'Error, se deben ingresar una cantidad de acciones coherente con la longitud de la pista'
    for i in range (len(action)):
        if (action[i] not in ['run','jump']) or (road[i] not in ['_','|']):
            return 'Error, se ha ingresado una acción o un tipo de camino incorrecto, posición: {} accion: {}, camino: {}'.format(i,action[i],road[i])
        else:
            auxRoad+=checkObstacle(action[i],road[i])
    print('\n'+auxRoad)
    return True if auxRoad==road else False
        
    
def checkObstacle(action:str,road:str):
    if ((action=='run'and road=='_')or(action=='jump'and road=='|')):
        return road
    elif road=='_':
        return 'x' 
    else:
        return '/'
    
print(obstacleRace(['run','jump','run','jump','run'], "||_|_"))
print(obstacleRace(['run','jump','run','jump','run'], "_|_|_"))
print(obstacleRace(['jump','run','run','run','run'], "|____"))
print(obstacleRace(['run','jump','run','jump','run'], "__||_"))
