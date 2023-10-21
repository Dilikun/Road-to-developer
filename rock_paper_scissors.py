import random

while True:
    user_action = input('Сделайте выбор- камень, ножницы или бумага: ')
    possible_actions = ['камень', 'бумага', 'ножницы']
    computer_actions = random.choice(possible_actions)

    print(f'Вы выбрали-{user_action} и компьютер выбрал-{computer_actions}')

    if user_action == computer_actions:
        print(f"Оба пользователя выбрали одинаковый элемент- {user_action}")
    elif user_action == 'камень':
        if computer_actions == 'ножницы':
            print("Камень бьёт ножницы! Вы победили!")
        else:
            print("Бумага обворачивает камень! Вы проиграли!")

    elif user_action == 'бумага':
        if computer_actions == 'камень':
            print("Бумага обворачивает камень! Вы выиграли!")
        else:
            print('Ножницы режут бумагу! Вы проиграли!')

    elif user_action == 'ножницы':
        if computer_actions == 'бумага':
            print("Ножницы режут бумагу! Вы выиграли!")
        else:
            print('Камень бьёт бумагу! Вы проиграли!')

    play_again = ''
    play_again = input('Сыграем ещё раз? (д/н): ')
    if play_again.lower() != 'д':
        break
