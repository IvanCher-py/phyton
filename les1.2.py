print("Привет!")
print("Давай переведем секунды в часы, минуты и секунды.")
time = int(input("Введите число (секунды): "))
h = time // 3600
h_max = h * 3600
m = (time - h_max) // 60
m_max = m * 60
s = (time - h_max) - m_max
print(f"{h:02}:{m:02}:{s:02}")

input("Нажмите Enter, чтобы выйти!")