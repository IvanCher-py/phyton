my_list = [7, 5, 3, 3, 2]
num = float(input("Элемент рейтинга: "))
for i in range(len(my_list)):
    if num > my_list[i]:
        my_list.insert(i, num)
        print(my_list)
        break
    elif num <= my_list[-1]:
        my_list.append(num)
        print(my_list)
        break

