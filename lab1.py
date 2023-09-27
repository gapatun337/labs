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
