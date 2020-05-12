class Warehouse:
    def __init__(self, units):
        self.units = units
        self.items = []

    def __str__(self):
        stock_availability = f'Наличие {self.units}:\n'
        if self.items:
            for i, item in enumerate(self.items):
                stock_availability += f"{i + 1}: {item}\n"
        else:
            stock_availability += 'пусто!\n'
        return stock_availability

    def debit(self, OfficeEquipment):
        self.items.append(OfficeEquipment)

    def credit(self, equipment):
        self.items.remove(equipment)

    def moveto(self, equipment, subdivision):
        self.credit(equipment)
        subdivision.debit(equipment)


class OfficeEquipment:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        if not (type(quantity) is int or type(quantity) is float):
            raise OfficeEquipment("Вы ввели не число!")

    def __str__(self):
        return f'Производитель техники: {self.name}, Цена за ед.: {self.price},' \
               f' Количество: {self.quantity}'


class Printer(OfficeEquipment):
    def __init__(self, name, price, quantity, color):
        super().__init__(name, price, quantity)
        self.color = color

    def __str__(self):
        return f'Производитель техники: {self.name}, Цена за ед.: {self.price},' \
               f' Количество: {int(self.quantity)}, Цвет печати: {self.color}'


class Scanner(OfficeEquipment):
    def __init__(self, name, price, quantity, flow):
        super().__init__(name, price, quantity)
        self.flow = flow

    def __str__(self):
        return f'Производитель техники: {self.name}, Цена за ед.: {self.price},' \
               f' Количество: {self.quantity}, Формат печати: {self.flow}'


class Copier(OfficeEquipment):
    def __init__(self, name, price, quantity, print_form):
        super().__init__(name, price, quantity)
        self.print_form = print_form

    def __str__(self):
        return f'Производитель техники: {self.name}, Цена за ед.: {self.price},' \
               f' Количество: {self.quantity}, Тип сканирования: {self.print_form}'


printer1 = Printer('HP', 5000, 5, 'цветной')
scanner1 = Scanner('Canon', 3500, 3, 'поточный')
copier1 = Copier('Xerox', 545000, 2, 'A3')
warehouse_main = Warehouse('на складе')
warehouse_department1 = Warehouse('отдел 1')
warehouse_department2 = Warehouse('отдел 2')
warehouse_main.debit(printer1)
warehouse_main.debit(scanner1)
warehouse_main.debit(copier1)
print(warehouse_main)
warehouse_main.moveto(printer1, warehouse_department1)
print(warehouse_department1)
warehouse_main.moveto(scanner1, warehouse_department2)
warehouse_main.moveto(copier1, warehouse_department2)
print(warehouse_department2)
print(warehouse_main)