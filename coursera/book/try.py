def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Деление на ноль')

print(spam(2))
print(spam(0))