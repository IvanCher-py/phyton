class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        print(f"Имя - {self.name}\nФамилия - {self.surname}")

    def get_total_income(self):
        salary = self._income["wage"] + self._income["bonus"]
        print(f"Зарплата сотрудника: {salary} руб.")

position_1 = Position("Petr", "Pupkin", "engineer", 215000, 40000)
print(position_1.name)
print(position_1.surname)
print(position_1.position)
print(position_1._income)
position_1.get_full_name()
position_1.get_total_income()
