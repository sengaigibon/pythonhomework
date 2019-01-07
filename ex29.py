# Tic Tac Toe game...

def checkWinner(game):
    winner = 0
    for i in range(0,3):
        if game[i][0] == game[i][1] and game[i][0] == game[i][2] and game[i][0] != 0:
            winner = game[i][0]
            break
        if game[0][i] == game[1][i] and game[0][i] == game[2][i] and game[0][i] != 0:
            winner = game[0][i]
            break

    if not winner:
        if game[0][0] == game[1][1] and game[0][0] == game[2][2] and game[0][0] != 0:
            winner = game[0][0]
        elif game[0][2] == game[1][1] and game[0][2] == game[2][0] and game[0][2] != 0:
            winner = game[0][2]

    return winner



########## ########## 
import re

board = [[0,0,0],[0,0,0],[0,0,0]]
remainingMoves = 9

print('Tic Tac Toe Game')
print('Player 1 is X. Player 2 is O.')
print('Players indicate their movement by corrdinates row, column; from 1 to 3; like 1,1 - 1,3 - etc \n')
print('START! \n')
print('Boardgame:')
print('\n'.join(['  '.join([str(cell) for cell in row]) for row in board]))

player = 1
winner = 0
keepPlaying = True

while keepPlaying:
    move = input('Player %i: ' % (player)).strip()
    valid = re.search("[1-3],[1-3]", move)
    if not valid:
        print('Invalid input, try again.')
        continue
    
    coordinates = move.split(',')
    row = int(coordinates[0]) - 1 
    col = int(coordinates[1]) - 1 

    if board[row][col]:
        print('Place taken, try again.')
        continue
    
    if player == 1:
        board[row][col] = 'X'
        player = 2
    else:
        board[row][col] = 'O'
        player = 1
    
    remainingMoves -= 1
    print('Boardgame:')
    print('\n'.join(['  '.join([str(cell) for cell in row]) for row in board]))

    if remainingMoves < 5:
        winner = checkWinner(board)
        if winner:
            if winner == 'X':
                winner = 1
            else:
                winner = 2
            print('Player #%d wins!' % winner)
            keepPlaying = input('Do you want to play again?').strip().lower()
            if(keepPlaying == 'n'):
                keepPlaying = False
            else:
                player = winner
                winner = 0
                keepPlaying = True
            continue
    
    if remainingMoves == 0:
        print('No winner - Game Over!')
        keepPlaying = input('Do you want to play again?').strip().lower()
        if(keepPlaying == 'n'):
            keepPlaying = False
        else:
            player = winner
            winner = 0
            keepPlaying = True
        continue

