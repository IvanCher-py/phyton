class Cell:
    def __init__(self, ch):
        self.ch = ch

    def __str__(self):
        return f"Результат {self.ch}"

    def __add__(self, other):
        return Cell(self.ch + other.ch)

    def __sub__(self, other):
        my_sub = self.ch - other.ch
        if my_sub > 0:
            return Cell(my_sub)
        else:
            return f"Error"

    def __mul__(self, other):
        return Cell(self.ch * other.ch)

    def __truediv__(self, other):
        my_truediv = self.ch // other.ch
        if my_truediv > 0:
            return Cell(my_truediv)
        else:
            return f"Error"

    def make_order(self, num):
        row = ''
        for i in range(int(self.ch / num)):
            row += f'{"*" * num} \n'
        row += f'{"*" * (self.ch % num)}'
        return row


my_obj_1 = Cell(20)
my_obj_2 = Cell(20)
print(my_obj_1.make_order(5))
print(my_obj_2.make_order(6))
print(my_obj_1 + my_obj_2)
print(my_obj_1 - my_obj_2)
print(my_obj_1 * my_obj_2)
print(my_obj_1 / my_obj_2)
