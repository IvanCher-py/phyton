def my_dict(x, y):
    i = y
    first_number = x
    while i < -1:
        x = 1 / (x * x)
        i += 1
    print(f'Возведение {first_number} в степень {y} равно {round(x, 3)}')


my_dict(10, -2)
