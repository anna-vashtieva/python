class Car:

    def __init__(self, speed, color, name, is_polise):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_polise

    def go(self):
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} повернул {direction}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} равна {self.speed} км/ч')

class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print(f'Внимание! Превышение скорости на {self.speed - 60} км/ч')
        else:
            print(f'Текущая скорость автомобиля {self.name} равна {self.speed} км/ч')

class SportCar(Car):

    def overtaking(self, target, time):
        if self.speed > target.speed:
            result = ((target.speed / 60) * time) / (self.speed / 60 - target.speed / 60)
            print(f'{self.name} догонит {target.name} через {round(result, 2)} мин')
        else:
            print(f'К сожалению, {self.name} не сможет догнать {target.name} :(')

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print(f'Внимание! Превышение скорости на {self.speed - 40} км/ч')
        else:
            print(f'Текущая скорость автомобиля {self.name} равна {self.speed} км/ч')

class PoliceCar(Car):

    def work_day(self, target):
        for el in target:
            if ((el == towncar or el == sportcar) and el.speed > 60) or (el == workcar and el.speed > 40):
                print(f'Работа {self.name} началась!')
                break

    def chase(self, target):
        if (target == towncar or target == sportcar) and target.speed > 60:
            print(f'Преследование автомобиля {target.name} началось')
            if self.speed > target.speed:
                print(f'Автомобиль {target.name} задержан. Водителю выписан штраф')
            else:
                print(f'Автомобиль {target.name} ушел от погони')

        if target == workcar and target.speed > 40:
            print(f'Преследование автомобиля {target.name} началось')
            if self.speed > target.speed:
                print(f'Автомобиль {target.name} задержан. Водителю выписан штраф')
            else:
                print(f'Автомобиль {target.name} ушел от погони')

towncar = TownCar(70, 'Серый', 'Kia', False)
sportcar = SportCar(120, 'Оранжевый', 'Jaguar', False)
workcar = Car(40, 'Красный', 'КАМАЗ', False)
policecar = PoliceCar(100, 'Белый', 'LADA_Police', True)
target = []

towncar.go()
towncar.show_speed()

sportcar.go()
sportcar.show_speed()
sportcar.overtaking(towncar, 5)

workcar.go()
workcar.show_speed()
workcar.turn('налево')
workcar.stop()

policecar.work_day([towncar, sportcar, workcar])
policecar.chase(towncar)
policecar.chase(sportcar)
policecar.chase(workcar)
