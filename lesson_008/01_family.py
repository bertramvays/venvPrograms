# -*- coding: utf-8 -*-

from termcolor import cprint, colored
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# +Все они живут в одном доме, дом характеризуется:
# +  кол-во денег в тумбочке (в начале - 100)
# +  кол-во еды в холодильнике (в начале - 50)
# +  кол-во грязи (в начале - 0)
#
# +У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# +Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# +Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# +Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# +Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# +Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# +Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# +Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# +Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# +Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 250
        self.dirt = 0
        self.cat_food = 150

    def act(self):
        self.dirt += 5

    def __str__(self):
        return colored(f'В доме:\n\t >>>денег: {self.money}, >>>еды:{self.food},'
                       f' >>>грязи:{self.dirt}', color='blue')


class Human:
    total_eated_food = 0

    def __init__(self, name, house):
        self.fullness = 50
        self.happiness = 100
        self.name = name
        self.house = house

    def __str__(self):
        return (colored(f'{self.name} >> '
                        f'уровень сытости: {self.fullness}, '
                        f'уровень счатья: {self.happiness}.', color='yellow'))

    def petting_cat(self):
        self.happiness += 5 * len(cats)
        print(f'{self.name} гладит кота. Кот мурлыкает.')


class Husband(Human):
    total_earned_money = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def eat(self):
        if self.house.food >= 50:
            self.fullness += 50
            self.house.food -= 50
            Human.total_eated_food += 50
            cprint(f'{self.name} - поел.', color='blue')
        else:
            # self.fullness -= 10
            # self.happiness -= 10
            cprint(f'В доме не хватает еды.'
                   f'{self.name} не может поесть.', color='red')

    def work(self):
        self.house.money += 350
        Husband.total_earned_money += 350
        self.fullness -= 30
        cprint(f'{self.name} - поработал.', color='blue')

    def gaming(self):
        self.happiness += 20
        self.fullness -= 10
        cprint(f'{self.name} - поиграл.', color='blue')

    def buy_cat_food(self):
        if self.house.money >= 90:
            self.house.cat_food += 90
            self.house.money -= 90
            cprint(f'{self.name} купил коту еды.', color='blue')
        else:
            cprint(f'Нет денег купить коту еды. {self.name} завтра пойдет на работу.', color='red')

    def act(self):
        if self.fullness < 0:
            print(colored(f'{self.name} умер!!!!', color='red'))
            return
        elif self.happiness < 10:
            print(colored(f'{self.name} умер от депресии!!!!', color='red'))
            return
        elif self.house.dirt > 90:
            self.happiness -= 10
        if self.fullness <= 50:
            self.eat()
            return
        elif self.house.money < 90:
            self.work()
            return
        elif self.house.cat_food <= 70:
            self.buy_cat_food()
        dice = randint(1, 6)
        if dice == 1 or dice == 2:
            self.work()
        elif dice == 3:
            self.eat()
        elif dice == 4:
            self.petting_cat()
        else:
            self.gaming()


