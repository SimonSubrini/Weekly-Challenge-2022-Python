def RockPaperScisors(games):
    winner=0
    for game in games:
        if game[0] not in 'RPS' or game[1] not in 'RPS':
            return "Error, se ingreso una jugada incorrecta"
        if game[0]=='R':
            if game[1]=='S':
                winner+=1
            elif game[1]=='P':
                winner-=1
        elif game[0]=='S':
            if game[1]=='P':
                winner+=1
            elif game[1]=='R':
                winner-=1
        else:
            if game[1]=='R':
                winner+=1
            elif game[1]=='S':
                winner-=1
    if winner>0:
        return "Player 1"
    elif winner==0:
        return "Tie"
    else:
        return "Player 2"


print(RockPaperScisors([("R","S"), ("S","R"), ("P","S")]))
print(RockPaperScisors([("R","S"), ("S","S"), ("P","S")]))
print(RockPaperScisors([("P","S"), ("P","R"), ("R","S")]))
