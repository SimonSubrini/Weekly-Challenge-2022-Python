def RingsOfPower(goodTroops,badTroops):
    goodPoints=0
    badPoints=0
    for troop in goodTroops:
        goodPoints+=goodTroops[troop][0]*goodTroops[troop][1]
    for troop in badTroops:
        badPoints+=badTroops[troop][0]*badTroops[troop][1]
    return goodPoints-badPoints

# Tropas buenas
numPelosos=0
numSureBuenos=0
numEnanos=0
numNumenoreanos=0
numElfos=0

# Tropas malas
numSureMalos=0
numOrcos=0
numGoblins=0
numHuargos=0
numTrolls=0

goodTroops={"Pelosos":[1,numPelosos],"SureBuenos":[2,numSureBuenos],"Enanos":[3,numEnanos],"Numenoreanos":[4,numNumenoreanos],"Elfos":[5,numElfos]}
badTroops={"SureMalos":[2,numSureMalos],"Orcos":[2,numOrcos],"Goblins":[2,numGoblins],"Huargos":[3,numHuargos],"Trolls":[5,numTrolls]}

result=RingsOfPower(goodTroops,badTroops)

if result>0:
    print("Gano el bien")
elif result==0:
    print("Empate")
else:
    print("Gano el mal")
