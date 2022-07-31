class Worker:
    _income = {}

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income

class Position(Worker):

    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname} работает в должности {self.position}')

    def get_total_income(self):
        result = 0
        for key in self._income:
            result += self._income.get(key)
        print(f'Доход сотрудника с учетом премии составляет {result}')

worker_1 = Position('Иван', 'Петров', 'инженер', {'оклад': 45000, 'премия': 35000})

print(worker_1.get_full_name())
print(worker_1.get_total_income())
