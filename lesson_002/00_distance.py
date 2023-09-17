#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from itertools import combinations
from typing import List, Dict

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}


def distance_between_cities(sities: Dict, result_dict: Dict) -> Dict:
    for sity in combinations(sities.keys(), 2):
        first, second = sity
        x1, y1 = sities[first]
        x2, y2 = sities[second]
        key = first + '_' + second
        result_dict[key] = round(((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5, 2)
    return result_dict


distances = distance_between_cities(sities=sites, result_dict=distances)
print(distances)




