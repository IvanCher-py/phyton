class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title}")
        print("Запуск отрисовки ")


class Pen(Stationery):

    def draw(self):
        print(f"{self.title}")
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print(f"{self.title}")
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print(f"{self.title}")
        print("Запуск отрисовки маркером")


pen_1 = Pen("Ручка")
pen_1.draw()
pencil_1 = Pencil("\nКарандаш")
pencil_1.draw()
handle_1 = Handle("\nМаркер")
handle_1.draw()