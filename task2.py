# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = ['gb', None, 3, 1.1, True]
for el in my_list:
    print(f'{el} - {type(el)}')

# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

num_el_my_list = int(input("Enter the number of elements of list "))
el = 0
i = 0
my_list = []
while el < num_el_my_list:
    my_list.append(input("Enter the value of element "))
    el += 1
print(my_list)
if len(my_list) % 2 == 0:
    a = len(my_list)
else:
    a = len(my_list) - 1
while i < a:
    elem = my_list[i]
    my_list[i] = my_list[i+1]
    my_list[i+1] = elem
    i += 2
print(my_list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month_num = int(input("Enter the number of month "))
month_dict = {
    1: 'Jan',
    2: 'Feb',
    3: 'Mar',
    4: 'Apr',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'Aug',
    9: 'Sept',
    10: 'Oct',
    11: 'Nov',
    12: 'Dec'
}
print(month_dict.get(month_num, 'Wrong number'))
# через словарь
seasons = {'Winter': [1, 2, 12],
           'Spring': [3, 4, 5],
           'Summer': [6, 7, 8],
           'Autumn': [9, 10, 11]}
for key in seasons.keys():
    if month_num in seasons[key]:
        print(key)
# через список
seasons_list = ['Winter', 'Spring', 'Summer', 'Autumn']
if month_num == 1 or month_num == 12 or month_num == 2:
    print(seasons_list[0])
elif month_num == 3 or month_num == 4 or month_num == 5:
    print(seasons_list[1])
elif month_num == 6 or month_num == 7 or month_num == 8:
    print(seasons_list[2])
elif month_num == 9 or month_num == 10 or month_num == 11:
    print(seasons_list[3])

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

new_string = input("Enter string(divide by a space) ")
my_string = new_string.split(' ')
for i, word in enumerate(my_string):
    if len(word) < 10:
        print(f"{i} {word}")
    else:
        print(f"{i} {word [0:10]}")

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]
new_number = int(input("Enter new number. (For exit enter 00) "))
while new_number != 00:
    for el in range(len(my_list)):
        if my_list[el] == new_number:
            my_list.insert(el+1, new_number)
            break
        elif my_list[el] > new_number and my_list[el + 1] < new_number:
            my_list.insert(el + 1, new_number)
        elif my_list[0] < new_number:
            my_list.insert(0, new_number)
        elif my_list[-1] > new_number:
            my_list.append(new_number)
    print(f"New list {my_list}")
    new_number = int(input("Enter new number. (For exit enter 00) "))
print("You're out")

# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
goods = []
while input("Do you want to add product? Enter yes/no: ") == 'yes':
    number = int(input("Enter product number: "))
    features = {}
    while input("Do you want add product parameters? Enter yes/no: ") == 'yes':
        feature_key = input("Enter feature product: ")
        feature_value = input("Enter feature value product: ")
        features[feature_key] = feature_value
    goods.append(tuple([number, features]))
print(goods)
analytics = {}
for el in goods:
    for feature_key, feature_value in el[1].items():
        if feature_key in analytics:
            analytics[feature_key].append(feature_value)
        else:
         analytics[feature_key] = [feature_value]
print(analytics)
