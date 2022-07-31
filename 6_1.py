import time
import signal

class TrafficLight:

    def running(self):
        _color = {'красный': 7, 'желтый': 2, 'зеленый': 20}
        # _color = ['Красный', 'Желтый', 'Зеленый']
        # _time = [7, 2, 10]
        print('Светофор включен:')
        while True:
            for key in _color:
                print(key)
                time.sleep(_color.get(key))

First = TrafficLight()
print(First.running())

#
# red = TrafficLight('Красный', 7)
# yellow = TrafficLight('Желтый', 2)
# green = TrafficLight('Зеленый', 15)
#
# print(red._color, red._time)
# print(yellow._color, yellow._time)
# print(green._color, green._time)
