x = input()
time = int(x)

hours = time // 60 % 24
minuts = time % 60
print(hours, minuts)
