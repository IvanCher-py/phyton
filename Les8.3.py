class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def is_number(e):
    try:
        float(e)
        return True
    except ValueError:
        return False


new_list = []
while True:
    inp_data = input("Введите положительное число через пробел, для завершения наберите 'stop': ")
    if inp_data == 'stop':
        break
    try:
        if not is_number(inp_data):
            raise OwnError("Вы ввели не число!")
    except OwnError as err:
        print(err)
    else:
        new_list.append(inp_data)

print(f"Все хорошо. Ваш список: {new_list}")



