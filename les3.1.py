def my_func(a, b):
    try:
        a / b
        b / a
    except ZeroDivisionError:
        print('Деление на ноль невозможно!')
    else:
        result = a / b
        print(f"Выполним деление указанных чисел: {a}/{b}={round(result, 2)}")


my_func(int(input('Введите первое число - ')), int(input('Введите второе число - ')))

