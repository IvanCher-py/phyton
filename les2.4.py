
my_str = input("Введите несколько слов через пробел: ")
my_list = my_str.split()
for i, my_list in enumerate(my_list, 1):
    print(i, my_list[:10])



