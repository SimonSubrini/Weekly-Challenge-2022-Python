import numpy as np
def tictactoe(matrix:list):
    matrix=np.array(matrix)
    # Devuelvo "None" si la matriz no es de 3x3 o si el número de X's y O's es incosistente
    if matrix.shape != (3,3):
        return 'None'
    if abs(count(matrix,'O')-count(matrix,'X'))>1:
        return 'None'
    # Devuelvo "Empate" si ambos jugadores ganaron
    if check(matrix,'O') and check(matrix,'X'):
        return 'Empate'
    # Devuelvo "O" o "X" si uno de los jugadores gano
    if check(matrix,'O'):
        return 'O'
    if check(matrix,'X'):
        return 'X'
    # Devuelvo "None" si no gano ninguno
    return 'None'

def count(matrix,letter):
    c=0
    for i in range(3):
        for j in range(3):
            c += 1 if matrix[i][j]==letter else 0
    return c

def check(matrix,letter):
    letterCountDiag1=0
    letterCountDiag2=0
    for i in range(3):
        letterCountX=0
        letterCountY=0
        letterCountDiag1 += 1 if matrix[i][i]==letter else 0
        letterCountDiag2 += 1 if matrix[2-i][i]==letter else 0
        for j in range(3):
            letterCountX += 1 if matrix[i][j]==letter else 0
            letterCountY += 1 if matrix[j][i]==letter else 0
        if letterCountX==3 or letterCountY==3 or letterCountDiag1==3 or letterCountDiag2==3:
            return True
    return False
    

matrix=np.array([['O','O','X'],['O',' ','X'],['X','O','X']])
print(matrix)
print('Ganador: '+tictactoe(matrix))

matrix=np.array([['O',' ','X'],['O',' ','X'],['X','O',' ']])
print(matrix)
print('Ganador: '+tictactoe(matrix))

matrix=np.array([['O',' ','X'],['O','X','X'],['O','O',' ']])
print(matrix)
print('Ganador: '+tictactoe(matrix))
