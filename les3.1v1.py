def my_func():
    i = 0
    while i >= 0:
        a = int(input('Введите первое число - '))
        b = int(input('Введите второе число - '))
        try:
            a / b
            b / a
        except ZeroDivisionError:
            print('Введите значение больше - 0')
            i += 1
        else:
            result = a / b
            print(f"Выполним деление указанных чисел: {a}/{b}={round(result, 2)}")
            break


my_func()

