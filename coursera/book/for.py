list = ['первый', 'второй', 'третий']

for i in range(len(list)):
        if i == (len(list)-1):
            print(',and' + list[i])
        else:
            print(str(i) + list[i])

