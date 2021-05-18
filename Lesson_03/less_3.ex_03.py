def my(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return print(sum(z))
my(int(input('Введиете число:')), int(input('Введиете число:')), int(input('Введиете число:')))
