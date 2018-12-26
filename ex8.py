# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, 
# print out a message of congratulations to the winner, and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

print('Playing: Rock Paper Scissors!')
print('Press \'q\' anytime to quit')

while True:
    winner = '0'

    player1 = input('Player 1, choose (R/P/S/q): ').upper()
    if player1 == 'Q': break
    
    player2 = input('Player 2, choose (R/P/S/q): ').upper()
    if player2 == 'Q': break

    if player1 == 'R':
        if player2 == 'P':
            winner = '2'
        elif player2 == 'S':
            winner = '1'
    elif player1 == 'P':
        if player2 == 'R':
            winner = '1'
        elif player2 == 'S':
            winner = '2'
    elif player1 == 'S':
        if player2 == 'R':
            winner = '2'
        elif player2 == 'P':
            winner = '1'
    
    if winner == '0':
        print('Draw!!')
    else:
        print('Player'+winner + ' wins!')
    
    print("\n")