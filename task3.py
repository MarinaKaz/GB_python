# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def div(*args):
    try:
        num1 = int(input("Enter 1th number "))
        num2 = int(input("Enter 2nd number "))
        result = num1/num2
    except ValueError:
        return 'Value error!'
    except ZeroDivisionError:
        return "Division by zero"
    return result
print(div())

# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
name1 = input("Enter name: ")
surname1 = input("Enter surname: ")
city1 = input("Enter city: ")
year_dob = int(input("Enter year: "))
email1 = input("Enter email: ")
phone1 = input("Enter phone: ")
name = input("Enter name: ")
surname = input("Enter surname: ")
year = input("Enter year: ")
city = input("Enter city: ")
email = input("Enter email: ")
phone = input("Enter phone: ")

def func(name,surname,year,city,email,phone):
    return ''.join([
        "name: ", name,
        ". surname: ", surname,
        ". year: ", year,
        ". city: ", city,
        ". email: ", email,
        ". phone: ", phone
        ])
print(func(name=name, surname=surname, year=year, city=city, email=email, phone=phone))

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(arg1, arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(f'Result - {my_func(int(input("enter 1th num1 ")), int(input("enter 2nd num2 ")), int(input("enter 3d num9 ")))}')

# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func(x, y):
    if x > 0 and y < 0:
        num1 = x ** y
        num2 = 1
        i = 1
        while i <= abs(y):
            num2 *= x
            i += 1
        return num1, 1 / num2
    else:
        print("You made mistake")
#
# print(my_func(int(input("enter the 1th number: ")), int(input("enter the 2nd number: "))))

# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
# сумме и после этого завершить программу.

def my_sum(my_string):
    sum_res = 0
    number_list = my_string.split()
    for el in number_list:
            if el:
                try:
                    if el == "Q":
                        return sum_res, False
                    else:
                        sum_res = sum_res + int(el)
                except ValueError:
                   continue
    return sum_res, True
flag = True
result = 0
while flag:
    my_string = input("Enter sequence (for exit press Q) ")
    sum, flag = my_sum(my_string)
    result += sum
print(f"Result: {result}")

# 6.Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(*args):
    word = input("Enter word(lat): ")
    return word.title()
print(f"Result: {int_func()}")
