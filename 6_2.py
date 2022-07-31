class Road:

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def submit(self):
        mas = self._length * self._width * 25 * 5
        print(f'Для ремонта учаска дороги длиной {self._length} м и шириной {self._width} м потребуется {mas / 1000} т асфальта')

road = Road(500, 8)

print(road.submit())
