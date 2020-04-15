print("Привет!")
number = int(input("Введите положительно целое число: "))
num_2 = 0
while number > 0:
    num_1 = number % 10
    if num_1 > num_2:
        num_2 = num_1
        number //= 10
print(f"Самая большая цифра в числе: {num_2}")
input("Нажмите Enter, чтобы выйти!")




