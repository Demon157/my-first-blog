h = int(input())
a = int(input())
b = int(input())

h = h - a
b = a - b
s = (b - h % b) % b
d = 1 + (h + s) // b

print(d)
