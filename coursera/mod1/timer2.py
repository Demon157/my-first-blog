n = int(input())

n = n % (3600*24)
h = n // 3600
m = n % 3600 // 60
s = n % 60
print(h // 10, h % 10, ':', m // 10, m % 10, ':', s // 10, s % 10,sep='')