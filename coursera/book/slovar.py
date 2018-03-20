dr = {'Дима': '24.07.1990',
      'Аня': '09.04.1990',
      'Руслан': '13.03.2016'}
while True:
    print('Введите имя или нажмите ввод для выхода')
    name = input()
    if name == '':
        break
    if name in dr:
        print(dr[name] + 'день рожденья' + name)
    else:
        print('Я не знаю даты дня рождения' + name)
        print('Введите дату рождения для ' + name)
        bday = input()
        dr[name] = bday
        print('Ваша дата добавлена в Базу')