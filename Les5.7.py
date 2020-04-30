import json

pos_prof = {}
neg_prof = {}
average_prof = {}
sum_prof = 0
count = 0
with open("text_7.txt", "r", encoding="utf-8") as f_obj:
    for line in f_obj:
        line_obj = line.split()
        firm = line_obj[0]
        l_obj = list(map(int, line_obj[2:]))
        pos_profit = l_obj[0] - l_obj[1]
        if pos_profit > 0:
            pos_prof[firm] = pos_profit
            sum_prof = sum_prof + pos_profit
            count += 1
        elif pos_profit < 0:
            pos_prof[firm] = pos_profit
    average_prof['Средняя прибыль'] = round(sum_prof / count)
    aver_prof = [pos_prof, average_prof]
    print(aver_prof)
with open("text_7.json", "w") as write_f:
    json.dump(aver_prof, write_f)
