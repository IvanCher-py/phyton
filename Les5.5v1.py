my_f = open("text_5.txt", "w")
my_num = input("Введите числа через пробел ")
my_f.write(my_num)
my_l = my_num.split()
sum_l = sum(map(int, my_l))
print(sum_l)
my_f.close()

