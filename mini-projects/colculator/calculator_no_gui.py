class Calculator:
    """Класс калькулятора, выполняющий основные математические операции"""

    # Выполняет сложение двух чисел
    def add(self, x, y):
        return x + y

    # Выполняет сложение двух чисел
    def subtract(self, x, y):
        return x - y

    # Выполняет умножение двух чисел
    def multiptly(self, x, y):
        return x * y

    # Выполняет деление двух чисел
    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return 'Ошибка: деление на ноль'


def get_user_input(message):
    while True:
        try:
            value = float(input(message))
            return value
        except ValueError:
            print('Не удалось распознать число. Попробуйте снова.')


def main():
    calc = Calculator()

    operations = {
        "1": calc.add,
        "2": calc.subtract,
        "3": calc.multiptly,
        "4": calc.divide
    }

    while True:
        print('Выберите операцию')
        print('1. Сложение')
        print('2. Вычитание')
        print('3. Умножение')
        print('4. Деление')
        print('5. Выход')

        choice = input('Введите номер операции: ')

        if choice == '5':
            print('Выход из программы')
            break
        if choice not in operations:
            print('Не кореектный выбор операции.')
            continue

        num1 = float(input('Введите первое число: '))
        num2 = float(input('Введите второе число: '))

        result = operations[choice](num1, num2)
        print(f'Рузультат: {result}')


if __name__ == '__main__':
    main()