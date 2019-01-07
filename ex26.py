# from pandas import *
# import numpy as np
# Check Tic Tac Toe 
# If a game of Tic Tac Toe is represented as a list of lists, like so:
game = [[0, 1, 2], 
        [2, 2, 1], 
        [2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

# Given a 3 by 3 list of lists that represents a Tic Tac Toe game board, tell me whether anyone has won, and tell me which player won, if any. 
# A Tic Tac Toe win is 3 in a row - either in a row, a column, or a diagonal. 
# Don’t worry about the case where TWO people have won - assume that in every board there will only be one winner.

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

if winner:
    print('Winner is #' + str(winner))
else:
    print('No winner')

# print(DataFrame(game))
# print(np.matrix(game))
print('\n'.join(['  '.join([str(cell) for cell in row]) for row in game]))