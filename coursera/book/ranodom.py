import random, sys

for i in range (100):
    print (random.randint(700,1000))
while True:
    print('Введите ВЫХОД для выхода')
    response = input()
    if response == 'ВЫХОД':
        sys.exit()
    print ('Ты ввел ' + response)

