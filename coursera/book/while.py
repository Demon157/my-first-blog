while True:
    print('Как Ваше имя?')
    name = input()
    if name != 'Дмитрий':
        continue
    print('Привет, Дмитрий! Введи пароль!')
    password = input()
    if password == '':
        print('Пустой пароль')
    else:
        print('Доступ разрешен')
