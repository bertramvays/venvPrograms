# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water:

    def __init__(self):
        self.name = 'water'

    def __str__(self):
        return 'I\'m water'

    def __add__(self, other):

        if other.name == 'air':
            return Storm()
        elif other.name == Fire():
            return Steam()
        elif other.name == Ground():
            return Dirt()
        else:
            return 'Hello'


class Air:

    def __init__(self):
        self.name = 'air'

    def __str__(self):
        return 'I\'m air'

    def __add__(self, other):
        if other.name == 'fire':
            return Flash()
        elif other.name == 'ground':
            return Dust()
        else:
            return None


class Fire:

    def __init__(self):
        self.name = 'fire'

    def __str__(self):
        return 'I\'m fire'

    def __add__(self, other):
        if other.name == "ground":
            return Lava()
        else:
            return None


class Ground:

    def __init__(self):
        self.name = 'ground'

    def __str__(self):
        return 'I\'m ground'


class Storm:

    def __init__(self):
        self.name = 'storm'

    def __str__(self):
        return 'I\'m storm'


class Steam:

    def __init__(self):
        self.name = 'steam'

    def __str__(self):
        return 'I\'m steam'


class Dirt:

    def __init__(self):
        self.name = 'dirt'

    def __str__(self):
        return 'I\'m dirt'


class Flash:

    def __init__(self):
        self.name = 'flash'

    def __str__(self):
        return 'I\'m flash'


class Dust:

    def __init__(self):
        self.name = 'dust'

    def __str__(self):
        return 'I\'m dust'


class Lava:
    def __init__(self):
        self.name = 'lava'

    def __str__(self):
        return 'I\'m lava'


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
