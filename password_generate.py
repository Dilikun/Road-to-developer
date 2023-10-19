import string
import random


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


password_length = int(input('Введите длину пароля: '))
generated_password = generate_password(password_length)

if __name__ == "__main__":
    print(f'Ваш сгенерированный пароль:  {generated_password}')