class Wife(Human):
    total_fur_coats = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def __str__(self):
        return super().__str__()

    def eat(self):
        if self.house.food > 25:
            self.fullness += 25
            self.happiness += 10
            self.house.food -= 25
            Human.total_eated_food += 25
            cprint(f'{self.name} - поела.', color='magenta')
        else:
            cprint(f'В доме не хватает еды.'
                   f'{self.name} не может поесть.', color='red')

    def shopping(self):
        if self.house.money >= 90:
            self.house.food += 150
            self.house.money -= 150
            self.fullness -= 20
            self.happiness += 15
            cprint(f'{self.name} - сходила за покупками.', color='magenta')
        else:
            cprint(f'В доме не хватает денег, '
                   f'{self.name} не может сходить за покупками.', color='red')

    def buy_fur_coat(self):
        if self.house.money > 350:
            self.house.money -= 350
            self.fullness -= 10
            self.happiness += 60
            Wife.total_fur_coats += 1
            cprint(f'{self.name} - купила шубу.', color='magenta')
        else:
            self.happiness -= 20
            cprint(f'{self.name} хотела купить шубу. Но денег не нее нехватает. '
                   f'Она расcтроена, будет просить мужа,'
                   f' чтобы он сходил на работу', color='magenta')

    def clean_house(self):
        self.house.dirt -= 50
        self.fullness -= 10
        self.happiness += 5
        cprint(f'{self.name} - сделала уборку в доме.', color='magenta')

    def act(self):
        if self.fullness < 0:
            print(colored(f'{self.name} умерла!!!!', color='red'))
            return
        elif self.happiness < 10:
            print(colored(f'{self.name} умерла от депресии!!!!', color='red'))
            return
        elif self.house.dirt > 90:
            self.happiness -= 10
        if self.house.food < 100:
            self.shopping()
            return
        elif self.fullness < 20:
            self.eat()
            return
        dice = randint(1, 6)
        if dice == 1 or dice == 2:
            if self.house.dirt > 80:
                self.clean_house()
            else:
                self.eat()
        elif dice == 3:
            self.shopping()
        elif dice == 4:
            self.buy_fur_coat()
        elif dice == 5:
            self.petting_cat()
        else:
            self.eat()


class Child(Human):

    def __init__(self, name, house):
        super().__init__(name, house)
        self.happiness = 100

    def __str__(self):
        return 'Ребенок ' + super().__str__()

    def eat(self):
        if self.house.food > 10:
            self.fullness += 10
            self.house.food -= 10
            Human.total_eated_food += 10
            cprint(f'Ребенок {self.name} - поел.', color='magenta')
        else:
            cprint(f'В доме не хватает еды.'
                   f'Ребенок {self.name} не может поесть.', color='red')

    def sleep(self):
        self.fullness -= 20
        cprint(f'Ребенок {self.name} - поcпал.', color='magenta')

    def act(self):
        if self.fullness < 0:
            print(colored(f'Ребенок {self.name} умерл!!!!', color='red'))
            return
        elif self.fullness < 20:
            self.eat()
            return
        dice = randint(1, 6)
        if dice == 1 or dice == 2:
            self.eat()
        else:
            self.sleep()


class Cat:

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.house = house

    def __str__(self):
        return 'Кот {} имеет сытость {}.'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.cat_food >= 10:
            cprint(f'Кот {self.name} покушал.', color='blue')
            self.fullness += 30
            self.house.cat_food -= 10
        else:
            cprint('{} нет еды для кота '.format(self.name), color='red')
            self.fullness -= 10

    def sleep(self):
        self.fullness -= 10
        cprint(f'Кот {self.name} спит.', color='blue')

    def tear_wallpaper(self):
        self.fullness -= 10
        self.house.dirt += 5
        cprint(f'Кот {self.name} подрал обои.', color='blue')

    def act(self):

        if self.fullness <= 0:
            cprint('Кот {} сдох...'.format(self.name), color='red')
            return

        dice = randint(1, 6)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1 or dice == 4:
            self.tear_wallpaper()
        else:
            self.sleep()

cats_count = 9
cats_names = ['Мурзик', 'Рыжик', 'Пушок', 'Пушистик', 'Белые лапки', 'Пеструха', 'Мурка', 'Трикси', 'Дикси',]
home = House()
serge = Husband('Сережа', home)
masha = Wife('Маша', home)
kolya = Child('Коля', home)
cats = []
for _ in range(cats_count):
    cats.append(Cat(cats_names.pop(), home))



for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    for cat in cats:
        cat.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    for cat in cats:
        cprint(cat, color='cyan')
    cprint(home, color='green')


print(f'За год семья заработала денег: {Husband.total_earned_money}, '
      f'сьела еды: {Human.total_eated_food} , купила шуб: {Wife.total_fur_coats}. В семье было {len(cats)} кота.')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
