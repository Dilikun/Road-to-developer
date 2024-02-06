from LxmlSoup import LxmlSoup
import requests

html = requests.get('https://sunlight.net/catalog').text
soup = LxmlSoup(html)
links = soup.find_all('a', class_="cl-item-link js-cl-item-link js-cl-item-root-link")

for i, link in enumerate(links):
    url = link.get('href')
    name = link.text()
    price = soup.find_all('div', class_='cl-item-info-price-discount')[i].text()
    print(i)
    print(f'Url: {url}')
    print(f'Price: {price}')
    print(f'Name: {name}\n')
