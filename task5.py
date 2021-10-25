# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

my_line = []
while True:
    line = input("Enter line: ")
    if line == '':
        exit()
    else:
        newline = line + '\n'
        my_line.append(newline)
    with open("text.txt", "w") as file_obj:
        file_obj.writelines(my_line)

# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
my_list = ['My\n', 'Name\n', 'is\n', 'Marina Haha\n']
with open("text2.txt", 'w+') as file_obj:
    file_obj.writelines(my_list)

file_open = open('text2.txt', 'r')
num_lines = len(file_open.readlines())
print(f"The number of lines {num_lines}")

with open("text2.txt") as file_obj:
    for line in file_obj.readlines():
        words = len(line.split())
        print(words)

# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
file_open = open('text3.txt', 'r')
data = file_open.read()
data_list = data.strip().split('\n')
data_dict = {
        data_list[list_i].split()[el] : data_list[list_i].split()[el+1]
        for list_i in range(len(data_list))
        for el in range(len(str(list_i).split()))
    }
list_person = []
for key, value in data_dict.items():
    if int(value) < 20000:
        list_person.append(key)
print(f"People, who have salary less 20000: {list_person}")

for item in data_dict:
    for key, value in data_dict.items():
        try:
            data_dict[key] = int(value)
        except ValueError:
            data_dict[key] = float(value)
avg_salary = sum(data_dict.values())/(len(data_dict))
print(avg_salary)

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('text4.txt', 'r') as file_obj:
    for i in file_obj:
        i = i.split(' ', 1)
        new_file.append(russian[i[0]] + ' ' + i[1])
    print(new_file)

with open('text4.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
#
try:
    with open("text5.txt", "w") as file_obj:
        line = input('Enter the number: \n')
        file_obj.writelines(line)
        num = line.split()
        print(sum(map(int, num)))
except IOError:
    print('Error')
except ValueError:
    print('Value error')

# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
subject = {}
with open("text6.txt", "r") as file_obj:
    for line in file_obj:
        sub, lec, prac, lab = line.split()
        subject[sub] = int(lec) + int(prac) + int(lab)
    print(subject)

# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

import json
profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('text7.txt', 'r') as file_obj:
    for line in file_obj:
        name, firm, salary, cost = line.split()
        profit[name] = int(salary) - int(cost)
        # print(profit)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
    else:
        print(f'None average_profit')
    pr_new = {'average_profit': round(prof_aver)}
    my_string = '[' + str(profit)+','+str(pr_new) + ']'
    print(my_string)

with open('text7.json', 'w') as write_js:
    json.dump(profit, write_js)
    json.dump(pr_new, write_js)
