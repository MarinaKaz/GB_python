# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

script_name, worked_hour, rate, benefit = argv
salary = int(worked_hour) * int(rate) + int(benefit)
print(f'Your salary {salary}')

# 2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [my_list[i] for i in range(len(my_list)) if my_list[i-1] < my_list[i]]
print(my_list)
print(new_list)

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

new_list = [i for i in range(20, 240) if i % 20 == 0 or i % 21 == 0]
print(new_list)

# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(new_list)

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().
from functools import reduce
my_list = [i for i in range(100, 1000) if i % 2 == 0]
sum = reduce((lambda x, y: x * y), my_list)
print(my_list)
print(sum)

# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

from itertools import cycle, count

num = int(input('Enter the number: '))
stop = int(input('Enter the number(stop): '))
a) var_1
for i in count(num):
    if i < stop:
        print(i)
    else:
        break

a) var_2
my_list = [i for i in range(stop)]
count = 0
for index in cycle(my_list):
    if count < stop:
        print(index)
        count += 1
    else:
        break
b)
my_list = [i for i in range(stop)]
count = 0
for el in cycle(my_list):
    if el == my_list[0]:
        count += 1
    if count < 3:
        print(el)
    else:
        break
# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор. Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

from math import factorial
from itertools import count

def factorial(num):
    for i in count(1):
        if i <= num:
            value = factorial(i)
            yield value
        else:
            break
