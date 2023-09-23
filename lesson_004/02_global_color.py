# -*- coding: utf-8 -*-
import simple_draw as sd


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
def draw_figure(figure=None, point=sd.random_point(), angle=0, length=100):
    """
    :param angle: угол наклона вектора
    :type length: длина вектора
    :param point: начальная точка вектора
    :param length: длина вектора
    :return: равносторонняя фигура
    """
    color_list = {
        1: {'red': sd.COLOR_RED},
        2: {'orange': sd.COLOR_ORANGE},
        3: {"yellow": sd.COLOR_YELLOW},
        4: {"green": sd.COLOR_GREEN},
        5: {"cyan": sd.COLOR_CYAN},
        6: {"blue": sd.COLOR_BLUE},
        7: {"purple": sd.COLOR_PURPLE},
    }
    for key in color_list.keys():
        for k in color_list[key]:
            print(key, ": ", k)

    color_num = int(input("Выбирай цвет фигуры: "))
    while color_num not in [1, 2, 3, 4, 5, 6]:
        print("Вы ввели некорректное число, попробуйте снова")
        color_num = int(input("Выбирай цвет фигуры: "))
    else:
        color = list(color_list[color_num].values())[0]

    assert isinstance(point, object)
    point = point
    if figure == 'треугольник':
        for a in range(3):
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
            v1.draw(color=color)
            angle += 120
            point = v1.end_point

    elif figure == 'квадрат':
        for a in range(4):
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
            v1.draw(color=color)
            angle += 90
            point = v1.end_point

    elif figure == 'шестиугольник':
        for a in range(6):
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
            v1.draw(color=color)
            angle += 60
            point = v1.end_point

    elif figure == 'пятиугольник':
        for a in range(5):
            v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
            v1.draw(color=color)
            angle += 72
            point = v1.end_point
    else:
        print("Укажите фигуру и попробуйте еще раз")

    print("Ваша фигура на экране!!!")
# TODO здесь ваш код
draw_figure(point=sd.random_point(), angle=0, length=100, figure='треугольник')
sd.pause()
