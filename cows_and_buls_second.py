import random

secret_numbers = str(random.randint(1000, 9999))
print('Try guess number. It contains 4 digits')
# print(secret_numbers)
remaining_try = 7


def get_bulls_cows(number, user_guess):
    bulls_cows = [0, 0]
    for i in range(len(number)):
        if user_guess[i] == number[i]:
            bulls_cows[0] += 1
        elif user_guess[i] in number:
            bulls_cows[1] += 1
        return bulls_cows


while remaining_try > 0:
    player_guess = input('Player guess: ')

    if player_guess == secret_numbers:
        print('Yay, you win guessed it!')
        print('YOU WIN!')
        break
    else:
        bulls_cows = get_bulls_cows(secret_numbers, player_guess)

        print('Bulls is: ', bulls_cows[0])
        print('Cows is: ', bulls_cows[1])

        remaining_try -= 1

        if remaining_try < 1:
            print('You lost the game!')
            break

