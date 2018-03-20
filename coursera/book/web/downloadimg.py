import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

while not url.endswith('#'):
    #Загрузка страницы
    print('Загружается страница %s...' % url)
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text)

    # Поиск URL-адреса изображения
    comicElem = soup.select('#comic img')
    if comicElem == []:
      print('Не удалось найти изображение')
    else:
        comicUrl = 'https:' + comicElem[0].get('src')
        # Загрузить изображение
        print('Загружается изображение %s...' % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()

    #Сохранение изображения
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()

    #Получение URL-адрес кнопки Prev
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Готово')