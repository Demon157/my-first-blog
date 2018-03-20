import re

phoneNumRegex = re.compile(r'(\d)?-(\d\d\d)?\-\d\d\d-\d\d-\d\d')
mo = phoneNumRegex.search('Мой номер: 8-963-690-87-37, 8-953-876-77-55')
print('Найден телефонный номер: ' + mo.group())
