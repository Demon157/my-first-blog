x = input()
y = int(x)

d1 = y % 10
y = y // 10
d2 = y % 10
y = y // 10
d3 = y % 10
res = d1+d2+d3
print(res)
