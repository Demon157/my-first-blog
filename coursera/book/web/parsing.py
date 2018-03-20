import requests, bs4

exampleFile = open ('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read(),"html.parser")
elems = exampleSoup.select('#author')
print('Автор из HTML статьи:' + elems[0].getText())