from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def costume(self):
        pass

    @abstractmethod
    def full_cloth(self):
        return str(f"Общая площадь ткани \n"
                   f" {(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)}")


class MyCoat(Clothes):
    @property
    def coat(self):
        sum_cloth = self.size / 6.5 + 0.5
        return f"Количество требуемой ткани для пальто {sum_cloth:.2f} м."

    @property
    def costume(self):
        sum_cloth = 2 * self.height + 0.3
        return f"Количество требуемой ткани для костюма {sum_cloth:.2f} м."

    @property
    def full_cloth(self):
        return str(f"Общая площадь ткани {round(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)} м.")


class MyCloth(Clothes):
    @property
    def costume(self):
        sum_cloth = 2 * self.height + 0.3
        return f"Количество требуемой ткани для костюма {sum_cloth:.2f} м."

    @property
    def coat(self):
        sum_cloth = self.size / 6.5 + 0.5
        return f"Количество требуемой ткани для пальто {sum_cloth:.2f} м."

    @property
    def full_cloth(self):
        return str(f"Общая площадь ткани {round(self.size / 6.5 + 0.5) + (self.height * 2 + 0.3)} м.")


clothes1 = MyCoat(10, 20)
clothes2 = MyCloth(20, 10)
print(clothes1.full_cloth)
print(clothes1.coat)
print(clothes1.costume)
print(clothes2.full_cloth)
print(clothes2.costume)
print(clothes2.coat)