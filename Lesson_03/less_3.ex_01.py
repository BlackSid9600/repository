def res(a, b):
    if not b == 0:
        print(a / b)
    if b == 0:
        print('Error')

res(int(input('Введите первое число:')), int(input('Введие второе число:')))
