class My_Error(Exception):
    def __init__(self):
        pass


class Check:
    def __init__(self):
        self.list = []

    def check_data(self):
        while True:
            try:
                try:
                    user_data = int(input('Введите число: '))
                    ne = input('Для продолжения нажмите "Enter", для остановки введите "stop":')
                    self.list.append(user_data)
                    if ne == 'stop':
                        print(self.list)
                        break

                except ValueError:
                    raise My_Error
            except:
                ne = input('Необходимо ввести число:')
                if ne == 'n':
                    print(self.list)
                    break
x = Check()
x.check_data()