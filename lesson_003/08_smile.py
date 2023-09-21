# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
sd.resolution = (1200, 600)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
x0 = 600
y0 =300

sd.circle(sd.get_point(x0, y0), 250)
sd.circle(sd.get_point(x0-100, y0+75))
sd.circle(sd.get_point(x0+100, y0+75))
sd.ellipse(left_bottom=sd.get_point(x0-50, y0-50),
           right_top=sd.get_point(x0+50, y0), color=sd.COLOR_BLUE
           )

point_list = [sd.get_point(x0-125, y0-100), sd.get_point(x0+125, y0-100), sd.get_point(x0, y0-125)]
sd.polygon(point_list, width=10, color=sd.COLOR_ORANGE)
sd.pause()
