# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
a = 1
b = 5
print(a, ' + ', b, ' = ', a+b)

user_string1 = input("Enter the first line ")
user_number1 = int(input("Enter the first number "))
user_string2 = input("Enter the second line ")
user_number2 = int(input("Enter the second number "))
print("Your lines and numbers: %s, %s and %d, %d" % (user_string1, user_string2, user_number1, user_number2))

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
import datetime

user_time = int(input("Enter time in seconds "))
new_format = datetime.timedelta(seconds=user_time)
print("New format of your time hh:mm:ss ", new_format)

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

number = int(input("Enter number "))
sum = total = (number + int(str(number) + str(number)) + int(str(number) + str(number)+ str(number)))
print("new sum = ", sum)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
positive_number = int(input("Enter any positive number "))
max = positive_number % 10
while positive_number >= 1:
    positive_number = positive_number // 10
    if positive_number % 10 > max:
        max = positive_number % 10
    if positive_number > 9:
        continue
    else:
        print("Max number = ", max)
        break

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = int(input("Enter company revenue "))
cost = int(input("Enter company cost "))
if revenue > cost:
    print("The company works good! Profit")
    print(f"Pofitability = {revenue / cost:.2f}")
    number_workers = int(input("Enter number of workers "))
    print(f"Revenue for 1 worker = {revenue / number_workers:.2f}")
elif revenue == cost:
    print("The company works not good! revenue == cost")
else:
    print("The company works bad! Loss")

# 6. Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
a = int(input("The number of kilometers on the first day a(km) = "))
b = int(input("The expected results b(km) = "))
i = 1
while a < b:
    a = 1.1*a
    # print(a)
    i += 1

print("The number of the day when a sportsmen will achieve the expected result = ", i)