# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

# TODO здесь ваш код
def draw_figure(point=sd.random_point(), angle=0, length=100):
    """
    :param angle: угол наклона вектора
    :type length: длина вектора
    :param point: начальная точка вектора
    :param length: длина вектора
    :return: равносторонняя фигура
    """

    figure_dict = {1: 'треугольник', 2: 'квадрат',
                   3: 'пятиугольник', 4: 'шестиугольник'
                   }
    for key in figure_dict.keys():
        print(key, ": ", figure_dict[key])

    figure_num = int(input("Выбираем фигуру: "))
    while figure_num not in [1, 2, 3, 4]:
        print("Вы ввели некорректное число для фигуры, попробуйте снова")
        figure_num = int(input("Выбирай фигуру: "))
    else:
        figure = figure_dict[figure_num]
    print()
    print(f"Ты выбрал {figure}")
    print()

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
        print("Вы ввели некорректное число для цвета, попробуйте снова")
        color_num = int(input("Выбирай цвет фигуры: "))
    else:
        color = list(color_list[color_num].values())[0]
    print()
    print(f"Ты выбрал цвет {list(color_list[color_num].keys())[0]} для фигуры")
    print()
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

    print("Твоя фигура на экране!!!")


draw_figure(point=sd.random_point(), angle=0, length=100)

sd.pause()
