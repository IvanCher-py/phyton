class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_calc(self):
        mass_calc = (self._width * self._length * 25 * 5) / 1000
        print(f"Определим массу асфальта для покрытия дороги длинной {self._length} м., шириной {self._width}"
              f" и толщиной 5 см.\nМасса асфальта равна {mass_calc} т.")

road_1 = Road(int(input("Введите длину покрытия ")), int(input("Введите ширину покрытия ")))
road_1.mass_calc()
