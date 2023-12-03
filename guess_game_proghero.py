import random

print("Enter ('q') anytime you want to quit: q")
score = 0
while True:
    num = random.randint(0, 10)
    guess = input('Guess the number between 0-10: ')
    if guess =='q':
        print('Game Over')
        break
    guess_num = int(guess)
    if guess_num == num:
        print('CONGRATS!You guessed the number')
        score += 10
        print("Your score is: ", score)
    else:
        print("You didn't guess the number")
        print('The number was: ', num)
