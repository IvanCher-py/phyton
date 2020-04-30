word_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
print(word_dict)
new_f = []
with open("text_4.txt", "r") as my_f:
    for i in my_f:
        i = i.split(' ', 1)
        new_f.append(word_dict[i[0]] + ' ' + i[1])
    print(new_f)
with open("text_4v1.txt", "w", encoding="utf-8") as my_f:
    my_f.writelines(new_f)

