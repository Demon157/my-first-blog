n = int(input())

k = n % 100
n = n // 100
k = k // 10 + k % 10 * 10
r = n - k + 1
print(r)
