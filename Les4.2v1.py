user_list = input('Введите числа через пробел: ').split()
my_list = [int(i) for i in user_list]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(my_list)
print(new_list)