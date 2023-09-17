#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother', 'father', 'brother', 'sister']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Anna', 153],
    ['Tom', 167],
    ['Peter', 187],
    ['Lise', 164],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
for ch, ex in zip(my_family, my_family_height):
    print(f"Рост {ch} - {ex[1]} см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

def sum_height_family(d: list) -> int:
    s = 0
    for i in d:
        s += i[1]
    return s

print(sum_height_family(my_family_height))