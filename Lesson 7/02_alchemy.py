# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   +Вода + Воздух = Шторм
#   +Вода + Огонь = Пар
#   +Вода + Земля = Грязь
#   +Воздух + Огонь = Молния
#   +Воздух + Земля = Пыль
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
        elif other.name == 'fire':
            return Steam()
        elif other.name == 'ground':
            return Dirt()
        else:
            return None


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
        elif other.name == 'water':
            return Storm()
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
        elif other.name == 'air':
            return Flash()
        elif other.name == 'water':
            return Steam()
        else:
            return None


class Ground:

    def __init__(self):
        self.name = 'ground'

    def __str__(self):
        return 'I\'m ground'

    def __add__(self, other):
        if other.name == "fire":
            return Lava()
        elif other.name == 'air':
            return Dust()
        elif other.name == 'water':
            return Dirt()
        else:
            return None


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


# print(Water(), '+', Air(), '=', Water() + Air())
# print(Water(), '+', Air(), '=', Air() + Water())
# print(Fire(), '+', Air(), '=', Fire() + Air())
# print(Fire(), '+', Air(), '=', Air() + Fire())
# print(Water(), '+', Fire(), '=', Water() + Fire())
# print(Water(), '+', Fire(), '=', Fire() + Water())
# print(Water(), '+', Ground(), '=', Water() + Ground())
# print(Water(), '+', Ground(), '=', Ground() + Water())
# print(Air(), '+', Ground(), '=', Air() + Ground())
# print(Air(), '+', Ground(), '=', Ground() + Air())
print(Fire(), '+', Ground(), '=', Fire() + Ground())
print(Fire(), '+', Ground(), '=', Ground() + Fire())
