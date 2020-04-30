from random import randint

num_list = [randint(0, 100) for i in range(10)]
num_sum = sum(num_list)
new_list = list(map(str, num_list))
print(new_list)
print(num_sum)
with open("text_5.txt", "w") as my_f:
    my_f.writelines(new_list)
