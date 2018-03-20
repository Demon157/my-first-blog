catNames = []

while True:
    print('Введите имя кота №' + str(len(catNames) + 1) + 'Или нажмите Enter')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]
print('Имена всех котов')
for name in catNames:
    print(' ' + name)
