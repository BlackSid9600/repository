import time
class TrafficLight:


    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            print(TrafficLight.__color[i])
            if i == 0:
                time.sleep(7)
            if i == 1:
                time.sleep(2)
            if i == 2:
                time.sleep(10)
            i +=1

traf = TrafficLight()
traf.running()
