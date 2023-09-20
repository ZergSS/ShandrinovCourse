# -*- coding: utf-8 -*-
import random

import simple_draw as sd

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
width = 1
radius0 = 25
x = 300
y = 300


# for i in [10, 20, 30]:
#     sd.circle(center_position=sd.get_point(x, y), radius=radius0+i, width = 2)

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
def draw_circle(x: float, y: float, radius: float, step: int, num: int, color=sd.COLOR_ORANGE):
    x0 = x
    y0 = y
    for i in range(0, num):
        sd.circle(center_position=sd.get_point(x0, y0), radius=radius)
        x0 += 2 * step


# Нарисовать 10 пузырьков в ряд
# draw_circle(x, y, radius0, step=radius0, num=10)
# Нарисовать три ряда по 10 пузырьков

# for i in range(0, 3):
#     draw_circle(x, y, radius0, step=radius0, num=10)
#     y += 2 * radius0


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами

def draw_circle_random_set(radius=25, step=0, num=100):
    for i in range(1, num + 1):
        sd.circle(sd.random_point(), radius=radius, color=sd.random_color())


draw_circle_random_set()

sd.pause()
