class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    inp_data = int(input("Введите положительное число: "))
    inp_data1 = int(input("Введите положительное число: "))
    try:
        if inp_data == 0 or inp_data1 == 0:
            raise OwnError("Деление на ноль недопустимо!")
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        print(f'Все хорошо. Ваше число: {(inp_data / inp_data1):.2f}')
        break
