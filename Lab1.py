from math import tan, sqrt


def task1():
    print("Привет! Приступаю к решению задания N1")
    # блок ввода данных
    x = float(input("Введи x: "))
    y = float(input("Введи y: "))
    z = float(input("Введи z: "))
    # блок вычисления
    a = (1 + x + (abs(y))*(1/2)) / (x + (y*(1/3)))
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
    x_result = (a * ((x ** b + x) / 3) - (x ** b) * (1 / 3))
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

def task4(radius=None, distance=None):
    print('Привет! Приступаю к решению задания N4')
    
    if radius is None:
        radius = float(input("Введите радиус: "))
    if distance is None:
        distance = float(input("Введите расстояние: "))
    
    section_area = calculate_section_area(radius, distance)
    print("Площадь сечения шара:", section_area)
    
def calculate_section_area(radius, distance):
    if distance >= radius:
        return 0
    else:
        section_radius = math.sqrt(radius**2 - distance**2)
        section_area = math.pi * section_radius**2
        return section_area
    
task4()   

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

import math

def task6():
    print('Привет! Приступаю к решению задания N6')

def calculate_prism_surface_area(radius, height):
    
    cylinder_circumference = 2 * math.pi * radius
    
    prism_surface_area = cylinder_circumference * height
    
    return prism_surface_area

task6()

radius = float(input("Введите радиус основания цилиндра: "))
height = float(input("Введите высоту цилиндра: "))

surface_area = calculate_prism_surface_area(radius, height)

print("Площадь боковой поверхности призмы:", surface_area)

def task7():
    print('Привет! Приступаю к решению задания N7')
    
    def solve_quadratic_equation(A, B, C):
        
        discriminant = B**2 - 4*A*C
    
        
        if discriminant < 0:
            print("Действительных корней нет.")
        else:
            
            root1 = (-B + math.sqrt(discriminant)) / (2*A)
            root2 = (-B - math.sqrt(discriminant)) / (2*A)
    
            
            if root1 < root2:
                print("{:.4f}".format(root1))
                print("{:.4f}".format(root2))
            else:
                print("{:.4f}".format(root2))
                print("{:.4f}".format(root1))
    
    
    A = float(input("Введите коэффициент A: "))
    B = float(input("Введите коэффициент B: "))
    C = float(input("Введите коэффициент C: "))
    
    
    if A == 0:
        print("Коэффициент A не может быть нулем.")
    else:
        
        solve_quadratic_equation(A, B, C)
    
task7()

def task8():
    print('Привет! Приступаю к решению задания N8')

    def calculate_angular_velocity(latitude):

        latitude_rad = math.radians(latitude)

        angular_velocity = 2 * math.pi / 24  # 2π / 24 часа

        return angular_velocity

    def calculate_linear_velocity(radius, latitude):
        
        angular_velocity = calculate_angular_velocity(latitude)

        linear_velocity = radius * angular_velocity

        return linear_velocity

    def calculate_linear_acceleration(radius, latitude):
        
        angular_velocity = calculate_angular_velocity(latitude)

        linear_acceleration = radius * angular_velocity**2

        return linear_acceleration

    radius_earth = 6370

    latitude = float(input("Введите широту точки в градусах: "))

    linear_velocity = calculate_linear_velocity(radius_earth, latitude)
    print("Линейная скорость точки на широте {}: {:.2f} км/ч".format(latitude, linear_velocity))

    linear_acceleration = calculate_linear_acceleration(radius_earth, latitude)
    print("Линейное ускорение точки на широте {}: {:.2f} км/ч^2".format(latitude, linear_acceleration))

task8()

def task9():
    print('Привет! Приступаю к решению задания N9')

    exchange_rate = 0.098
    commission = 0.01

    amount_yuan = float(input("Введите сумму в юанях ¥: "))

    amount_rubles = amount_yuan * exchange_rate * (1 - commission)
    amount_rubles = round(amount_rubles, 2)

    print("Сумма в рублях: {:.2f}".format(amount_rubles))


task9()