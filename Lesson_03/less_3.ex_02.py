def my(**kwards):
    print(f'{kwards.values()}')
my(name = (input('Введите имя:')),
        n_name = (input('Введие фамелию:')),
        age = (input('Ваш возраст:')),
        city = (input('Ваш Город:')),
        email = (input('Ваш электронный адрес:')),
        tel = (input('Ваш номер телефона:'))
)
