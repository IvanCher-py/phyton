
name = input("Введите Ваше имя: ")
age = input("Укажите Ваш возраст: ")
print(f"Привет {name}, твой возраст {age}.")
answer = input("Хотите узнать сумму чисел (Y/N)")
if answer == "Y":
    print("Хорошо!")
    number1 = int(input("Введите первое число: "))
    number2 = int(input("Введите второе число: "))
    num_sum = number1 + number2
    print(f"Сумма равна: {num_sum}")
else:
    print("Очень жаль! До свидание!")
input("Нажмите Enter, чтобы выйти!")

