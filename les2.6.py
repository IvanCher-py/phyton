my_dict = {}
my_list = []
stat_list_tech = []
stat_list_sum = []
stat_list_am = []
stat_list_num = []
stat_dict = {}
count = int(input("Сколько будет видов товара: "))
while count >= 1:
    my_dict['название'] = (input("Введите название товара: "))
    my_dict['цена'] = int(input("Введите цену товара: "))
    my_dict['количество'] = (input("Введите количество товара: "))
    my_dict['ед'] = (input("Введите единицу измерения: "))
    my_typle = (count, my_dict)
    my_list.append(my_typle)
    count -= 1
    item_name = my_dict['название']
    stat_list_tech.append(item_name)
    item_sum = my_dict['цена']
    stat_list_sum.append(item_sum)
    item_am = my_dict['количество']
    stat_list_am.append(item_am)
    item_num = my_dict['ед']
    stat_list_num = [item_num]
    stat_dict['название'] = stat_list_tech
    stat_dict['цена'] = stat_list_sum
    stat_dict['количество'] = stat_list_am
    stat_dict['ед'] = stat_list_num
my_list.reverse()
print(f'Структура данных "Товары": \n{my_list}')
print(f'Словарь статистики: \n{stat_dict}')