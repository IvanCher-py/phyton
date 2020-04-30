fam_name = []
salary = []
salary_sum = []
salary_big = []
with open("text_3.txt", "r", encoding="utf-8") as cool:
    for i in cool:
        num = 20000.0
        i = i.split()
        salary_sum.append(i[1])
        if float(i[1]) < num:
            fam_name.append(i[0])
            salary.append(i[1])
sal_sum = sum(map(float, salary_sum)) / 10
salary_big = sum(map(float, salary)) / len(fam_name)
print(f"Сотрудники у кого зарплата менее 20000 {fam_name}"
      f" и их средняя зарплата данных сотрудников составляет {salary_big:.2f}")
print(f"Средняя зарплата всех сотрудников составляет {sal_sum}")
