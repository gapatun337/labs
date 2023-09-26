from math import tan, sqrt


def task1():
    print("Привет! Приступаю к решению задания N1")

    x = float(input("Введи x: "))
    y = float(input("Введи y: "))
    z = float(input("Введи z: "))

    a = (1 + x + abs(y) ** 0.5) / (x + 3 * sqrt(y))
    b = tan((x - y) / (x + y))

    print("Ответ: a = {0:.4f}, b = {1:.4f}. Спасибо, что воспользовался мной!".format(a, b))


task1()
