my_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
user_month = int(input("Введите месяц в виде целого числа: "))
month = user_month - 1
if month in range(len(my_list)):
    print(f"В это время года {my_list[month]}.")