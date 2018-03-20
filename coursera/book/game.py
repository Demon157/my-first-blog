import random

number = random.randint(1,20)
print('Я придумал число от 1 до 20. Попробуйте угадать его')

for i in range(1,7):
    userNumber = int(input())

    if userNumber > number:
     print('Задуманное число меньше введенного')
    elif userNumber < number:
     print('Задуманное число больше введенного')
    else:
     break
if number == userNumber:
    print('Поздравляем! Колиличество попыток' + str(i))
else:
    print('Вы проиграли! Задуманное число:' + str(userNumber))

