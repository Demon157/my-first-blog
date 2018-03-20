#! python3
# quickWaether.py - Вывод прогноза погоды для заданного населенного пункта

import json, requests, sys
# Определение названия населенного пунката из аргументов командной строки

print('Введите название города')
gorod = input()

if len(gorod) == 0:
    print('Вы ничего не ввели')
    sys.exit()
location = ' '.join(gorod)

# загрузка JSON из API сайта OpenWeatherMap.org

url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status()