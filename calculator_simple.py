def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def divide(num1, num2):
    return num1 / num2


def multiply(num1, num2):
    return num1 * num2


def modulo(num1, num2):
    return num1 % num2


# take input from user
def user_takes_input():
    num1 = float(input('Enter first number: '))
    operation = input('What you want to do(+, -, *, %): ')
    num2 = float(input('Enter first number: '))
    return num1, operation, num2


def main():
    result = 0
    num1, operation, num2 = user_takes_input()
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    elif operation == '%':
        result = modulo(num1, num2)
    else:
        print('Enter enter +, -, * or %')

    print(f'{num1} {operation} {num2} = {result}')


if __name__ == '__main__':
    main()