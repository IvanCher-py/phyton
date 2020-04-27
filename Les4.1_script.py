from sys import argv

script_name, work_hours, salary_param, premium_param = argv
print('Имя скрипта:', script_name)
salary = float(salary_param) * int(work_hours) + float(premium_param)

print(f'Отработанное время: {work_hours} ч.\n'
      f'Зарплата сотрудника составит: {salary} деревяных!\n')