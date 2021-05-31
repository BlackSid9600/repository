#namber = input('Введите любое число:')
#print('', max(namber))
number = int(input('Введите любое число:'))
r = -1
while number > 10:
    d = number % 10
    number //= 10
    if d > r:
        r = d
print('Наибольшая цифра в числе:', r)
