# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
import copy

m1 = [[31, 22],
 [37, 43],
 [51, 86]]

m2 = [[1, 1],
 [1, 1],
 [1, 1]]

class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for i in range(len(self.matrix)):
            s = s + '\t'.join(map(str, self.matrix[i])) + '\n'
        return s

    def __add__(self, other):
        result_matrix = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result_matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return Matrix(result_matrix)

print(m1)
print(m2)
if len(m1) != len(m2):
    print("error len")

matrix1 = Matrix(m1)
matrix2 = Matrix(m2)
matrix3 = matrix1 + matrix2
print(matrix3)

# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Staff(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def calculate(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Staff):
    @property
    def calculate(self):
        return self.param / 6.5 + 0.5


class Suit(Staff):
    @property
    def calculate(self):
        return self.param * 2 + 0.3


thing_1 = Coat(20)
thing_2 = Suit(30)
print(f"You things have the following parameters:{thing_1} and {thing_2}")
print(f"fabric consumption for each thing {thing_1.calculate} and {thing_2.calculate}")
print(f"sum = {thing_1.calculate + thing_2.calculate}")

# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class OrganicCell:
    def __init__(self, number):
        self.number = number
        self.simbol = '*'
        if self.number < 0:
            print("Error: num < 0")
            exit()

    def __str__(self):
        return str(self.number)

    def __add__(self, other):
        return OrganicCell(self.number + other.number)

    def __sub__(self, other):
        return OrganicCell(self.number - other.number)

    def __mul__(self, other):
        return OrganicCell(self.number * other.number)

    def __truediv__(self, other):
        return OrganicCell(self.number // other.number)

    def make_order(self, count):
        i = self.number
        while i > 0:
            for j in range(1, count+1):
                print(self.simbol, end='')
                i -= 1
                if i <= 0:
                    break
            print('\n', end='')

cell_1 = OrganicCell(3)
cell_2 = OrganicCell(5)
print(f"sum {cell_2+cell_1}")
print(f"subtract {cell_2-cell_1}")
print(f"mul {cell_2 * cell_1}")
print(f"div {cell_2 / cell_1}")
cell_3 = OrganicCell(12)
cell_3.make_order(5)
