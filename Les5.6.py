subj = {}
with open('text_6.txt', 'r', encoding="utf-8") as my_f:
    for i in my_f:
        i = i.split()
        subject = i[0]
        sum_lesson = sum([int(x[:x.find('(')]) for x in i[1:] if '(' in x])
        subj[subject] = sum_lesson
    print(f"Общее количество часов по предмету - \n {subj}")