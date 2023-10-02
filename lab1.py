from math import tan, sqrt


def task1():
    print("Привет! Приступаю к решению задания N1")
    # блок ввода данных
    x = float(input("Введи x: "))
    y = float(input("Введи y: "))
    z = float(input("Введи z: "))
    # блок вычисления
    a = (1 + x + abs(y) ** 0.5) / (x + 3 * sqrt(y))
    b = tan((x - y) / (x + y))
    # блок вывода данных
    print("Ответ: a = {0:.4f}, b = {1:.4f}. Спасибо, что воспользовался мной!".format(a, b))


task1()


def task2():
    print("Привет! Приступаю к решению задания N2")
    # блок ввода данных
    x = float(input("Введи x: "))
    # блок вычисления
    a = -2
    b = -2
    x_result = (a * ((x ** b + x) / 3) - (x ** b) ** (1 / 3))
    # блок вывода данных
    print('Ответ: x = {:.4f}. Спасибо, что воспользовался мной!'.format(x_result))


task2()

import math


def task3():
    print('Привет! Приступаю к решению задания N3')

    x = float(input('введи x: '))

    base = 3

    x_result = (math.log(math.cosh(x ** 1 / 3), base))

    print('Ответ: x = {:.4f}. Спасибо, что воспользовался мной!'.format(x_result))


task3()

import math


def task5():
    print('Привет! Приступаю к решению задания N5')

    m1 = float(input('введи m1: '))
    v1 = float(input('введи v1: '))
    m2 = float(input('введи m2: '))
    v2 = float(input('введи v2: '))

    v = (m1 * v1 + m2 * v2) / (m1 + m2)
    v1_after = 2 * v - v1
    v2_after = 2 * v - v2

    print("Скорость движения тележек после соударения: {:.2f} м/с".format(v))
    print("Скорость первой тележки после соударения: {:.2f} м/с".format(v1_after))
    print("Скорость второй тележки после соударения: {:.2f} м/с".format(v2_after))


task5()


def task9():
    print('Привет! Приступаю к решению задания N9')

    exchange_rate = 0.098
    commission = 0.01

    amount_yuan = float(input("Введите сумму в юанях ¥: "))

    amount_rubles = amount_yuan * exchange_rate * (1 - commission)
    amount_rubles = round(amount_rubles, 2)

    print("Сумма в рублях: {:.2f}".format(amount_rubles))


task9()
