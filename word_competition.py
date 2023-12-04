import random


def get_a_clue():
    clues = ['a-e', 'y-ll-w', 's-mm-r', 'wi-t-e-r', 's-n-y', 'l-v', 'i-e']
    position = random.randint(0, len(clues)-1)
    clue = clues[position]
    print(clue)
    return clue


def check_word_match(clue, guess):
    if len(clue) != len(guess):
        return False
    for i in range(len(clue)):
        if clue[i] != '-' and clue[i ]!= guess[i]:
            return False
        return True


word_clue = get_a_clue()
print('Your word clue: ', word_clue)
answer = input('What would be the word: ')

is_matched = check_word_match(word_clue, answer)

if is_matched is not True:
    print('WOW! YOU WIN!!!')
else:
    print('Ooops! you missed it :(')

