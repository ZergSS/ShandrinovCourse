import random


class Lem:
    total, names = 0, ['Peter', 'Anna', 'Rem', 'Nik', 'Sofi', 'Denn', 'Lora', 'Sofa', 'Bred', 'Greg']

    def __init__(self):
        Lem.total += 1
        self.name = random.choice(Lem.names)

    def __repr__(self):
        return "I'm lemming, my name is  " + self.name + ". I'm next!!! "


for i in range(1, 101):
    if i % 2 == 0:
        lem = Lem()
        print(lem)

print(lem.total)