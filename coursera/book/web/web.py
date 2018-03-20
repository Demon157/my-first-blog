import webbrowser, requests
#webbrowser.open('http://rusartdesign.ru/test.txt')
res = requests.get('http://rusartdesign.ru/test.txt')
res.raise_for_status()
playFile = open('newfileforweb.txt', 'wb')
for chunk in res.iter_content(100):
    col = playFile.write(chunk)
    print(col)
playFile.close()