# -*- coding: utf-8 -*-



# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

from random import randint
from termcolor import cprint
# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.



class Man:
    MAX_PETS = 10

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.my_pets = []

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 30
            self.house.food -= 30
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def get_cat(self):
        if cats:
            cat = cats.pop()
            self.my_pets.append(cat)
            print(f'У {self.name} в доме поселился кот {cat.name}')
            if self.house.cat_food < 10 and cat.fullness < 2:
                self.buy_cat_food(self.house)
        else:
            cprint('Больше котов брать не могу', color='cyan')

    def buy_cat_food(self, house):
        self.house.cat_food += 50
        self.house.money -= 50
        print(f'{self.name} купил для кота еды.')

    def clean_house(self, house):
        self.house.dirt -= 100
        self.fullness -= 20
        print(f'{self.name} убрался в доме.')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 20:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif len(self.my_pets) < 5:
            self.get_cat()
        elif self.house.dirt > 150:
            self.clean_house(self.house)
        elif self.house.cat_food < 10 and len(self.my_pets) > 0:
            self.buy_cat_food(self.house)
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.cat_food = 0
        self.dirt = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, грязь в доме {}, еды у кота {}'.format(
            self.food, self.money, self.dirt, self.cat_food)


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 1
        self.house = house

    def __str__(self):
        return 'Кот {} имеет сытость {}.'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint(f'Кот {self.name} покушал.', color='blue')
            self.fullness += 10
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды для кота '.format(self.name), color='red')

    def sleep(self):
        self.fullness -= 10
        cprint(f'Кот {self.name} спит.', color='blue')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint(f'Кот {self.name} подрал обои.', color='blue')

    def act(self):

        if self.fullness < 0:
            cprint('Кот {} умер...'.format(self.name), color='red')
            return

        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1 or dice == 4:
            self.tear_wallpaper()
        else:
            self.sleep()


citizens = [
    Man(name='Самурай Джек'),
]
my_sweet_home = House()
cats = [
    Cat('Мурчик', house=my_sweet_home),
    Cat('Пушок', house=my_sweet_home),
    Cat('Рыжик', house=my_sweet_home),
    Cat('Fluffy', house=my_sweet_home),
    Cat('Гав', house=my_sweet_home),
]

for citizen in citizens:
    citizen.go_to_the_house(house=my_sweet_home)

for day in range(1, 1000):
    print('================ день {} =================='.format(day))
    for citizen in citizens:
        citizen.act()
        if len(citizen.my_pets) > 0:
            for pet in citizen.my_pets:
                pet.act()
    print('--- в конце дня ---')
    for citizen in citizens:
        print(citizen)
    for pet in citizen.my_pets:
        print(pet)
    print(my_sweet_home)


# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
