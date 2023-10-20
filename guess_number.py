import random


# Gets user number
def get_user_input():
    while True:
        try:
            answer = int(input("Угадайте число: "))
            if 1<= answer <= 100:
                return answer
            print('Пожалуйста введите число в диапазоне от '
                  '1 до 100')
        except ValueError:
            print('Введите число!')


# Main function to play
def play_game():
    random_number = random.randint(1, 100)
    attempts = 0

    while True:
        attempts += 1
        answer = get_user_input()

        if answer == random_number:
            print('Поздравляю вы угадали число!')
            print(f'Вам понадобилось {attempts} попыток')
            break
        elif answer > random_number:
            print('Ваше число слишком большое')
        else:
            print('Ваше число сликшмо маленькое')


if __name__ == '__main__':
    play_game()

