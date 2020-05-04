class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self):
        turn_direction = input("Укажите направление автомобиля ")
        print(f"{self.name} едит {turn_direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name} {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Снизьте скорость на {self.speed - 60} км/ч")
        else:
            print("Good")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Снизьте скорость на {self.speed - 40} км/ч")
        else:
            print("Good")


class PoliceCar(Car):
    pass


town_car = TownCar(int(input("Укажите скорость машины ")), input("Укажите цвет машины "), input("Укажите марку машины "), False)
print(town_car.speed, town_car.color, town_car.name, town_car.is_police)
town_car.go()
town_car.stop()
town_car.turn()
town_car.show_speed()
town_car.is_police
sport_car = SportCar(int(input("Укажите скорость машины ")), input("Укажите цвет машины "), input("Укажите марку машины "), False)
print(sport_car.speed, sport_car.color, sport_car.name, sport_car.is_police)
sport_car.go()
sport_car.stop()
sport_car.turn()
sport_car.show_speed()
sport_car.is_police
work_car = WorkCar(int(input("Укажите скорость машины ")), input("Укажите цвет машины "), input("Укажите марку машины "), False)
print(work_car.speed, work_car.color, work_car.name, work_car.is_police)
work_car.go()
work_car.stop()
work_car.turn()
work_car.show_speed()
work_car.is_police
police_car = PoliceCar(int(input("Укажите скорость машины ")), input("Укажите цвет машины "), input("Укажите марку машины "), True)
print(police_car.speed, police_car.color, police_car.name, police_car.is_police)
police_car.go()
police_car.stop()
police_car.turn()
police_car.show_speed()
police_car.is_police





