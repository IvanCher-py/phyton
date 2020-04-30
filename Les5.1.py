user_line = input("введите слова через пробел ")
my_f = open("les5.1.txt", "w", encoding="utf-8")
while user_line:
    my_f.write(user_line + "\n")
    user_line = input("введите слова через пробел ")
    if not user_line:
        break
my_f.close()
my_f = open("les5.1.txt", "r", encoding="utf-8")
for i in my_f:
    print(i)
