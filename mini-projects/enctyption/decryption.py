import pyAesCrypt
import os


# Функция дешифрования файла
def decryption(file, password):

    # Задаём размера буфера
    buffer_size = 523 * 1024

    # вызыываем метод расшифровки
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.split(file)[0]),
        password,
        buffer_size
    )

    # чтобы выдеть результат выводим на печать файл имя зашифрованного файла
    print(" [Файл '" + str(os.path.splitext(file)[0]) + "' зашифрован]")

    # удаляем исходный файл
    os.remove(file)


# Функция сканирования директорий
def walking_by_dirs(dir, password):

    # перебираем все поддиректории в узаканной директории
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # если находим файл то расшифруем его
        if os.path.isfile(path):
            try:
                decryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


password = input('Введите пароль для шифрования: ')
walking_by_dirs(dir, password)
