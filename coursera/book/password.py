#! usr/bin/python3
# -*- coding: utf-8 -*-
# password.py - Программа для незащищенного хранения паролей.

PASSWORDS = {'mail': 'Xj91732rrz',
             'vk': 'jasfyYYfdsjaf288321$$3',
             'mac': '3434'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('Использование: python password.py [имя учетной записи] -'
          'копирование пароля учетной записи')
    sys.exit()
account = sys.argv[1] # первый аргумент командной строки - это
                      # имя учетной записи
if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Пароль для ' + account + 'скопирован в буфер.')
else:
    print('Учетная запись ' + account + 'отсутствует в списке.')
