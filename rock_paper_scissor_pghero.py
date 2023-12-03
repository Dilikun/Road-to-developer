def get_winner(p1, p2):
    if p1 == p2:
        return "it's a tie"
    elif p1 =='rock':
        if p2 == 'scissors':
            return 'First plyer wins!'
        else:
            return 'Second plyer wins!'
    elif p1 == 'scissors':
        if p2 == 'paper':
            return 'First plyer wins!'
        else:
            return 'Second plyer wins!'
    elif p1 == 'paper':
        if p2 == 'rock':
            return 'First plyer wins!'
        else:
            return 'Second plyer wins!'
    else:
        return 'Invalid input'


player1 = input('First player: rock, paper or scissors: ')
player2 = input('First player: rock, paper or scissors: ')
print(get_winner(player1, player2))


# Alternative solution
def get_winner_second(p1,p2):
    if p1 == "rock" and p2 == "paper":
        return 'Second player wins!'
    elif p1 == "rock" and p2 == "scissors":
        return 'First player wins!'
    elif p1 == "paper" and p2 == "rock":
        return 'First player wins!'
    elif p1 == "paper" and p2 == "scissors":
        return 'Second player wins!'
    elif p1 == "scissors" and p2 == "rock":
        return 'Second player wins!'
    elif p1 == "scissors" and p2 == "paper":
        return 'First player wins!'
    else:
        return 'Tie'


player11 = input('First player: rock, paper or scissors: ')
player12 = input('First player: rock, paper or scissors: ')
print(get_winner_second(player11, player12))