class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки инстументом {self.title}')

class Pen(Stationery):

    def draw(self):
        print(f'Вы выбрали инструмент {self.title}. Запуск отрисовки линии выбранным инструментом')

class Pencil(Stationery):

    def draw(self):
        print(f'Вы выбрали {self.title}. Запуск отрисовки штриховки выбранным инструментом')

class Handle(Stationery):

    def draw(self):
        print(f'Вы выбрали {self.title}. Запуск отрисовки заливки выбранным инстументом')

pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()
