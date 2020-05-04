from time import sleep
from colorama import Fore
from colorama import init

init()


class TrafficLight:
    __color = ["Красный", "Жёлтый", "Зелёный"]
    print("Работа светофора")

    def running(self):
        while True:
            print(Fore.RED + self.__color[0])
            sleep(7)
            print(Fore.YELLOW + self.__color[1])
            sleep(2)
            print(Fore.GREEN + self.__color[2])
            sleep(7)
            print(Fore.YELLOW + self.__color[1])
            sleep(2)
            if input(Fore.WHITE + "Для завершения нажмите Q или 'Enter' чтобы продолжить").upper() == 'Q':
                break


TrafficLight_1 = TrafficLight()
TrafficLight_1.running()

