import random
import string


def random_password(size):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''
    password += random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    for char in range(size-4):
        password += random.choice(all_chars)
    return password


pass_len = int(input('What would be the password length?: '))

print('First Random Password is: ', random_password(pass_len))
print('Second Random Password is: ', random_password(pass_len))
print('Third Random Password is: ', random_password(pass_len))