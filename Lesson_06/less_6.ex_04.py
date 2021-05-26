class Car:


    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn_l(self):
        print(f'Машина {self.name} повернула на лево')

    def turn_r(self):
        print(f'Машина {self.name} повернула на право')


class TownCar(Car):


    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            x = self.speed - 60
            print(f'{self.name} привысила скорость на {x} км/ч, органичение скорости 60 км/ч. Текущая скорость {self.speed} км/ч.')


class SportCar(Car):


    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


class WorkCar(Car):


    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            x = self.speed - 40
            print(f'Вы {self.name} привысила скорость на {x} км/ч, органичение скорости 40 км/ч. Текущая скорость {self.speed} км/ч.')



class PoliceCar(Car):


    def __init__(self, speed, color, name, is_police):
        Car.__init__(self, speed, color, name, is_police)


bmw = TownCar(129, 'Черный', 'BMW', False)
audi = WorkCar(89, 'Черный', 'Audi', False)
mercedes = SportCar(150, 'Черный', 'Mecedes', True)
kia = PoliceCar(150, 'Белый', 'KIA', False)


bmw.go(), bmw.turn_l(), bmw.show_speed(), bmw.stop(), print("\n")
audi.go(), audi.turn_r(), audi.show_speed(), audi.stop(), print("\n")
mercedes.go(), mercedes.turn_l(), mercedes.stop(), print("\n")
kia.go(), kia.turn_r(), kia.stop(), print("\n")