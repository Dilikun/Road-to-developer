# Скрапинг содержимого страницы

# Использован модуль urllib.request стандартной библиотеки urllib
# from urllib.request import urlopen
# url = 'http://example.com/'
# page = urlopen(url)
# print( page.read().decode('UTF-8'))


# # Использован requests
# from bs4 import BeautifulSoup
# import requests
# url = 'https://skillbox.ru/media/code/parsing-sayta-vmeste-s-python-i-bibliotekoy-beautiful-soup-prostaya-instruktsiya-v-tri-shaga/'
# res = requests.get(url)
# soup = BeautifulSoup(res.text, 'html.parser')
# print(soup)


# Парсинг без имитации действий пользователя
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# url = "https://sky.pro/media/chto-takoe-rekursiya-v-python-i-kak-ee-ispolzovat/"
# page = urlopen(url)
# html = page.read().decode('utf-8')
# soup = BeautifulSoup(html, 'html.parser')
# links = set()
# for link in soup.find_all('a'):
#     l = link.get('href')
#     if l != None and l.startswith('https'):
#         links.add(l)
# for link in links:
#     print(link)


# С имитацией действия пользователя
# использована библиотека MechanicalSoup альтернатива Selenium
import mechanicalsoup

# создаём экземпляр класса
browser = mechanicalsoup.StatefulBrowser()

# передаём ссылку которую будем обрабатывать (парсить)
browser.open('http://httpbin.org/   ')

# через метод клсса передаём аргумент
browser.follow_link('forms')

# Имитируем выбор полей ввода с помощье метода
browser.select_form('form[action="/post"]')

# выводим в консоль поля ввода
print(browser.form.print_summary())

# Имитация заполнения формы
browser["custname"] = "Best Customer"
browser["custtel"] = "+7 916 123 45 67"
browser["custemail"] = "trex@example.com"
browser["size"] = "large"
browser["topping"] = ("cheese", "mushroom")
browser["comments"] = "Add more cheese, plz. More than the last time!"

# Отправляем форму в поля ввода
response = browser.submit_selected()

