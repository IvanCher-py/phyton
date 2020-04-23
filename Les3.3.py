def my_func(a, b, c,):
    number = [a, b, c,]
    numbers = []
    for i in range(2):
        numbers.append(max(number))
        number.remove(max(number))
    print(numbers)
    print(f'Сумма наибольших двух аргументов равна {sum(numbers)}.')


my_func(7, 10, 5)