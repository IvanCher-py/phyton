def sum_func():
    user_exit = False
    result = 0
    while not user_exit:
        user_num = input('Введите целое число через пробел или нажмите "Q" для выхода из программы: ').upper()
        user_list = user_num.split()
        user_sum = 0
        for i in range(len(user_list)):
            if user_list[i] == "Q":
                user_exit = True
            else:
                user_sum = user_sum + int(user_list[i])
        result = result + user_sum
        print(f'Сумма всех чисел равна {result}')


sum_func()
