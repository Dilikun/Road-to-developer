import string
import random


def generate_password(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for char in range(size):
        rand_char = random.choice(all_chars)
        password += rand_char
    return password


pass_len = int(input('Enter how many characters you want in password: '))
new_password = generate_password(pass_len)
print('Your password has been generated: ', new_password)
