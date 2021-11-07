# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []
        for i in day_month_year.split():
            if i != '-': my_date.append(i)
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 < day or day > 31:
            return ValueError('Day not correct')
        elif 1 < month or month > 12:
            return ValueError('Month not correct')
        elif 0 < year or year > 3000:
            return ValueError('Year not correct')
        else:
            return 'All numbers are correct'


my_date = Data.extract(str(input('Enter the date in format dd - mm - yyyy ')))
print(Data.valid(my_date[0], my_date[1], my_date[2]))


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(div, den):
        try:
            return (div / den)
        except ZeroDivisionError:
            return 'Divide by null'


a = int(input('Enter divider '))
b = int(input('Enter denominator '))
print(DivisionByNull.divide_by_null(a, b))


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.

class IntList:
    def __init__(self, *args):
        self.list = []

    def check_list(self):
        while True:
            try:
                num = int(input('Enter the number '))
                self.list.append(num)
            except:
                print('The number not digit')
                stop = input(f'Try again. If not enter STOP ')
                if stop != 'STOP':
                    print(try_except.check_list())
                if stop == 'STOP':
                    print(f'Exit {self.list}')
                    break


try_except = IntList()
try_except.check_list()


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class OrgTech:
    def __init__(self, name, cost, amount, using):
        self.name = name
        self.cost = cost
        self.using = using
        self.amount = amount
        self.store = []
        self.my_store_full = []
        self.unit = {'The name': self.name, 'Cost': self.cost, 'Amount': self.amount}

    def rent(self):
        try:
            unit = input('Enter the name ')
            cost = int(input(f'Enter the cost '))
            num = int(input(f'Enter the number '))
            unique = {'The name': unit, 'Cost': cost, 'Amount': num}
            self.unit.update(unique)
            self.store.append(self.unit)
        except:
            return 'Error ValueError'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.store)
            print(f'Весь склад -\n {self.my_store_full}')
            quit()
        else:
            return OrgTech.rent(self)


class Printer(OrgTech):
    def print(self):
        return print(f'To print {self.using}')


class Scanner(OrgTech):
    def scan(self):
        return print(f'To scan {self.using}')


class Copier(OrgTech):
    def copier(self):
        return print(f'To copy {self.using}')


unit = OrgTech(0, 0, 0, 0)
unit.rent()


#
# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__(self, other):
        return ComplexNumber(self.num1 + other.num1, self.num2 + other.num2)

    def __mul__(self, other):
        return ComplexNumber(self.num1 * other.num1 - self.num2 * other.num2,
                             self.num1 * other.num2 + self.num2 * other.num1)

    def __str__(self):
        return f"{self.num1} + {self.num2}j"


complex1 = ComplexNumber(2, 3)
complex2 = ComplexNumber(3, 4)
print(f'Sum = {complex1 + complex2}')
print(f'Mult = {complex1 * complex2}')
