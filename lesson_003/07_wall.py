# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (1200, 600)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код

x0 = 0
y0 = 0
side_x = 100
side_y = 50
num_stone_x = 12
num_stone_y = 12

for i in range(0, num_stone_y+1):
    for j in range(0, num_stone_x+1):
        point_left_0 = sd.get_point(x0, y0)
        point_right_0 = sd.get_point(x0+side_x, y0+side_y)
        sd.rectangle(left_bottom=point_left_0, right_top=point_right_0, width=1)
        x0 += side_x
    y0 += side_y
    x0 = 0


sd.pause()
